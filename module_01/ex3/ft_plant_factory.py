class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(self.name, ':', self.height, 'cm,', self.age, 'days old')


if __name__ == "__main__":
    plants_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 80, 45)
    ]

    plants = []
    count = 0
    for name, height, age in plants_data:
        plants += [Plant(name, height, age)]
        count += 1

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created:", end=" ")
        plant.get_info()

    print("Total plants created:", count)
