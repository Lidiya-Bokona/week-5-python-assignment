class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life
    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}... 📞")
    def take_photo(self):
        print(f"Taking a photo with {self.brand} {self.model}... 📸")
my_phone = Smartphone("Apple", "iPhone 14", "20 hours")
print(my_phone.brand)
my_phone.make_call("123-456-7890")
my_phone.take_photo()
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery_life, game_mode):
        super().__init__(brand, model, battery_life)
        self.game_mode = game_mode
    def play_game(self):
        print(f"Playing in {self.game_mode} mode on {self.brand} {self.model}... 🎮")
my_gaming_phone = GamingSmartphone("Asus", "ROG Phone 5", "18 hours", "High Performance")
my_gaming_phone.play_game()