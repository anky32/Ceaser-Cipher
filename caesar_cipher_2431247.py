import os

# Displays a welcome message to the user
def welcome():
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")

# takes input from the user in lower case
def enter_message(mode):
    message = input(f"What message would you like to {mode}: ").lower()
    return message


# the message encrypts using ceaser cipher and writes result to a file
def encrypt(store_value):
    message, shift = store_value[1:]

    encrypt_message = ""
    for msg in message.upper():
        if msg.isalpha():
            adjusted_value = ord(msg) - 65 + shift
            if adjusted_value > 25:
                adjusted_value %= 26
            encrypt_message += chr(adjusted_value + 65)
        else:
            encrypt_message += msg
    write_message(encrypt_message)
    print("Encrypted message:", encrypt_message)
    

# the message decrypts using ceaser cipher and writes result to a file
def decrypt(store_value):
    message, shift = store_value[1:]

    decrypt_message = ""
    for msg in message.upper():
        if msg.isalpha():
            adjusted_value = ord(msg) - 65 - shift
            if adjusted_value < 0:
                adjusted_value %= 26
            decrypt_message += chr(adjusted_value + 65)
        else:
            decrypt_message += msg

    write_message(decrypt_message)
    print("Decrypted message:", decrypt_message)


#depending upon the mode, it reads the message from the given file and process either encrypts or decrypts
def process_file(filename, mode, shift):
    try:
        with open(filename, 'r') as f:
            msg = f.read()

        if mode == "e":
            encrypt_message = ""
            for m in msg:
                if m == " ":
                    encrypt_message += m
                else:
                    encrypt_message += chr(ord(m) + shift)
            write_message(encrypt_message)
            print("Encrypted message:", encrypt_message)
        elif mode == "d":
            decrypt_message = ""
            for m in msg:
                if m == " ":
                    decrypt_message += m
                else:
                    decrypt_message += chr(ord(m) - shift)
            write_message(decrypt_message)
            print("Decrypted message:", decrypt_message)

    except FileNotFoundError:
        print("File not found:", filename)


# Checks whether the given file exists or not
def is_file(filename):
    return os.path.isfile(filename)


# Writes the given message to a file named "result.txt"
def write_message(msg):
    try:
        with open("result.txt", 'w') as f:
            f.write(msg)
    except Exception as e:
        print(f"Error :{e}")



#this is the main function and tells user to choose whether to read the message from the console or the file and whether to encrypt or decrypt the message also
def message_or_file():
    welcome()

    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()

        if mode not in ('e', 'd'):
            print("Invalid mode.")
            continue

        while True:
            reading_mode = input("Would you like to read from a file (f) or the console (c)? ").lower()

            if reading_mode not in ('f', 'c'):
                print("Invalid reading mode.")
                continue

            shift = input("What is the shift number: ")

            try:
                shift = int(shift)
            except ValueError:
                print("Invalid shift number.")
                continue

            if reading_mode == 'f':
                filename = input("Enter a filename: ")
                if not is_file(filename):
                    print("File not found:", filename)
                    continue
                process_file(filename, mode, shift)
                break

            elif reading_mode == 'c':
                message =enter_message(mode)
                store_value = (mode, message, shift)
                if mode == "e":
                    encrypt(store_value)
                elif mode == "d":
                    decrypt(store_value)
                break
        another_message = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        if another_message == "n":
            print("Thanks for using the program, goodbye!")
            break


message_or_file()