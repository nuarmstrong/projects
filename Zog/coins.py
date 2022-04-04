import random

def utility_print(b):
    print("Generated bags:")
    for key, val in b.items():
        stmnt = "{ " + str(key) + " : " + str(val) + " }"
        print(stmnt)
        stmnt = ""


def generate_bags():
    x = random.randrange(1, 11)
    bags = {}
    for i in range(1, 11):
        if (i == x):
            bags[i] = float(1.1)
            # bags["fake"] = x
        else: bags[i] = 1
    utility_print(bags)
    return bags 

def select_coins(b): 
    coins_to_weigh = []
    for i in range(1, 11):
        this_bag = []
        for j in range(0, i):
            this_bag.append(b[i])
        coins_to_weigh.append(this_bag)
    print(coins_to_weigh)
    return coins_to_weigh

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

