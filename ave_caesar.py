alphabet = "abcdefghijklmnopqrstuvwxyz"
def cipher_decode(message, shift):
  decoded_message = ""
  for character in message:
    if character in alphabet:
      character_value = alphabet.find(character)
      decoded_message += alphabet[(character_value + shift) % 26]
    else:
      decoded_message += character
  return decoded_message

def cipher_encode(message, shift):
  encoded_message = ""
  for character in message:
    if character in alphabet:
      character_value = alphabet.find(character)
      encoded_message += alphabet[(character_value - shift) % 26]
    else:
      encoded_message += character
  return encoded_message

print("\033[1;36m")
print("      .o.       oooooo     oooo oooooooooooo")
print("     .888.       `888.     .8'  `888'     `8")
print("    .8\"888.       `888.   .8'    888")
print("   .8' `888.       `888. .8'     888oooo8")
print("  .88ooo8888.       `888.8'      888    \"")
print(" .8'     `888.       `888'       888       o")
print("o88o     o8888o       `8'       o888ooooood8")
print("\033[0m")

print("\nCaesar's Cipher Encoder / Decoder / Brute Forcer")
print("by PrzemoKam 2023\n")

print("\033[1mWhat would you like to do?\033[0m")
print("\033[91m1.\033[0m Decode message (I know shift number)")
print("\033[91m2.\033[0m Decode message (I don't know the shift number - brute force it!")
print("\033[91m3.\033[0m Encode message")

choice = input(
    "\n\033[1mInput your choice (\033[91m1\033[0m, \033[91m2\033[0m or \033[91m3\033[0m):\033[0m ")

if choice == '1':
    message_to_decode = input("\n\033[1mType your message to decode:\033[0m ")
    shift = int(input("\033[1mPlease enter the shift of cipher:\033[0m "))
    print("\033[1mYour decoded message is:\033[0m", cipher_decode(message_to_decode, shift))

elif choice == '2':
    print(
        "\n\033[1mI will iterate through all possible 26 offsets. One of them will be decoded.\033[0m")
    message_to_brute_force = input("\033[1mType your message to decode:\033[0m ")

    for i in range(1, 26):
        print("\n\033[1mTesting offset:\033[0m {}".format(i))
        print(
            "\t \033[1mDecoded message:\033[0m {}".format(cipher_decode(message_to_brute_force, i)))

elif choice == '3':
    message_to_encode = input("\n\033[1mType your message to encode:\033[0m ")
    while True:
        try:
            shift = int(input("\033[1mPlease enter the shift of cipher:\033[0m "))
            break
        except ValueError:
            print("\n\033[1;31mPlease enter a number!\033[0m")
    print("\033[1mYour encoded message is:\033[0m ", cipher_encode(message_to_encode, shift))
    print("\nThanks for testing my script!")

else:
    print(
        "\n\033[1;31mInvalid choice. Try to input numbers 1, 2 or 3 only.\033[0m")
