MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ':' '}


print('Welcome to my text to Morse-Code Converter \n')

def text_converter():
    text = input("Please input the text you want to convert. \n\n")

    d_t = ""
    for char in text:
        if MORSE_CODE_DICT.get(char.upper()) == None:
            print(f"Thr character {char} does not have a Morse Code equivalent, but here is your code anyway. 🤗")
            d_t += char
        else:
            deciphered = MORSE_CODE_DICT.get(char.upper())
            d_t+= f" {deciphered}"

    print(d_t)
    text_converter()
text_converter()