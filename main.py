import re
from collections import Counter
from colorama import Fore, Style, init
from tabulate import tabulate

init(autoreset=True)

log_file = "logs/auth.log"

with open(log_file, "r") as f:
    logs = f.readlines()

ips = []

for line in logs:
    match = re.search(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", line)
    if match:
        ips.append(match.group())

counter = Counter(ips)

table = []
for ip, count in counter.items():
    if count >= 3:
        table.append([Fore.RED + ip, count, "SUSPECT"])
    else:
        table.append([ip, count, "OK"])

print("\nTentatives de connexion par IP :\n")
print(tabulate(table, headers=["IP", "Tentatives", "Statut"]))