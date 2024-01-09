class Polygon:

    type = "Polygon"

    def __init__(self, sides, length):
        if sides < 3:
            raise Exception("A polygon must have at least 3 sides.")

        self.sides = sides
        self.length = length

    def identify_polygon(self):
        identifier_dict = {
            3: "Triangle",
            4: "Quadrilateral",
            5: "Pentagon",
            6: "Hexagon",
            7: "Heptagon",
            8: "Octagon",
            9: "Nonagon",
            10: "Decagon"
        }
        try:
            self.type = identifier_dict[self.sides]
        except KeyError:
            self.type = f"Polygon with {self.num_sides} sides"

    
    @classmethod
    def polygon_factory(cls, lst):

        all_objs = []

        for sides, length in lst:
            all_objs.append(cls(sides, length))

        return all_objs

    @staticmethod
    def get_perimeter(polygon):
        return polygon.sides * polygon.length


    
        