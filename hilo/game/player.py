import random


class Player:
    
    present_card = 0
    future_card = 0
    total_points = [300]

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
        #print (ans, next_card)
        if ans == next_card:
            result = True
        elif ans != next_card:
            result = False
        return result


    def count_points(self): 
        guess = self.guess()      
        if guess == True:
            self.total_points.append(100)
        elif guess == False:
            self.total_points.append(-75)
        return sum(self.total_points)
        

shared = Player()
david = Player()


shared.draw()

#print(shared.total_points)
print(shared.count_points())
#print(shared.total_points)


