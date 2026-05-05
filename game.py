# Codédex Checkpoint Project: Terminal Adventure Game
# Theme: The Lost Tara

print("== WELCOME TO THE LOST Tara ==")
print("You are Captain Obreoi , piloting the 'The Vikrant'.")
print("Your mission: Find the Ancient Star Core before your fuel runs out.")
print("-----------------------------------")

# Initializing variables
fuel = 3
has_artifact = False
game_running = True

while game_running:
    print(f"\nStatus: {fuel} fuel units remaining.")
    
    # Choice 1: Navigation
    choice = input("Do you steer toward the (1) Distant Planet or (2) Glowing tara? ")

    if choice == "1":
        print("\nYou land on a rocky planet. An alien offer you fuel in exchange for a song.")
        action = input("Do you (A) Sing a song or (B) Refuse and leave? ").upper()
        
        if action == "A":
            print("The alien loved it! You gained 2 fuel units.")
            fuel += 2
        else:
            print("You left empty-handed and wasted fuel.")
            fuel -= 1

    elif choice == "2":
        print("\nYou fly into the tara and find a hidden temple!")
        action = input("Do you (A) Enter the temple or (B) Scan from afar? ").upper()
        
        if action == "A":
            print("Success! You found the Ancient Star Core!")
            has_artifact = True
            game_running = False # Win condition
        else:
            print("The scan revealed nothing, and the tara's radiation drained your fuel.")
            fuel -= 2
    else:
        print("Invalid command. You drift aimlessly...")
        fuel -= 1

    # Check for Lose Condition
    if fuel <= 0:
        print("\n--- GAME OVER ---")
        print("Your ship has run out of fuel. You are drifting in space forever.")
        game_running = False

# Ending Message
if has_artifact:
    print("\n--- VICTORY ---")
    print("You return home as a hero with the Ancient Star Core!")