class ShoeController:
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
