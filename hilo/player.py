
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

        ans = input("The next card will be higher or lower? l/h: " ).lower()
        
        print(f"Next card was {self.future_card}")
        
        if self.present_card < self.future_card:
            next_card = "h"
        elif self.present_card > self.future_card:
            next_card = "l"
        elif self.present_card == self.future_card:
            next_card = "equal"
        #print (ans, next_card)
        if ans == "h":
            result = True
        elif ans == "l":
            result = False
        else:
            result = None
        return result


    def count_points(self): 
        guess = self.guess()      
        if guess == True:
            self.total_points.append(100)
        elif guess == False:
            self.total_points.append(-75)
        elif guess == None:
            self.total_points.append(0)
        return sum(self.total_points)

