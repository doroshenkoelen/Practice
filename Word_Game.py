VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

def load_words():

    wordlist = []
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):

    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq

def get_word_score(word, n):

    score_fc = 0

    word = str.lower(word)
    wordlen = len(word)

    if '*' in word:
        word = word.replace('*', '')
    for letter in word:
        score_fc += SCRABBLE_LETTER_VALUES[letter]
    score_sc = max(7 * wordlen - 3 * (n - wordlen), 1)

    return score_fc * score_sc

def display_hand(hand):

    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end = ' ')
    print()

def deal_hand(n):

    hand = {}
    num_vowels = int(math.ceil(n / 3)) - 1

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    hand['*'] = 1

    for i in range(num_vowels, n - 1):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand

def update_hand(hand, word):

    word = str.lower(word)
    word = get_frequency_dict(word)
    new_hand = {}

    for letter in hand.keys():
        if letter in word.keys():
            freq_remained = hand[letter] - word[letter]
            if freq_remained > 0:
                new_hand[letter] = new_hand.get(letter, freq_remained)
        else:
            new_hand[letter] = hand[letter]

    return new_hand

def is_valid_word(word, hand, word_list):

    word = str.lower(word)
    word_freq = get_frequency_dict(word)
    valid_word = []

    for letter in word_freq.keys():
        valid_word.append(letter in hand.keys() and hand[letter] >= word_freq[letter])
    if False not in valid_word:
        if word in word_list:
            return True
        elif '*' in word:
            for vowel in VOWELS:
                possible_word = word.replace('*', vowel)
                if possible_word in word_list:
                    return True
    else:
        return False

def calculate_handlen(hand):

    return sum(hand.values())

def play_hand(hand, word_list):

    total_score = 0
    while calculate_handlen(hand) > 0:

        print('\nCurrent Hand: '), display_hand(hand)
        word = input('Please enter a word or '"!!"' to indicate you are done: ')
        word = str.lower(word)

        if word == '!!':
            print('Total score for this hand:', total_score, 'points')
            break
        elif is_valid_word(word, hand, word_list):
            word_score = get_word_score(word, calculate_handlen(hand))
            total_score += word_score
            print('"' + word + '"', 'earned', word_score, 'points. Total:', total_score, 'points')
        else:
            print('That is not a valid word. Please choose another word.')
        hand = update_hand(hand, word)
        if calculate_handlen(hand) == 0:
            print('\nRan out of letters.', '\nTotal score for this hand:', total_score, 'points')

    return total_score

def substitute_hand(hand, letter):

    letter = str.lower(letter)
    substitute_letter = letter

    while substitute_letter in hand:
        if letter == '*':
            return hand
            break

        LETTERS = VOWELS + CONSONANTS
        substitute_letter = random.choice(LETTERS)

    hand[substitute_letter] = hand.get(letter, 0)
    del (hand[letter])

    return hand


def play_game(word_list):

    n = int(input('Enter hand size: '))
    number_of_hands = int(input('Enter total number of hands: '))
    total_game_score = 0
    substitute_letter_used = 0
    replay_hand_used = 0
    replay_hand = 0
    substitute_letter = 0

    for i in range(number_of_hands):
        hand = deal_hand(n)

        if substitute_letter_used == 0:
            print('Current Hand: '), display_hand(hand)
            substitute_letter = input('Would you like to substitute a letter? ')
            substitute_letter = str.lower(substitute_letter)
            if substitute_letter in 'yes':
                substitute_letter_used += 1
                letter = input('Which letter would you like to replace: ')
                letter = str.lower(letter)
                hand = substitute_hand(hand, letter)
        hand_score = play_hand(hand, word_list)
        print('----------')

        if replay_hand_used == 0:
            replay_hand = input('Would you like to replay the hand? ')
            replay_hand = str.lower(replay_hand)
            if replay_hand in 'yes':
                replay_hand_used += 1
                replay_hand_score = play_hand(hand, word_list)
                hand_score = max(hand_score, replay_hand_score)
        total_game_score += hand_score

        if i == number_of_hands - 1:
            print('Total score over all hands:', total_game_score)

    return total_game_score

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)