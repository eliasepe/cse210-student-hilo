import random

default = 300
class Player:
    
    present_card = 0
    future_card = 0
    def __init__(self, points=300):
        self.points = points 

    def draw(self):
        self.present_card = random.randint(1, 13)
        self.future_card = random.randint(1, 13)

    def guess(self):
        print(f"The card is {self.present_card}")

        ans = str(input("The next card will be higher or lower? H\L")).upper()
        
        print(f"Next card was {self.future_card}")
        
        if self.present_card <= self.future_card:
            next_card = "L"
        elif self.present_card >= self.future_card:
            next_card = "H"

        if ans.upper() == next_card:
            result = True
        elif ans.upper() != next_card:
            result = False
        return result

    



shared = Player()
david = Player()

print(shared.points)

"""
print(shared.present_card)


print(david.future_card)

shared.draw()
print(shared.present_card)
print(shared.future_card)
"""
shared.draw()
shared.guess()