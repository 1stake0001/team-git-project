import sys

with open(sys.argv[1], "r") as file:
    requests = file.readlines()

failed_logins = sum("POST /login 401" in request for request in requests)

print("===== Security Report =====")
print()
print(f"Total Requests: {len(requests)}")
print(f"Failed Logins: {failed_logins}")