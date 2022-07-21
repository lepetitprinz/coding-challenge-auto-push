def encrytion(text, width):
    text = text.replace(' ', '')
    text = list(text.upper())
    length = len(text)

    encryted = [''] * length
    start_index = 0
    j = 0
    for i in range(length):
        idx = start_index + j * width
        if idx < length:
            encryted[idx] = text[i]
            j += 1
            if idx + width >= length:
                j = 0
                start_index += 1

    return ''.join(encryted)

while True:
    width = int(input())
    if width == 0:
        break
    else:
        text = input()
        print(encrytion(text, width))