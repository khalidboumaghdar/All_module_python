class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    r = Plant("Rose", 25, 30)
    s = Plant("Sunflower", 80, 45)
    c = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")

    print(r.name, ":", r.height, "cm,", r.age, "days old")
    print(s.name, ":", s.height, "cm,", s.age, "days old")
    print(c.name, ":", c.height, "cm,", c.age, "days old")
