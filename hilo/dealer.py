from player import Player


class dealer:
    def __init__(self):
        self.keep_playing = True
        #self.score = 300
        self.player = Player()
        self.start_game()

    def start_game(self):

        while self.keep_playing:
            self.get_inputs()
            "To see if the player wants to keep playing"
            #self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        "Get the result of the drawn card"
        self.player.draw()


    def do_outputs(self):

        result = self.player.count_points()

        print(f"Your actual score is {result}")

        if result > 0:
            choice = input("Draw again? [y/n]: ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False
            print("You lost the game, try again")


