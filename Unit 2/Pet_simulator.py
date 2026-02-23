import threading
import time
import random


stats = {
    "energy": 50,
    "hunger": 50,
    "happiness": 50,
    "oxygen":100,
    "fire":0

}

def found_food():
    print(" Your pet found food! Hunger decreases.")
    stats['hunger'] += 10

def got_sick():
    print(" Your pet got sick! Energy decreases.")
    stats['energy'] -= 10

def played_outside():
    print(" Your pet played outside! Happiness increases.")

def oxygen_leak():
    print(" Oxygen leakage detected! ")
    stats['oxygen'] -= 50

def fire_ship():
    print(" Fire on the ship! Emergency situation!")
    stats['fire'] += 1

def watched_movie():
    print(" Your pet watched a movie! Happiness increases.")
    stats['happiness'] += 20

def got_poisoned():
    print(" Your pet got poisoned .")
    stats['hunger']-=50
    

def rain_started():
    print(" It started raining. ")


events= {
    "Found food": found_food,
    "Got sick": got_sick,
    "Played outside": played_outside,
    "Oxygen Leakage": oxygen_leak,
    "Fire on the ship": fire_ship,
    "Watched a movie": watched_movie,
    "Got poisoned": got_poisoned,
    "Rain started": rain_started
}




def passive_decay():
    while True:
        time.sleep(1)
        stats['hunger'] += 1
        stats['energy'] -= 1
        stats['happiness'] -= 1
        stats['oxygen'] -= 1

thread = threading.Thread(target=passive_decay, daemon=True)
thread.start()

action_history = []
if len(action_history)>5:
    action_history.pop(0)

def show_status():
    print(f"\n--- STATUS ---")
    print(f"Energy: {stats['energy']}")
    print(f"Hunger: {stats['hunger']}")
    print(f"Happiness: {stats['happiness']}")
    # ... etc

def feed_creature():
    print("You feed the creature...")
    stats['hunger'] -= 10 # This is how we access and modify the stats dictionary, stats is a dictionary, and we can access its values using keys like 'hunger' and 'energy'
    stats['energy'] += 5
    action_history.append("Fed creature")

def reversefeed_creature():
    stats['hunger'] += 10 # This is how we access and modify the stats dictionary, stats is a dictionary, and we can access its values using keys like 'hunger' and 'energy'
    stats['energy'] -= 5
    
def sleep_pet():
    print("Your pet is sleeping")
    stats['hunger'] += 20 # This is how we access and modify the stats dictionary, stats is a dictionary, and we can access its values using keys like 'hunger' and 'energy'
    stats['energy'] += 15
    stats['happiness'] += 30
    action_history.append("Creature slept")

def reversesleep_pet():
    stats['hunger'] -= 20 # This is how we access and modify the stats dictionary, stats is a dictionary, and we can access its values using keys like 'hunger' and 'energy'
    stats['energy'] -= 15
    stats['happiness'] -= 30
    
def history_view():
    if len(action_history)!=0:
        print("History is here:\n" )
        if len(action_history)==5:
            action_history.pop(0)
        elif  len(action_history)>5:
            nom=len(action_history)-5
            for i in range(1,nom):
                action_history.pop(0)
        else:
            pass
        for i in action_history:
            print(i)
        reve_fu=input("Do you want to reverse your last action?(y/n)")
        last_act=action_history[-1]
        if reve_fu=="y":
            action_history.pop()
            if last_act=="Fed creature":
                reversefeed_creature()
                action_history.append("Viewed history")
            elif last_act=="Creature slept":
                reversesleep_pet()
                action_history.append("Viewed history")
            print(f"last action {last_act} has been reversed")
        elif reve_fu=="n":
            print("last action {last_act} was not reversed")
            action_history.append("Viewed history")
        else:
            print("invalid answer, run choice 3 again")
            action_history.append("Viewed history")
    else:
        print("history is empty")
    



# 2. Main Game Loop
while True:
    if random.randint(1, 10) == 1:
        print("A random event is going to occur now!!!!")
        name, event = random.choice(list(events.items()))
        event()

    show_status()
    print("1. Feed")
    print("2. Sleep")
    print("3. View History")
    print("4. Quit")
    
    
    choice = input("Choose an action: ")
    turn+=1

    
    # 3. Logic
    if choice =="1":
        feed_creature()
    elif choice =="2":
        sleep_pet()
    elif choice =="3":
        history_view()# Print action_history using a loop, unless you want to implement undo functionality, in which case you can pop from the list and reverse the effects of the last action
         # These are placeholders for you to implement actions you want to add---pass
    elif choice =="4":
        print("quitting.....")
        break
    else:
        print("Choose a number 1-4")
            
    # 4. Game Over check
    if stats['hunger'] >= 100:
        print("Your creature starved! Game Over.")
        stats['hunger']=50
        break

    for category in stats:
        if stats[category] >= 100 and category!='hunger':
            stats[category]=100
        elif stats[category]<0 :
            stats[category]=0
        else:
            pass
        
