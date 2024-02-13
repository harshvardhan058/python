password = "ndjksamdklmk"
passwordLength = len(password)

if passwordLength <= 6:
    strength = "Weak"
elif passwordLength <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Your Password is",strength)