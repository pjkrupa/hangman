import random


class HangmanGame:
    def __init__(self, word_list):  #this class requires a list of words as an argument
        self.gallows = {            #these functions print out the gallows. each is stored as a function,
            0: self.zero_wrong,
            1: self.one_wrong,      #referenced by a dictionary value
            2: self.two_wrong,
            3: self.three_wrong,
            4: self.four_wrong,
            5: self.five_wrong,
            6: self.six_wrong
        }

        self.word_list = word_list                      #this section defines the mystery word and sets up
        self.word = random.choice(word_list)            #the blank word the user has to guess to fill in
        self.current_guess = '_' * len(self.word)
        self.counter = 0
        print('''       
                        _______                         
                        |     |
                        |
                        |
                        |
                        |
                ________|________
        ''')
        print(self.current_guess)

    def make_guess(self, letter_guess):
        new_guess = list(self.current_guess)
        word_as_list = list(self.word)
        letter_check = self.word.find(letter_guess)
        for index, letter in enumerate(word_as_list):
            if letter_guess == letter:
                new_guess[index] = letter_guess
                word_as_list[index] = '_'
        self.current_guess = ''.join(new_guess)
        self.word = ''.join(word_as_list)
        if letter_check == -1:
            self.counter += 1
        return self.current_guess, self.word, letter_check

    @staticmethod
    def zero_wrong():
        gallows = '''
                 _______                         
                 |     |
                 |     
                 |
                 |
                 |
         ________|________
         '''
        print(gallows)

    @staticmethod
    def one_wrong():
        gallows = '''
                        _______                         
                        |     |
                        |     0
                        |
                        |
                        |
                ________|________
        '''
        print(gallows)

    @staticmethod
    def two_wrong():
        gallows = '''   
                        _______                         
                        |     |
                        |     0
                        |    /
                        |
                        |
                ________|________
        '''
        return gallows

    @staticmethod
    def three_wrong():
        gallows = '''   
                        _______                         
                        |     |
                        |     0
                        |    / \
                        |
                        |
                ________|________
        '''
        return gallows

    @staticmethod
    def four_wrong():
        gallows ='''    
                        _______                         
                        |     |
                        |     0
                        |    / \\
                        |     |
                        |
                ________|________
        '''
        return gallows

    @staticmethod
    def five_wrong():
        gallows = '''   
                        _______                         
                        |     |
                        |     0
                        |    / \\
                        |     |
                        |    /
                ________|________
        '''
        return gallows

    @staticmethod
    def six_wrong():
        gallows = '''   
                        _______                         
                        |     |
                        |     0
                        |    / \\
                        |     |
                        |    / \\
                ________|________
        '''
        return gallows
