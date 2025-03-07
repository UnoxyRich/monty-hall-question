import random

def monty_hall(num_trials, switch=True):
    wins = 0

    for _ in range(num_trials):

#0 contains goat, and 1 contains prize        
        doors = [0, 0, 0]  
        car_position = random.randint(0, 2)  
        doors[car_position] = 1  

        initial_choice = random.randint(0, 2)

        possible_doors_to_open = [i for i in range(3) if i != initial_choice and doors[i] == 0]
        host_opens = random.choice(possible_doors_to_open)
        
        if switch:
            remaining_doors = [i for i in range(3) if i != initial_choice and i != host_opens]
            final_choice = remaining_doors[0]
        else:
            final_choice = initial_choice
        
        if doors[final_choice] == 1:
            wins += 1

    win_percentage = (wins / num_trials) * 100
    return win_percentage


num_trials = 100000

switch_win_percentage = monty_hall(num_trials, switch=True)
print(f"Win percentage when switching: {switch_win_percentage:.2f}%")

stay_win_percentage = monty_hall(num_trials, switch=False)
print(f"Win percentage when staying: {stay_win_percentage:.2f}%")
