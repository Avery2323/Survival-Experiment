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
    survivor = [name, 0] #[name, energy]
    survivors.append(survivor)
tick = 0
day = 0

while True:
    line(f"Day: {day}")
    while tick <= 24:
        tick += 1
        for i in range(survivors):
            
    
