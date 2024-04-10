# Task 2 "Setting the Scene":

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        action = "cross a river"
        print("You found a boat!")


elif place == "cave":
    action = input("light a torch? ")
    if action == 'yes':
        print("The Torch Revealed Some Well Hidden Treasure!")
    else:
        action = 'no'
        print("Proceed in the Dark")