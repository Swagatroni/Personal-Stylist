# This is an app that will allow you to input your wardrobe and generate outfits for the day.
import random

# Function to import database
def import_closet(file_path):
    # This function will import the wardrobe database from a file
    with open(file_path, 'r') as file:
        wardrobe = file.readlines()
    return [item.strip() for item in wardrobe]

# Function to generate outfit
def generate_outfit(wardrobe):
    # This function will generate a random outfit from the wardrobe
    top = random.choice([item for item in wardrobe if 'top' in item])
    bottom = random.choice([item for item in wardrobe if 'bottom' in item])
    shoes = random.choice([item for item in wardrobe if 'shoes' in item])
    return top, bottom, shoes

# Function to display outfit
def display_outfit(outfit):
    # This function will display the generated outfit
    top, bottom, shoes = outfit
    print(f"Today's outfit:\nTop: {top}\nBottom: {bottom}\nShoes: {shoes}")


# Example usage
if __name__ == "__main__":
    wardrobe = import_closet('wardrobe.txt')
    outfit = generate_outfit(wardrobe)
    display_outfit(outfit)
