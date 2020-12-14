import random
import string

words_list = "words.txt"

# Loading word list from file:
def load_words():
    print("Loading word list from file...")
    inFile = open(words_list, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

# Choosing a random word from the words_list:
choose_word = lambda wordlist: random.choice(wordlist)

# Downloading a words file into wordlist:
wordlist = load_words()

# Determining the guessed letter of the word:
def is_word_guessed(secret_word, letters_guessed):
    word_guessed = []
    for letter in secret_word:
        word_guessed.append(letter in letters_guessed)
    if False in word_guessed:
        word_guessed = False
    else:
        word_guessed = True
    return word_guessed

# Definition of guessed letters:
def get_guessed_word(secret_word, letters_guessed):
    guessed_word = list(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] not in letters_guessed:
            guessed_word[i] = '_ '
    guessed_word = ''.join(guessed_word)
    return guessed_word


# Definition of available letters:
def get_available_letters(letters_guessed):

    available_letters = list(string.ascii_lowercase)
    for letter in string.ascii_lowercase:
        if letter in letters_guessed:
            available_letters.remove(letter)
    available_letters = ''.join(available_letters)

    return available_letters

def hangman(secret_word):
    warnings_remaining = 3
    guesses_remaining = 6

    vowels = 'aeiou'
    letters_guessed = []
    unique_letters = []

    print('Welcome to the game Hangman! \n \n' + 'I am thinking of a word that is \n', len(secret_word), 'letters long. \n')
    print('You have', warnings_remaining, 'warnings left. \n', '-------------', '\n You have', guesses_remaining, 'guesses left. \n', 'Available letters:', get_available_letters(letters_guessed))

    for letter in secret_word:
        if letter not in unique_letters:
            unique_letters.append(letter)
    number_unique_letters = len(unique_letters)

    word_guessed = is_word_guessed(secret_word, letters_guessed)

    while guesses_remaining > 0 and word_guessed == False:
        char = input('Please guess a letter: ')

        if str.isalpha(char) == False or char in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                if char in letters_guessed:
                    print("Oops! You've already guessed that letter. ", 'You have', warnings_remaining, 'warnings left:', get_guessed_word(secret_word, letters_guessed))
                else:
                    print('Oops! That is not a valid letter. ', 'You have', warnings_remaining, 'warnings left:', get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                if char in letters_guessed:
                    print("Oops! You've already guessed that letter. ", 'You have no warnings left so you lose ', 'one guess:', get_guessed_word(secret_word, letters_guessed))
                else:
                    print('Oops! That is not a valid letter. ', 'You have no warnings leftso you lose ','one guess:', get_guessed_word(secret_word, letters_guessed))

        else:
            letter = str.lower(char)
            letters_guessed.append(letter)

            if letter in secret_word:
                print('Good guess:', get_guessed_word(secret_word, letters_guessed))
            elif letter in vowels and guesses_remaining > 1:
                guesses_remaining -= 2
                print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))

        word_guessed = is_word_guessed(secret_word, letters_guessed)

        if word_guessed == False and guesses_remaining > 0:
            print('-------------', '\n', 'You have', guesses_remaining, 'guesses left.', '\n', 'Available letters:', get_available_letters(letters_guessed))
        elif guesses_remaining == 0:
            print('-------------', '\n', 'Sorry, you ran out of guesses. The word was', str(secret_word) + '.')
        else:
            total_score = guesses_remaining * number_unique_letters
            print('-------------', '\n', 'Congratulations, you won!', '\n', 'Your total score for this game is:', total_score)

# Finding matches with gaps:
def match_with_gaps(my_word, other_word):
    match_letters = []
    match_result = []
    matched = False
    my_word = my_word.replace(' ', '')

    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            char = my_word[i]
            if str.isalpha(char) == True:
                match_result.append(char == other_word[i])
                if char == other_word[i]:
                    match_letters.append(other_word[i])

        for i in range(len(my_word)):
            char = my_word[i]
            if str.isalpha(char) == False:
                match_result.append(other_word[i] not in match_letters)

        if False not in match_result:
            matched = True

    return matched

# Finding matches:
def show_possible_matches(my_word):
    possible_matches = str()
    for word in wordlist:
        if match_with_gaps(my_word, word) == True:
            possible_matches += word + ' '

    if possible_matches == '':
        print('No matches found')
    else:
        return possible_matches

# Hangman game function:
def hangman_with_hints(secret_word):
    warnings_remaining = 3
    guesses_remaining = 6

    vowels = ['a', 'e', 'i', 'o', 'u']
    letters_guessed = []
    unique_letters = []

    print('Welcome to the game Hangman!', '\n' + 'I am thinking of a word that is', len(secret_word), 'letters long.\n', 'You have', warnings_remaining, 'warnings left.\n', '-------------')
    print('\n You have', guesses_remaining, 'guesses left.', '\n Available letters:', get_available_letters(letters_guessed))

    for letter in secret_word:
        if letter not in unique_letters:
            unique_letters.append(letter)
    number_unique_letters = len(unique_letters)

    word_guessed = is_word_guessed(secret_word, letters_guessed)

    while guesses_remaining > 0 and word_guessed == False:
        char = input('Please guess a letter: ')

        if char != '*' and str.isalpha(char) == False or char in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                if char in letters_guessed:
                    print("Oops! You've already guessed that letter. You have", warnings_remaining, 'warnings left:', get_guessed_word(secret_word, letters_guessed))
                else:
                    print('Oops! That is not a valid letter. You have', warnings_remaining, 'warnings left:', get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                if char in letters_guessed:
                    print("Oops! You've already guessed that letter. \n You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                else:
                    print('Oops! That is not a valid letter. You have no warnings left so you lose one guess:', get_guessed_word(secret_word, letters_guessed))

        elif char == '*':
            print('Possible word matches are:\n' + show_possible_matches(get_guessed_word(secret_word, letters_guessed)))

        else:
            letter = str.lower(char)
            letters_guessed.append(letter)

            if letter in secret_word:
                print('Good guess:', get_guessed_word(secret_word, letters_guessed))
            elif letter in vowels and guesses_remaining > 1:
                guesses_remaining -= 2
                print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))

        word_guessed = is_word_guessed(secret_word, letters_guessed)

        if word_guessed == False and guesses_remaining > 0:
            print('-------------', '\n', 'You have', guesses_remaining,'guesses left.', '\n Available letters:', get_available_letters(letters_guessed))
        elif guesses_remaining == 0:
            print('-------------', '\n', 'Sorry, you ran out of guesses. The word was', str(secret_word), '.')
        else:
            total_score = guesses_remaining * number_unique_letters
            print('-------------', '\n', 'Congratulations, you won!', '\n', 'Your total score for this game is:', total_score)

if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
