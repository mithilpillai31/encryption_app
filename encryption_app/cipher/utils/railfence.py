def encrypt_rail_fence(text, key):
    fence = [[' ' for _ in range(len(text))] for _ in range(key)]
    direction, row, col = -1, 0, 0
    for char in text:
        fence[row][col] = char
        col += 1
        if row == 0 or row == key - 1:
            direction *= -1
        row += direction
    encrypted_text = ''.join(char for row in fence for char in row if char != ' ')
    print("Rail Fence Cipher Table:")
    for row in fence:
        print(' '.join(row))
    print()
    return encrypted_text


def decrypt_rail_fence(text, key):
    fence = [[' ' for _ in range(len(text))] for _ in range(key)]
    direction, row, col = -1, 0, 0
    for _ in text:
        fence[row][col] = '*'
        col += 1
        if row == 0 or row == key - 1:
            direction *= -1
        row += direction

    index = 0
    for i in range(key):
        for j in range(len(text)):
            if fence[i][j] == '*' and index < len(text):
                fence[i][j] = text[index]
                index += 1
    decrypted_text = ''.join(fence[i][j] for j in range(len(text)) for i in range(key) if fence[i][j] != ' ')
    print("Rail Fence Cipher Table:")
    for row in fence:
        print(' '.join(row))
    print()
    return decrypted_text
