import random


class Player:
    
    present_card = 0
    future_card = 0
    

    def __init__(self):
        pass

    def draw(self):
        self.present_card = random.randint(1, 13)
        self.future_card = random.randint(1, 13)

    def guess(self):
        print(f"The card is {self.present_card}")

        ans = input("The next card will be higher or lower? l/h: " )
        
        print(f"Next card was {self.future_card}")
        
        if self.present_card <= self.future_card:
            next_card = "h"
        elif self.present_card >= self.future_card:
            next_card = "l"
        print (ans, next_card)
        if ans == next_card:
            result = True
        elif ans != next_card:
            result = False
        return result

    def count_points(self):
        total_points = [300]
        if Player.guess(self) == True:
            total_points.append(100)
        elif Player.guess(self) == False:
            total_points.append(-75)
        return sum(total_points)
        

shared = Player()

"""
print(shared.present_card)


print(david.future_card)

shared.draw()
print(shared.present_card)
print(shared.future_card)
"""
shared.draw()


print(shared.guess())
print(Player.count_points(shared))


