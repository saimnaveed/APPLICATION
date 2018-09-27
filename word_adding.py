def word_addition():
    """adds ly or ing at he end of word if wordsize is bigger than three """
    initial_word='addora'
    length=(len(initial_word))
    if(length>3):
        for i in range (length):

            if initial_word[length-3:length]=='ing':
                final_word=initial_word+'ly'
            else:
               final_word=initial_word+'ing'

    else:
        final_word=initial_word
    print(final_word)
    return
word_addition()