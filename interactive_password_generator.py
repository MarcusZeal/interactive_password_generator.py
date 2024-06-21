import random
import string

def generate_password(length, num_special_chars):
    if num_special_chars > length:
        raise ValueError("Number of special characters cannot exceed total length.")
    
    all_characters = string.ascii_letters + string.digits
    special_characters = string.punctuation
    
    password_chars = random.choices(special_characters, k=num_special_chars)
    remaining_length = length - num_special_chars
    password_chars += random.choices(all_characters, k=remaining_length)
    random.shuffle(password_chars)
    password = ''.join(password_chars)
    
    return password

def main():
    try:
        length = int(input("Enter the total length of the password: "))
        num_special_chars = int(input("Enter the number of special characters: "))
        password = generate_password(length, num_special_chars)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
