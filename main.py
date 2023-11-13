import count_and_track

animal_dict = {
    "chicken": count_and_track.Chicken(),
    "cow": count_and_track.Cow(),
    "goat": count_and_track.Goat(),
    "pig": count_and_track.Pig(),
    "sheep": count_and_track.Sheep(),
}

animal = input("What kind of animal do you want to detect? ")

if animal.lower() in animal_dict:
    animal_dict[animal.lower()].main()
else:
    print(f"Support for {animal} is not yet added.")
