class House: 

    def __init__(self, wall_area):
        self.wall_area = wall_area

    def paint_needed(self):
        return self.wall_area * 2.5 

class Paint: 

    def __init__(self, buckets, color):
        self.buckets = buckets
        self.color = color
        


    def total_paint_price(self):
        if self.color == "white":
            return self.buckets * 1.99
        else:
            return self.buckets * 2.19

house1 = House(34)
print(house1.paint_needed())
paint1 = Paint(5, "white")
print(paint1.total_paint_price())