class Dog:
    species = "Canis familiaris"
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def display_details(self):
        print("Dog Name:", self.name)
        print("Breed:", self.breed)
        print("Species:", Dog.species)
        print("-" * 25)
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")
dog1.display_details()
dog2.display_details()