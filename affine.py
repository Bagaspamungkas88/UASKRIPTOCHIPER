import string

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_cipher(text, key, mode):
    result = ""
    a, b = key
    if mode == "encrypt":
        for char in text:
            if char in string.ascii_letters:
                if char.islower():
                    result += chr(((a * (ord(char) - ord('a')) + b) % 26) + ord('a'))
                else:
                    result += chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A'))
            else:
                result += char
    elif mode == "decrypt":
        a_inv = mod_inverse(a, 26)
        if a_inv is None:
            return "Key is not valid for decryption"
        for char in text:
            if char in string.ascii_letters:
                if char.islower():
                    result += chr(((a_inv * (ord(char) - ord('a') - b)) % 26) + ord('a'))
                else:
                    result += chr(((a_inv * (ord(char) - ord('A') - b)) % 26) + ord('A'))
            else:
                result += char
    return result

def main():
    text = input("Masukkan teks: ")
    a = int(input("Masukkan nilai 'a' (integer): "))
    b = int(input("Masukkan nilai 'b' (integer): "))
    key = (a, b)
    mode = input("Encrypt (e) atau Decrypt (d)?: ").lower()

    if mode == "e":
        mode = "encrypt"
    elif mode == "d":
        mode = "decrypt"

    result = affine_cipher(text, key, mode)
    print(f"{mode.capitalize()}ed Text: {result}")

if __name__ == "__main__":
    main()
