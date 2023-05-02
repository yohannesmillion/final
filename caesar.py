import sys

def encode(message, shift):
    cipher = ""
    for letter in message:
        if letter.isalpha():
            cipher += chr(((ord(letter.upper()) - 65 + shift) % 26) + 65)
    return cipher

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python caesar.py shift")
        sys.exit(1)
    try:
        shift = int(sys.argv[1])
    except ValueError:
        print("Shift must be an integer")
        sys.exit(1)
    message = input().strip()
    cipher = encode(message, shift)
    for i in range(0, len(cipher), 5):
        print(cipher[i:i+5], end=" ")
        if (i+5) % 50 == 0:
            print()
