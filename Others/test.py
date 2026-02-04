import subprocess
from datetime import datetime


def get_windows_uptime():
    try:
        # Execute 'systeminfo' and decode the output
        result = subprocess.run(
            ["systeminfo"], capture_output=True, text=True, check=True
        )
        output_lines = result.stdout.splitlines()

        # Search for the "System Boot Time" line
        for line in output_lines:
            if "System Boot Time:" in line:
                boot_time_str = line.split("System Boot Time:")[1].strip()
                return boot_time_str
        return "System Boot Time not found."
    except Exception as e:
        return f"Error getting uptime: {e}"


if __name__ == "__main__":
    starttime = [
        int(x)
        for x in get_windows_uptime().replace(":", ", ").replace("-", ", ").split(", ")
    ]
    currenttime = [
        int(x) for x in datetime.now().strftime("%d %m %Y %H %M %S").split(" ")
    ]
    uptime = str([currenttime[index] - i for index, i in enumerate(starttime)])
    print(f"OS Uptime: {uptime}")
