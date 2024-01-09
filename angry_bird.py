class AngryBird:

    def __init__(self):
        self.x = 0
        self.y = 0

    def move_up_by(self, delta):
        self.y  += delta
    

obj = AngryBird()

print(obj)
print(obj.y)

obj.move_up_by(10)
print(obj.y)
