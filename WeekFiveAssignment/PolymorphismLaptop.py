class Laptop:
    def use(self):
        raise NotImplementedError("Subclass must implement abstract method.")

class Ultrabook(Laptop):
    def use(self):
        return "Lightweight and portable, perfect for travel and office work."

class Workstation(Laptop):
    def use(self):
        return "Optimized for heavy tasks like video editing and 3D rendering."

class GamingLaptop(Laptop):
    def use(self):
        return "Powerful for gaming, with high-end GPU and cooling."

# Example usage
laptops = [Ultrabook(), Workstation(), GamingLaptop()]

for laptop in laptops:
    print(laptop.use())
