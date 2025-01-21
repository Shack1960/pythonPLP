class Laptop:
    def __init__(self, brand, model, processor, ram, storage):
        self.brand = brand
        self.model = model
        self.processor = processor
        self.ram = ram
        self.storage = storage

    def display_info(self):
        return f"{self.brand} {self.model} with {self.processor}, {self.ram}GB RAM, and {self.storage}GB storage."

    def browse(self, website):
        return f"Browsing {website} on {self.model}."

class GamingLaptop(Laptop):
    def __init__(self, brand, model, processor, ram, storage, gpu, cooling_system):
        super().__init__(brand, model, processor, ram, storage)
        self.gpu = gpu
        self.cooling_system = cooling_system

    def start_game(self, game):
        return f"Launching {game} on {self.model} with {self.gpu} and {self.cooling_system} cooling system."

# Example usage
laptop = Laptop("Dell", "Inspiron 15", "Intel i5", 8, 512)
gaming_laptop = GamingLaptop("Alienware", "M15 R7", "Intel i9", 32, 1000, "NVIDIA RTX 3080", "Advanced Vapor Chamber")

print(laptop.display_info())
print(laptop.browse("openai.com"))
print(gaming_laptop.display_info())
print(gaming_laptop.start_game("Cyberpunk 2077"))
