import transport
class Plane (transport.Transport):

    def __init__(self, model, type_cargo, maximum_speed, assignment):
        super().__init__(model, type_cargo, maximum_speed)
        self.assignment = assignment

    def print_info(self):
        super().print_info()
        print(transport.Transport.FORMAT_ALL % ("Assignment:   ", self.assignment))

    def speed_comparison(plane1,plane2):
        print()
        if plane1.maximum_speed > plane2.maximum_speed :
            print("%s faster than %s for %s km/hr" %(plane1.model, plane2.model, plane1.maximum_speed-plane2.maximum_speed))
        else :
            print("%s faster than %s for %s km/hr" %(plane2.model, plane1.model, plane2.maximum_speed-plane1.maximum_speed))
