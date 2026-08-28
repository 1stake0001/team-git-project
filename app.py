import sys

with open(sys.argv[1], "r") as file:
    requests = file.readlines()

print("===== Security Report =====")
print()
print(f"Total Requests: {len(requests)}")