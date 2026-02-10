while True:
    user_word = input("Enter a word with 'h' or 'H': ")

    if 'h' in user_word.lower():
        print("Great job!")
        break

    print("There is no 'h' here. Try again!")