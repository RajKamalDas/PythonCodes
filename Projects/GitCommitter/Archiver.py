def archive_deleted_files(
    deleted_files,
    source_repo="RajKamalDas/PythonCodes",
    archive_repo="RajKamalDas/PythonGraveyard",
):
    import base64
    import requests
    import os
    from datetime import date

    github_token = os.environ["GITHUB_TOKEN"]

    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github+json",
    }

    def last_commit_for_file(repo, path):
        r = requests.get(
            f"https://api.github.com/repos/{repo}/commits",
            headers=headers,
            params={
                "path": path,
                "per_page": 1,
            },
        )
        if r.status_code != 200 or not r.json():
            return None
        return r.json()[0]["sha"]

    def file_at_commit(repo, path, sha):
        r = requests.get(
            f"https://api.github.com/repos/{repo}/contents/{path}",
            headers=headers,
            params={"ref": sha},
        )
        if r.status_code != 200:
            return None
        return base64.b64decode(r.json()["content"])

    def upload(repo, path, content):
        requests.put(
            f"https://api.github.com/repos/{repo}/contents/{path}",
            headers=headers,
            json={
                "message": f"[{date.today()}] Buried {path}",
                "content": base64.b64encode(content).decode("utf-8"),
                "committer": {
                    "name": "Auto Archive Bot",
                    "email": "archive@users.noreply.github.com",
                },
            },
        )

    for i, path in enumerate(deleted_files):
        sha = last_commit_for_file(source_repo, path)
        if not sha:
            continue

        content = file_at_commit(source_repo, path, sha)
        if not content:
            continue

        upload(archive_repo, f"{path}", content)

        print(f"{i+1} Done. {path}|{sha}")
