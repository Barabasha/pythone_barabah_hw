import transport
class Plane:

    def __init__(self, model, type_cargo, maximum_speed, assignment):
        transport.Transport.__init__(self, model, type_cargo, maximum_speed)
        self.assignment = assignment

    def print_info(self):
        transport.Transport.print_info(self)
        print(transport.Transport.FORMAT_ALL % ("Assignment:   ", self.assignment))