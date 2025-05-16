alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            if letter in alphabet:
                shift_position = alphabet.index(letter) + shift_amount
                shift_position %= len(alphabet)
                output_text += alphabet[shift_position]

    print(f"here is the {encode_or_decode}d text: {output_text}")

should_condition = True
while should_condition:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' to continue or 'no' to complete:\n").lower()
    if restart == "no":
       should_condition = False
       print("good bye")




