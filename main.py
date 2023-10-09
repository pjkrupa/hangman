from modules import HangmanGame
word_list = ['monitor', 'yellow', 'market', 'foster']       #list of possible words for the game
while True:
    y_n = input('Do you want to play a game? y/n    ')          #infinite loop to get the user to choose whether to play
    if y_n not in ['y', 'n']:
        print('Please enter either y or n.  ')
        continue
    elif y_n == 'n':
        raise SystemExit('goodbye.  ')                #closes the program if 'n'
    elif y_n == 'y':
        print('lets gooooo! ')
        break                                   #breaks the infinite loop if y, on to the next section

game = HangmanGame(word_list)                   #instantiates the HangmanGame class with the word_list as an argument


# this infinite loop is the game. every loop, it requests a letter, calls game.make_guess
# with the letter as the argument, and uses the game.letter_check variable to quickly get a
# yes/no on whether the letter is there. if no, print the "sorry, wrong" message, if yes, print the
# "yay, nice job!" message. then print the correct gallows based on the number wrong so far.
# lastly, it checks to see if user has guessed all letters ('you win!') or if six guesses have
# been made ('you lose!')
while True:
    letter_guess = input('guess a letter!   ')
    current_guess, word, letter_check = game.make_guess(letter_guess)
    if letter_check == -1:
        print('that letter is not in this word!')
    else:
        print('you got one!')
    print(game.gallows[game.counter]())
    print(current_guess)
    if '_' not in game.current_guess:
        print('congrats, you win!')
        break
    if game.counter == 6:
        print('sad trombone, you hung the dude.')
        print('the word was ' + game.word)
        break

print('thanks for playing!')








