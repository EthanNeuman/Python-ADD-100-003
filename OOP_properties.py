class Pet:
    vet_name = "Vet Stop"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    def get_owner_first_name(self):
        return self.__owner_first_name

    def set_owner_first_name(self, name):
        self.__owner_first_name = name

    def get_owner_last_name(self):
        return self.__owner_last_name

    def set_owner_last_name(self, name):
        self.__owner_last_name = name

    def get_pet_id(self):
        return self.__pet_id

    def set_pet_id(self, pet_id):
        self.__pet_id = pet_id

    def get_pet_name(self):
        return self.__pet_name

    def set_pet_name(self, pet_name):
        self.__pet_name = pet_name

    def get_pet_type(self):
        return self.__pet_type

    def set_pet_type(self, pet_type):
        self.__pet_type = pet_type

    def display_pet_info(self):
        print(f"Owner: {self.__owner_first_name} {self.__owner_last_name}")
        print(f"Pet ID: {self.__pet_id}")
        print(f"Pet Name: {self.__pet_name}")
        print(f"Pet Type: {self.__pet_type}")
        print(f"Veterinary Clinic: {Pet.vet_name}")
        print("-" * 40)


def check_property(pet_object, property_name):
    return hasattr(pet_object, property_name)


def main():
    pet1 = Pet("Ethan", "Neuman", "01", "Bandit", "Dog")
    pet2 = Pet("Jacquelyn", "Worthem", "02", "Duke", "Dog")
    pet3 = Pet("Jim", "Neuman", "03", "Harlee", "Dog")

    pet1.set_pet_name("Bandit")
    pet1.display_pet_info()
    pet2.display_pet_info()
    pet3.display_pet_info()

    print("Property '_Pet__pet_name' exists in pet1:",
          check_property(pet1, "_Pet__pet_name"))
    print("Property '_Pet__birthday' exists in pet2:",
          check_property(pet2, "_Pet__birthday"))
    print("Property '_Pet__owner_last_name' exists in pet3:",
          check_property(pet3, "_Pet__owner_last_name"))


main()
