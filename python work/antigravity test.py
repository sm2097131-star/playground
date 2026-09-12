def encode_message():
    message = input("Enter Your Message: ")
    words = message.split(" ")
    encoded_words = []
    
    for word in words:
        if len(word) >= 3:
            # Move first letter to the end, then wrap with 'xyz' and 'abc'
            new_word = "xyz" + word[1:] + word[0] + "abc"
            encoded_words.append(new_word)
        else:
            # Reverse the word
            encoded_words.append(word[::-1])
            
    return " ".join(encoded_words)

def decode_message(encoded_message):
    words = encoded_message.split(" ")
    decoded_words = []
    
    for word in words:
        if len(word) >= 3:
            # Strip the 3 leading (xyz) and 3 trailing (abc) characters
            core = word[3:-3]
            # Move the last letter back to the start
            new_word = core[-1] + core[:-1]
            decoded_words.append(new_word)
        else:
            # Reverse the word back
            decoded_words.append(word[::-1])
            
    return " ".join(decoded_words)

# Main driver code
j = encode_message()
k = decode_message(j)
print('CODE:', j)

consent = input("Enter yes to decode the message: ")
if consent.lower() == 'yes':
    print('Message:', k)