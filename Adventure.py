# Define the rooms and their descriptions
rooms = {
    'Entrance': {
        'description': 'You are at the entrance of a mysterious house.',
        'exits': {'north': 'Hallway'}
    },
    'Hallway': {
        'description': 'A long hallway with doors on either side.',
        'exits': {'south': 'Entrance', 'east': 'Kitchen', 'west': 'Bedroom'},
        'objects': ['key']
    },
    'Kitchen': {
        'description': 'A kitchen with old appliances and a strange smell.',
        'exits': {'west': 'Hallway'}
    },
    'Bedroom': {
        'description': 'A dusty bedroom with a bed and a small chest.',
        'exits': {'east': 'Hallway'},
        'objects': ['treasure']
    }
}

# Define the player's starting position and inventory
player = {
    'location': 'Entrance',
    'inventory': []
}

def move(direction):
    current_room = player['location']
    if direction in rooms[current_room]['exits']:
        player['location'] = rooms[current_room]['exits'][direction]
        print(f"You move {direction} to the {player['location']}.")
    else:
        print("You can't go that way.")

def inspect():
    current_room = player['location']
    print(rooms[current_room]['description'])
    if 'objects' in rooms[current_room] and rooms[current_room]['objects']:
        print(f"You see the following objects: {', '.join(rooms[current_room]['objects'])}")
    else:
        print("There is nothing special here.")

def take(item):
    current_room = player['location']
    if 'objects' in rooms[current_room] and item in rooms[current_room]['objects']:
        rooms[current_room]['objects'].remove(item)
        player['inventory'].append(item)
        print(f"You take the {item}.")
    else:
        print(f"There is no {item} here.")

def main():
    print("Welcome to the Adventure Game!")
    inspect()
    
    while True:
        command = input("> ").lower().split()
        if len(command) == 0:
            continue
        
        action = command[0]
        if action == 'move' and len(command) > 1:
            move(command[1])
        elif action == 'inspect':
            inspect()
        elif action == 'take' and len(command) > 1:
            take(command[1])
        elif action == 'inventory':
            print(f"You are carrying: {', '.join(player['inventory'])}")
        elif action == 'quit':
            print("Thanks for playing!")
            break
        else:
            print("Invalid command. Try 'move', 'inspect', 'take', 'inventory', or 'quit'.")

if __name__ == "__main__":
    main()
