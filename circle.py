class Circle:

    import point

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def print_info (self):
        print("Circle, x=%d , y=%d, r=%d" %(self.x, self.y, self.r))


    def is_point_in_circle (self,point):
        import math
        r_point_circle = math.sqrt(pow(self.x - point.x, 2) + pow(self.y - point.y, 2))
        if r_point_circle <= self.r :
            return True
        else:
            return False

