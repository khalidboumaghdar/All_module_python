class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1

    def age_info(self):
        self.age += 1

    def get_info(self):
        print(self.name, ':', self.height, 'cm,', self.age, 'days old')


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    height_start = rose.height
    i = 1

    while i <= 7:
        print(f"=== Day {i} ===")
        rose.get_info()
        rose.grow()
        rose.age_info()
        i += 1

    rose.height -= 1
    result_height = rose.height - height_start
    print(f"Growth this week: +{result_height}cm")
