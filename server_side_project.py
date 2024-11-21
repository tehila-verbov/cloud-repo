import time
from severityOption import severityOption

path = "/var/log/syslog"
severity_dict = {
                    "timestamp": int, 
                    severityOption.INFO._name_: 0, 
                    severityOption.WARN._name_: 0, 
                    severityOption.ERROR._name_: 0
                 }

with open(path, "r") as file:
    for line in file:
        words = line.split()
        for word in words:
            if word == severityOption.INFO._name_:
                severity_dict[severityOption.INFO._name_] += 1
            elif word == severityOption.WARN._name_:
                severity_dict[severityOption.WARN._name_] += 1
            elif word == severityOption.ERROR._name_:
                severity_dict[severityOption.ERROR._name_] += 1

severity_dict["timestamp"] = int(time.time())
print(severity_dict)
