# song lyrics for House of Rising Suns by Five Finger Death Punch
def custom_song(place, profession, emotion, object1, object2, name1, name2, verb):
    print("\n\n")
    print(f"There is a house in {place},")
    print(f"They call the {object1} {object2},")
    print(f"And it's been the ruin of many a poor {profession},")
    print(f"And God, I know I'm {emotion}.")
    print()
    print(f"My {name1} was a tailor,")
    print(f"She sewed my new blue jeans.")
    print(f"My {name2} was a gamblin' {profession},")
    print(f"Down in {place} he {verb} away.")


#  get the user input
place = input("Enter a place: ")
profession = input("Enter a profession: ")
emotion = input("Enter an emotion: ")
object1 = input("Enter an object: ")
object2 = input("Enter another object: ")
name1 = input("Enter a person's name: ")
name2 = input("Enter another person's name: ")
verb = input("Enter a verb: ")

# function with user input
custom_song(
    place=place,
    profession=profession,
    emotion=emotion,
    object1=object1,
    object2=object2,
    name1=name1,
    name2=name2,
    verb=verb
)
