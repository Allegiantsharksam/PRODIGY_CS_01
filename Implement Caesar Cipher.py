class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, message):
        encrypted_message = ""
        for char in message:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                encrypted_message += chr((ord(char)-ascii_offset + self.shift) % 26 + ascii_offset)
            else:
                encrypted_message+=char
        return encrypted_message
    def decrypt(self, encrypted_message):
        decrypted_message = ""
        for char in encrypted_message:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                decrypted_message += chr((ord(char) - ascii_offset - self.shift) % 26 + ascii_offset)
            else:
                decrypted_message += char
        return decrypted_message
def main():
    shift = int(input("Enter the shift value: "))
    cipher = CaesarCipher(shift)

    message = input("Enter the message to encrypt: ")
    encrypted_message = cipher.encrypt(message)
    print(f"Encrypted message: {encrypted_message}")

    decrypted_message = cipher.decrypt(encrypted_message)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
