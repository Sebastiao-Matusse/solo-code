class BestScore():
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        self._best_score = self.get_best_score()
        self._points = 200
        self.write_values()

    def get_best_score(self):
        file = open("snake/high_scores.txt", "r")
        read_file = file.readlines()
        file.close
        self._best_score = int(read_file[0])
        
        return self._best_score

    def set_best_score(self):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self.set_text(f"Last best Score: {self._best_score}")

    def write_values(self):
        if self._points > self._best_score:
            file = open("snake/high_scores.txt", "w")
            file.write(f"{self._points}")
            file.close()

from time import sleep
counter = 1
x = 5
y = 0

# if self._counter < 15:
#     self._counter += 1
# else:
#     self.counter = 1
#     self._time_passed += 1

import base64
string = None
with open("head.png", "rb") as image2string:
    string = base64.b64encode(image2string.read())
  
with open('encode.bin', "wb") as file:
    file.write(string)

print(string)
# file = open('encode.bin', 'rb')
# byte = file.read()
# file.close()
  
# decodeit = open('hello_level.jpeg', 'wb')
# decodeit.write(base64.b64decode((byte)))
# decodeit.close()