class Food:
    def __init__(self, protein, carb, fat):
        self.protein = protein
        self.carb = carb
        self.fat = fat
        self.elements = [protein, carb, fat]

    def __str__(self):
        return f"количество каллорий продукта: {self.energy_food()}"

    def __add__(self, other):
        return Food(self.protein + other.proteins, self.carb + other.carb, \
                    self.fat + other.fat)

    def __mul__(self, other):
        return Food(self.protein * other, self.carb * other, self.fat * other)

    def __iadd__(self, other):
        return Food(self.protein * other, self.carb * other, self.fat * other)

    def __sub__(self, other):
        return self.energy_food() - other.energy_food()

    def __eq__(self, other):
        return self.energy_food() == other.energy_food()

    def __lt__(self, other):
        return self.energy_food() < other.energy_food()

    def __getitem__(self, item):
        return self.elements[item]

    def __len__(self):
        return len(self.elements)

    def __setitem__(self, key, value):
        return self.elements.append(value)

    def energy_food(self):
        return self.fat * 9 + (self.carb + self.protein) * 4.2


if __name__ == "__main__":
    carrot = Food(8, 2, 28)
    milk = Food(47, 23, 2)
    print(carrot < milk)
    print("the length of the object:", len(carrot))
    carrot[8] = 55
    print("the length of the object:", len(carrot))