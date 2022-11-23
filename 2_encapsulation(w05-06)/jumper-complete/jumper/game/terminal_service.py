class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
     
    def get_letter(self, prompt):
        """Gets a text character input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text character.
        """
        return input(prompt)

    def read_letter(self, prompt):
        """Gets a text character input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            text character: The user's input as a string.
        """
        return prompt.lower()
        
    def write_letter(self, letter):
        """Displays the given text character on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(letter)

    def draw_parachute_man(self, parachute, man):
        for line in parachute:
            print(line)
        for line in man:
            print(line)