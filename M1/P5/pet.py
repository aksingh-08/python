def apply_rules(hunger, energy, mood):
    """Apply game rules: adjust mood based on stats and clamp values."""
    if hunger >= 8:
        mood -= 2
        print("Pet is very hungry!")

    if energy <= 2:
        mood -= 1
        print("Pet is too tired to play.")

    if hunger == 10:
        print("Pet is starving!")

    hunger = max(0, min(hunger, 10))
    energy = max(0, min(energy, 10))
    mood = max(0, min(mood, 10))
    
    return hunger, energy, mood


hunger = 5
energy = 5
mood = 5

while True:
    print("\nHunger:", hunger, "Energy:", energy, "Mood:", mood)
    print("1. Feed")
    print("2. Play")
    print("3. Rest")
    print("4. Exit")

    choice = input("Choose action: ")

    if choice == "1":
        hunger -= 2
        mood += 1
        print("You fed the pet.")

    elif choice == "2":
        energy -= 2
        mood += 2
        hunger += 1
        print("You played with the pet.")

    elif choice == "3":
        energy += 3
        hunger += 1
        print("The pet rested.")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
        continue

    hunger, energy, mood = apply_rules(hunger, energy, mood)