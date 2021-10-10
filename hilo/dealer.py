from game.player import player

class dealer:
    def __init__(self):
        self.keep_playing = True
        self.score = 300
        self.player = player()

    def start_game(self):

        while self.keep_playing:
            self.get_inputs()
            "To see if the player wants to keep playing"
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        "Get the result of the drawn card"
        self.player.draw()

    def do_updates(self):
        "To update the score after the revelation of the drawn card"
        points = self.player.count_points()
        self.score += points
        return points


    def do_outputs(self):
        self.player.guess()
        print(f"Tour score is: {self.score}")
        if self.dealer.do_updates() > 0:
            choice = input("Draw again? [y/n]")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False
            print("You lost the game, try again")

        