import requests
import keyboard

url = "http://localhost:5000/submit/user069"  # ←Where The “Server” Is
jsonData = {
    "Score": 999,
    "Version": "v1.0.1",
    "Date": "10/01/2026",
}  # ↑ What Gets Posted

# Tries To Post The Record To The “Server”
response = requests.post(url, json=jsonData)

# Show What The “Server” Said
print(response.status_code)
print(response.text)

keyboard.wait("esc")
