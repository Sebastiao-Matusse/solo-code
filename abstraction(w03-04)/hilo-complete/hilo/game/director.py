from game.dealer import Dealer

class Director:
    """A person who directs the game.
    The responsability of a Director is to control the sequence of play.

    Attributes:
        current_card (int): the card number being displayed.
        is_playing (boolean): whether or not the game is being played.
        score(int): the score for one round after adding or reducing points to the total score.
    """

    def __init__(self):
        """Construts a new Director
        
        Args:
            self(Director): an instance of Director.
        """
        self.dealer = Dealer()
        self.current_card = self.dealer.draw()
        self.next_card = self.dealer.draw()
        self.is_playing = True
        self.score = self.dealer.score

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
    
    def get_inputs(self):
        """Asks the user if the next card will be higher or lower.

        Args:
            self (Director): An instance of Director.
        """
        print(f"The card is:{self.current_card}")
        self.card = input("Higher or Lower (h/l)? ")

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        if self.card == "l" and self.current_card > self.next_card:
            self.score += 100
        elif self.card == "l" and self.current_card < self.next_card:
            self.score -= 75
        elif self.card == "h" and self.current_card < self.next_card:
            self.score += 100
        elif self.card == "h" and self.current_card > self.next_card:
            self.score -= 75

        self.current_card = self.dealer.draw()

    def do_outputs(self):
        """Displays the current card. Also asks the player if they want to play again.
        
        Args:
            self(Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        print(f"The next card was {self.next_card}")
        print(f"Your score is {self.score}")
        prompt = input("Play again? [y/n] ")
        self.is_playing = (prompt == "y")
        print()
