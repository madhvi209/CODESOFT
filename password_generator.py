import random
import string

def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_punctuation=True):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters to ensure complexity.")

    # Define character sets
    characters = ""
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    # Ensure the password has at least one of each character type if selected
    password = []
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_punctuation:
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password length with random choices from the selected character set
    password += random.choices(characters, k=length - len(password))

    # Shuffle the resulting password to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def get_user_preferences():
    try:
        password_length = int(input("Enter the desired password length (at least 4): "))
        use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_punctuation = input("Include special characters? (y/n): ").strip().lower() == 'y'
        return password_length, use_upper, use_lower, use_digits, use_punctuation
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")
        return get_user_preferences()

def save_password(password):
    with open("generated_passwords.txt", "a") as f:
        f.write(password + "\n")
    print("Password saved to generated_passwords.txt.")

def main():
    password_length, use_upper, use_lower, use_digits, use_punctuation = get_user_preferences()

    try:
        generated_password = generate_password(password_length, use_upper, use_lower, use_digits, use_punctuation)
        print("Generated Password:", generated_password)

        save_choice = input("Would you like to save this password? (y/n): ").strip().lower()
        if save_choice == 'y':
            save_password(generated_password)

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
