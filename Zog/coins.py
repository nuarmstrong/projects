import random

## Just a printing function so see the contents of the bag
def utility_print(b):
    print("Generated bags:")
    for key, val in b.items():
        stmnt = "{ " + str(key) + " : " + str(val) + " }"
        print(stmnt)
        stmnt = ""

## Random bag generator that creates 10 bags ("1", "2", etc) with a coin weight of 1 or 1.1
## only 1 bag contains coins of weight 1.1g, the other 9 have 1g 
def generate_bags():
    x = random.randrange(1, 11)
    bags = {}
    for i in range(1, 11):
        if (i == x):
            bags[i] = float(1.1)
        else: bags[i] = 1
    utility_print(bags)
    return bags 

## coin selector alg that iterates over the bags and selects n coins from the nth bag
## where n is from 1...10. Eg: 1 coin from bag 1, 2 from bag "2", 3 from bag "3", etc
## Returns the list of coins to weigh
def select_coins(b): 
    coins_to_weigh = []
    for i in range(1, 11):
        this_bag = []
        for j in range(0, i):
            this_bag.append(b[i])
        coins_to_weigh.append(this_bag)
    print(coins_to_weigh)
    return coins_to_weigh

## Sums the weights in the passed list. If all coins were real (@ 1 g), then the total weight 
## should be 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55. Therefore, the  (sum - 55) * 10
## is the index of the bag with fake coins.
def weigh_and_determine(s):
    sum = float(0)
    for lst in s:
        for i in lst:
            sum += float(i)
    offset = sum - 55 
    offset *= 10
    print("Total Weight = " + str(sum) + " Bag " + str(offset)[:-2] + " contains fake coins.")


all_bags = generate_bags()
selected_coins = select_coins(all_bags)
weigh_and_determine(selected_coins)

