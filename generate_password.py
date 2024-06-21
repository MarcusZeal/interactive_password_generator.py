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
