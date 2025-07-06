import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) < 8:
        feedback.append("Password too short (minimum 8 characters).")
    elif len(password) >= 12:
        score += 2
        feedback.append("Good length.")
    else:
        score += 1
        feedback.append("Moderate length.")

    # Character Variety
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add at least one digit.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Repeated Characters
    if re.search(r'(.)\1{2,}', password):
        feedback.append("Avoid using repeated characters (e.g. aaa, 111).")
    else:
        score += 1

    # Final Rating
    if score >= 7:
        strength = "Very Strong"
    elif score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

# Demo
if __name__ == "__main__":
    password = input("Enter a password to test its strength: ")
    strength, suggestions = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if suggestions:
        print("Suggestions:")
        for s in suggestions:
            print(f" - {s}")
