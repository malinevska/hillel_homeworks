class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        if key == "side_a" and value <= 0:
            raise ValueError("The side should be bigger than 0.")

        if key == "angle_a":
            if not (0 < value < 180):
                raise ValueError("The angle should be between 0 and 180.")
            super().__setattr__(key, value)
            super().__setattr__("angle_b", 180 - value)
        else:
            super().__setattr__(key, value)


r = Rhombus(10, 60)
print(f"The side A: {r.side_a}, angle A: {r.angle_a}, angle B: {r.angle_b}")