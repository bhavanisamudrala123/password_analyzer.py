import re

password = input("Enter Password: ")

score = 0

if len(password) >= 8:
    score += 1
if re.search(r"[A-Z]", password):
    score += 1
if re.search(r"[a-z]", password):
    score += 1
if re.search(r"\d", password):
    score += 1
if re.search(r"[@$!%*?&]", password):
    score += 1

if score == 5:
    print("Password Strength: Strong")
elif score >= 3:
    print("Password Strength: Medium")
else:
    print("Password Strength: Weak")

if score < 5:
    print("Suggested Password: Secure@123")
