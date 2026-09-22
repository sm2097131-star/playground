def encode_message():

  word1 = input("Enter Your Message:").split(" ")
  final_word = []
  for word in word1:
    lst = list(word)
    if (len(word) >= 3):

      b = word[0]
      lst.pop(0)
      lst.append(b)
      lst.append('abc')
      lst.insert(0, 'xyz')

    else:
      lst.reverse()

    joined_word = "".join(lst)
    final_word.append(joined_word)
  final_output = " ".join(final_word)
  return final_output


def decode_message(encoded_message):
  
  final_word2 = []
  lst3 = encoded_message.split(" ")

  for word2 in lst3:
    lst2 = list(word2)

    if (len(word2) >= 3):
      core_chars = lst2[3:-3]
      last_char = core_chars.pop(-1)
      core_chars.insert(0, last_char)
      joined_words1 = "".join(core_chars)
      final_word2.append(joined_words1)

    else:
      lst2.reverse()
      joined_words = "".join(lst2)
      final_word2.append(joined_words)
  final_output2 = " ".join(final_word2)
  return final_output2

j=encode_message()
k=decode_message(j)
print('CODE:',j)
consent=input("Enter yes to decode the message:")
small=consent.lower()
if small=='yes':
  print('Message:',k)