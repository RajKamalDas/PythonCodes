import requests

try:
    response = requests.get(
        "https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{value}}}"
    )
    if response.status_code == 200:
        data = response.json()
        board = data['newboard']['grids'][0]['value']
except Exception as e:
    print(e)
