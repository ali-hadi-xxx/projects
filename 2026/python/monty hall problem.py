import random 

door_with_prize = random.randint(1, 3)
door_chosen_by_player = random.randint(1, 3)
doors = [1, 2, 3]
door_opened_by_host = None
wins_when_switching = 0
trials = 100000
wins_when_staying = 0
for door in doors:
    if door != door_with_prize and door != door_chosen_by_player:
        door_opened_by_host = door
        break
for _ in range(trials):
   
    door_with_prize = random.randint(1, 3)
    door_chosen_by_player = random.randint(1, 3)
    for door in doors:
      if door != door_with_prize and door != door_chosen_by_player:
        door_opened_by_host = door
        break
   
    if door_chosen_by_player == door_with_prize:
        wins_when_staying += 1
    else:
        wins_when_switching += 1

print(f"Wins when staying: {wins_when_staying}")
print(f"Wins when switching: {wins_when_switching}")
