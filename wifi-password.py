import subprocess
import re
name_regex = re.compile(r"All User Profile\s+: (.*)\b")
password_regex = re.compile(r"Key Content\s+: (.*)\b")

result_1 = subprocess.run(
    ["netsh", "wlan", "show", "profiles"], text=True, capture_output=True, check=True)

wifi_names = name_regex.findall(result_1.stdout)

for name in wifi_names:

    name = r"{}".format(name)

    try:
        result_2 = subprocess.run(["netsh", "wlan", "show", "profiles", str(
            name), "key=clear"], text=True, capture_output=True, check=True)
        password = password_regex.findall(result_2.stdout)
        if len(password) != 0:
            print(name, password[0])
        else:
            print(name, "OPEN WIFI")
    except:
        print(name, "Unable to get password")
