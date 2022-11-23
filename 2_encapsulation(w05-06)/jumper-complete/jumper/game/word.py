# TODO: Implement the Seeker class as follows...
import random
# 1) Add the class declaration. Use the following class comment.
class Word:
    """The list of words, randomly chosen. 
    
    The responsibility of a Seeker is to keep track of its location and distance travelled.
    
    Attributes:
        location (int): The location of the Seeker (1-1000).
    """
# 2) Create the class constructor. Use the following method comment.
    def __init__(self):
        """Constructs a new Seeker.

        Args:
            self (Seeker): An instance of Seeker.
        """
        self._words = ["computer", "object", "abstraction", "encapsulation, sebastian, matusse, deafault"]
        self._new_word = random.choice(self._words)
       
# 3) Create the get_location(self) method. Use the following method comment.
    def get_word(self):
        """Gets the current letter.
        
        Returns:
            text_character: The current letter,
        """
        return self._new_word

# 4) Create the move_location(self, location) method. Use the following method comment.
    def replace_letter(self, guess, display):
        """Replaces the empty space by correct guessed letter.

        Args:
            self (Seeker): An instance of Seeker.
            location (int): The given location.
        """
        i = 0
        if guess in self._new_word:
            while self._new_word.find(guess, i) != -1:
                i = self._new_word.find(guess, i)
                self._display = display[:i] + guess + display[i + 1:]
                i += 1
            return self._display
    
    def is_correct(self, guess):
                
        return self._new_word.find(guess)
        # if guess in word:
        #     while word.find(guess, i) != -1:   
        #         i = word.find(guess, i)
        #         display = display[:i] + guess + display[i + 1:]
        #         i +=1


        # if guess in self._new_word:
        #     while self._new_word.find(guess, i) != -1:   
        #         i = self._new_word.find(guess, i)
        #         self._display = self._display[:i] + guess + self._display[i + 1:]
        #         i += 1

