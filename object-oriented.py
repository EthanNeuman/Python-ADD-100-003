class Pet:
    def __init__(self, kind, breed, name):
        self._kind = kind
        self._breed = breed
        self._name = name

    def get_kind(self):
        return self._kind

    def get_breed(self):
        return self._breed

    def get_name(self):
        return self._name

    def set_kind(self, kind):
        self._kind = kind

    def set_breed(self, breed):
        self._breed = breed

    def set_name(self, name):
        self._name = name

    def print_details(self):
        print(
            f"Pet Info: {self.get_name()} is a {self.get_breed()} {self.get_kind()}.")


pet1 = Pet("Dog", "Labradoodle", "Bandit")
pet2 = Pet("Dog", "Lab", "Diesel")
pet3 = Pet("Dog", "Labradoodle", "Duke")

for pet in (pet1, pet2, pet3):
    pet.print_details()


print(f"Class name: {Pet.__name__}")

print(f"Type of pet2: {type(pet2)}")

print(f"Defined in module: {Pet.__module__}")

print(f"pet3's breed : {getattr(pet3, '_breed')}")

print(f"Is pet1 a Pet? {isinstance(pet1, Pet)}")
