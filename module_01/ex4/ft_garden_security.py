class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height):
        if height < 0:
            print(
                f"Invalid operation attempted: height {height}cm [REJECTED]"
            )
            print("Security: Negative height rejected")
            return
        self.__height = height
        print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, age):
        if age < 0:
            print(f"Invalid operation attempted: age {age} [REJECTED]")
            print("Security: Negative age rejected")
            return
        self.__age = age
        print(f"Age updated: {self.__age} days [OK]")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def get_info(self):
        print(
            f"Current plant: {self.name} ({self.get_height()}cm, "
            f"{self.get_age()} days)"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose", 10, 2)
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    plant.get_info()
