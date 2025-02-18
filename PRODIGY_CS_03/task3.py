import re
def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[@$!%*?&]', password) is not None
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria,
                        number_criteria, special_char_criteria])
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should contain at least one number.")
    if not special_char_criteria:
        feedback.append("Password should contain at least one special character (e.g., @$!%*?&).")
    return strength, feedback
def main():
    print("Password Complexity Checker")
    while True:
        password = input("Enter a password to assess its strength (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            print("Goodbye!")
            break
        strength, feedback = assess_password_strength(password)
        print(f"Password Strength: {strength}")
        if feedback:
            print("Feedback:")
            for line in feedback:
                print(f"- {line}")
        else:
            print("Your password meets all strength criteria!")
if __name__ == "__main__":
    main()