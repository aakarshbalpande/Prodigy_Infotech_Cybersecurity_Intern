def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        elif char.isdigit():
            result += chr((ord(char) + shift - 48) % 10 + 48)
        else:
            result += char
    return result
def main():
    print("Caesar Cipher Program")
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
    
    if choice not in ['e', 'd']:
        print("Invalid choice! Please choose 'e' for encrypt or 'd' for decrypt.")
        return
    message = input("Enter your message : ")
    shift = int(input("Enter the shift value : "))
    if choice == 'e':
        encrypted_message = caesar_cipher(message, shift)
        print("Encrypted Message:", encrypted_message)
    else:
        decrypted_message = caesar_cipher(message, -shift)
        print("Decrypted Message:", decrypted_message)
if __name__ == "__main__":
    main()