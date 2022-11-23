import random
# TODO: implement the dealer class as follows...

class Dealer:
    """
    Draws cards with different numbers randomly
    
    Attributes:
        card (int): the number represented by the card.
        points (int): The number of points the card is woth.
    """
    def __init__(self):
        """Constructs a new instance of dealer with a card number and the score.
        
        Args:
            self(dealer): An instance  of dealer.
        """
        self.current_card = ""
        self.next_card = ""
        self.score = 300
    
    def draw(self):
        """Generates a new random card and calculates the score
        
        Args:
            self(Dealer): An instance of Dealer.
        """
        self.current_card = random.randint(1, 13)
        return self.current_card


        # if self.current_card > self.next_card:
        #     self.score += 100
        # elif self.current_card < self.next_card:
        #     self.score -= 75

