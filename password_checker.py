import re

def check_password_strength(password):
    # Score starts at 0
    score = 0
    
    # Length check
    if len(password) >= 8:
        score += 1

    # Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1

    # Special characters
    if re.search(r"[@$!%*?&#]", password):
        score += 1

    # Final evaluation
    if score <= 2:
        return "Weak ❌"
    elif score == 3 or score == 4:
        return "Medium ⚠️"
    else:
        return "Strong ✅"

if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    print("Strength:", check_password_strength(pwd))
