
class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = 180 - angle_a

    def __setattr__(self, name, value):
        if name == "side_a" and value <= 0:
            raise ValueError("side_a must be greater than 0")
        if name == "angle_a":
            super().__setattr__(name, value)
            self.angle_b =  180 - value
        if name == "angle_b" and value + self.angle_a != 180:
            raise AttributeError("Sum of angle_b and angle_a do not equal to 180")

        super().__setattr__(name, value)

my_romb = Rhombus(10, 10)
print(f"Rhombus {my_romb.side_a} + angle a {my_romb.angle_a} angle b {my_romb.angle_b}")

my_romb.side_a = 20
my_romb.angle_a = 50
print(f"Rhombus {my_romb.side_a} + angle a {my_romb.angle_a} angle b {my_romb.angle_b}")

try:
    my_romb.angle_b = 150
except AttributeError as e:
    print(f" attribute error raised {e}")
print(f"Rhombus {my_romb.side_a} + angle a {my_romb.angle_a} angle b {my_romb.angle_b}")
