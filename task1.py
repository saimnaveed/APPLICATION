initial_word='adding'
length=(len(initial_word))
if(length>3):
    for i in range (length):

      if initial_word[length-3:length]=='ing':
           final_word=initial_word+'ly'
      else:
           final_word=initial_word+'ing'
      break
else:
    final_word=initial_word
print(final_word)