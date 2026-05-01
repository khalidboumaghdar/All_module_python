class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, color, name, height, age):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print("The flower is blooming")


class Tree(Plant):
    def __init__(self, trunk_diameter, name, height, age):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print("The tree provides shade")


class Vegetable(Plant):
    def __init__(self, harvest_season, nutritional_value, name, height, age):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    flower = Flower("red", "Rose", 30, 25)
    print(
        f"{flower.name} (Flower): "
        f"{flower.height}cm, {flower.age} days, "
        f"{flower.color} color"
    )
    flower.bloom()

    tree = Tree(50, "Oak", 500, 1825)
    print(
        f"{tree.name} (Tree): "
        f"{tree.height}cm, {tree.age} days, "
        f"{tree.trunk_diameter}cm diameter"
    )
    tree.produce_shade()

    vegetable = Vegetable("Summer", "Vitamin C", "Tomato", 80, 90)
    print(
        f"{vegetable.name} (Vegetable): "
        f"{vegetable.height}cm, {vegetable.age} days"
    )
