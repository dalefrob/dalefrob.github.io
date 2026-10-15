alphabet = " abcdefghijklmnopqrstuvwxyz"
message = input("Message: ").lower()
shift = int(input("Shift: "))

secret = ""

for letter in message:
    if letter in alphabet:
        position = alphabet.index(letter)
        new_position = (position + shift) % len(alphabet)
        secret = secret + alphabet[new_position]
    else:
        secret = secret + letter

print(secret)