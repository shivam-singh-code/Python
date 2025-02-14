class Vehicle:
    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along...')
    
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")

myCar = Vehicle("tesla", "Model 3")
print(myCar.make)
print(myCar.model)
myCar.get_make_model()
myCar.moves()

youcar = Vehicle("cadillac", "S3")
youcar.get_make_model()

class Airplane(Vehicle):
    def __init__(self, make, model, faa_id) -> None:
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print("Files along...")

class Truck(Vehicle):
    def moves(self):
        print("Rumbles along...")

class GolfCart(Vehicle):
    pass

cessna = Airplane('Cessna', 'Skyhwak', "Faa11")
makc = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yahama', 'GC100')

cessna.get_make_model()
cessna.moves()
makc.get_make_model()
makc.moves()
golfwagon.get_make_model()
golfwagon.moves()

for v in (myCar, youcar, cessna, makc, golfwagon):
    v.get_make_model()
    v.moves()