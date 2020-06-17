import time, random


def pause(number):
    time.sleep(number)


def line(text):
    print(text)
    pause(1)

survivors = []
line("Island Survival Simulation.")
line("How many starting survivors do you want?")
starting_amount = int(input(">>> "))
for i in range(starting_amount):
    line(f"What is survivor {i}'s name?")
    name = input(">>> ")
    survivor = [name, 0, 10, 15, random.randint(1, 3), random.randint(1,3)] 
    #[name, age, energy, hunger, strength, intelligence]
    line(survivor)
    survivors.append(survivor)
tick = 0
day = 0

while True:
    line(f"Day: {day}")
    while tick <= 24:
        tick += 1
        for i in range(len(survivors)):
            survivors[i][3] -= 1
            if survivors[i][3] < 0:
                print(f"{survivors[i][0]} Died of starvation")
                del survivors[i]
                if i > 0:
                    i -= 1
            elif survivors[i][2] > 0:
                survivors[i][2] -= 1
                action = random.randint(0, 1)
                if action == 0:
                    print(f"{survivors[i][0]} slept")
                    survivors[i][2] += random.randint(2, 4)
                elif action == 1:
                    action = random.randint(0, 1)
                    if action == 0:
                        print(f"{survivors[i][0]} went hunting")
                        survivors[i][3] += random.randint(0, 3)
                        survivors[i][4] += random.randint(0, 3)
                    elif action == 1:
                        print(f"{survivors[i][0]} went foraging")
                        survivors[i][3] += random.randint(0, 3)
                        survivors[i][5] += random.randint(0, 3)
            else:
                print(f"{survivors[i][0]} slept")
                survivors[i][2] += random.randint(1,3)
    tick = 0
    day += 1
            