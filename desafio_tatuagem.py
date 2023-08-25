def unicode_shift(unicode_code, shift_amount):
    try:
        unicode_value = int(unicode_code[2:], 16)  # Remove "U+" e converte em valor numérico
        shifted_unicode_value = unicode_value + shift_amount
        shifted_character = chr(shifted_unicode_value)
        return shifted_character
    except ValueError:
        return None

shift_amount = -2031

unicode_code = input("Input: ")
shifted_character = unicode_shift(unicode_code, shift_amount)

if shifted_character is not None:
    print(f"Caractere original: {unicode_code}")
    print(f"Caractere deslocado: {shifted_character}")
else:
    print("Entrada inválida ou não é um caractere Unicode válido.")


#U+0810	U+080F	U+0816	U+0812	U+0820	U+0816	U+0816	U+080C
