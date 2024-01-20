def vignere(text, key):
    key_repeated = (key * (len(text) // len(key) + 1))[:len(text)]

    result = ''
    for i in range(len(text)):
        if text[i].isalpha():
            ascii_offset = ord('a') if text[i].islower() else ord('A')
            shift = ord(key_repeated[i].lower()) - ord('a')
            result += chr((ord(text[i]) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += text[i]

    return result

def vignere_decrypt(text, key):
    key_repeated = (key * (len(text) // len(key) + 1))[:len(text)]

    result = ''
    for i in range(len(text)):
        if text[i].isalpha():
            ascii_offset = ord('a') if text[i].islower() else ord('A')
            shift = ord(key_repeated[i].lower()) - ord('a')
            result += chr((ord(text[i]) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            result += text[i]

    return result
