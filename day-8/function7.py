alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt (text, shift):
#     cipher_text = ""
#     for each_letter in text:
#         x = alphabet.index(each_letter)
#         x += shift
#         newx = alphabet[x]
#         cipher_text += str(newx)
#     print(f"The encoded text is: {cipher_text}")

# def decrypt (text, shift):
#     cipher_text = ""
#     for each_letter in text:
#         x = alphabet.index(each_letter)
#         x -= shift
#         newx = alphabet[x]
#         cipher_text += str(newx)
#     print(f"The decoded text is: {cipher_text}")

def caesar (text, shift, direction):
    cipher_text = ""
    for each_letter in text:
        x = alphabet.index(each_letter)
        if direction == "encode":
            x += shift
        elif direction == "decode":
            x -= shift
        else:
            print(f"{direction} is not a valid input!")
            exit
        newx = alphabet[x]
        cipher_text += str(newx)
    print(f"The decoded text is: {cipher_text}")

    #-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# if direction == "encode":
#     encrypt(text, shift)
# if direction == "decode":
#     decrypt(text,shift)
caesar(text, shift, direction)