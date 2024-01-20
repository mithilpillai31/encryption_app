class MonoalphabeticCipher:
    def __init__(self, key="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        self.alphabet = list(key.upper())
        self.mapping = {c: p for c, p in zip(self.alphabet, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

    def encrypt(self, text):
        return ''.join(self.mapping[char.upper()] if char.isalpha() else char for char in text)

    def decrypt(self, ciphertext):
        reversed_mapping = {p: c for c, p in self.mapping.items()}
        return ''.join(reversed_mapping[char.upper()] if char.isalpha() else char for char in ciphertext)
