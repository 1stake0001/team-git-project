import sys

with open(sys.argv[1], "r") as file:
    requests = file.readlines()

failed_logins = sum("/login" in request and "401" in request for request in requests)

ips = {request.split()[0] for request in requests if request.strip()}

print("===== Security Report =====")

print()
print(f"Total Requests Found: {len(requests)}")
print(f"Failed Logins: {failed_logins}")
print(f"Unique IPs: {len(ips)}")

