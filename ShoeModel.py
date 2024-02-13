class Shoe:
    def __init__(self, gender_type, shoe_id, style, color, price, brand, size):
        self.gender_type = gender_type
        self.id = shoe_id
        self.style = style
        self.color = color
        self.price = price
        self.brand = brand
        self.size = size

    def __str__(self):
        return (f"ID: {self.id}, Gender: {self.gender_type}, Style: {self.style}, "
                f"Color: {self.color}, Price: {self.price}, "
                f"Brand: {self.brand}, Size: {self.size}")

class ShoeModel:
    def __init__(self):
        self.shoe = []

    def add_shoe(self, shoe):
        self.shoe.append(shoe)

    def remove_shoe(self, shoe):
        self.shoe.remove(shoe)

    def find_shoe(self, hladane_ID, shoe):
        if hladane_ID in shoe:
            print("nachadza sa")
        else:
            print("nenachadza sa")






