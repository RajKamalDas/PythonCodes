from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)  # Make the app instance


@app.post("/submit/<userid>")  # URL of end point
def submit(userid):
    newData = request.get_json()
    if not newData:
        return jsonify({"error": "No Data Sent."}), 400
    else:
        do = verify(newData, userid)
        if do == {}:
            with open("Data.json", "r") as file:
                data = json.load(file)
            userid = userid.title()
            data["AllRecords"][userid] = newData
            with open("Data.json", "w") as file:
                json.dump(data, file, indent=4, separators=(",", ": "))  # Decor
            return jsonify({"Success": "All Data Accepted"}), 200
        else:
            return jsonify(do), 400


@app.get("/fetch")  # Endpoint
def fetch():
    with open("Data.json", "r") as file:
        data = json.load(file)
    return jsonify(data["Top10"]), 200


def verify(data, UID):
    mustHave = ["Score", "Version", "Date"]
    allowedVersions = ["v1.0.1", "v1.0.2"]
    if not UID.startswith("user"):
        return {"error": "Invaild userid."}
    for key in mustHave:
        if key not in data:
            return {"error": f"No {key} Sent."}

    version = data["Version"]

    if version not in allowedVersions:
        return {"error": "Non Standard Version."}

    try:
        datetime.strptime(data["Date"], "%d/%m/%Y")
        data["Score"] = data["Score"] + 111

        return {}
    except TypeError:
        return {"error": "Invaild Score Sent. Should Be 0-9 Only."}
    except ValueError:
        return {"error": "Invaild Date Sent. Should Be 'dd/mm/yyyy'"}
