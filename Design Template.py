class Dog:
    def walk (self):
        return "walking"
    def speak (self):
        print ("Woof!")

class JackRussellTerrier (Dog):
    def speak (self):
        return  super().walk() + " dog"

ciapek = JackRussellTerrier()
print(ciapek.speak())