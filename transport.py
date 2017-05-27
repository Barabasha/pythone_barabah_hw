class Transport:

    FORMAT_ATTR = "%5s"
    FORMAT_VALUE = "%20s"
    FORMAT_ALL = FORMAT_ATTR + FORMAT_VALUE

    def __init__(self, model, type_cargo, maximum_speed):
        self.model = model
        self.cargo = type_cargo
        self.maximum_speed = maximum_speed

    def print_info(self):
        print()
        print("----------------------------------")
        print(Transport.FORMAT_ALL % ("Model:        ", self.model))
        print(Transport.FORMAT_ALL % ("Type_cargo:   ", self.cargo))
        print(Transport.FORMAT_ALL % ("Maximum_speed:", self.maximum_speed))

