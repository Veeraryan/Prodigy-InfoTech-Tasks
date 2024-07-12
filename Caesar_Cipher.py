def encrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    choice = input("Would you like to (E)ncrypt or (D)ecrypt?: ").strip().upper()

    if choice in ['E', 'D']:
        message = input("Enter your message: ")
        shift = int(input("Enter shift value: "))

        if choice == 'E':
            print("Encrypted message:", encrypt(message, shift))
        else:
            print("Decrypted message:", decrypt(message, shift))
    else:
        print("Invalid choice. Please choose 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()