import transport
class Train (transport.Transport):

    def __init__(self, model, type_cargo, maximum_speed, engine_type):
        super().__init__(model, type_cargo, maximum_speed)
        self.engine_type = engine_type


    def print_info(self):
        super().print_info()
        print(transport.Transport.FORMAT_ALL %("Engine_type:  ", self.engine_type))

    def is_type_cargo_passenger(self):
        print()
        if self.cargo == "passenger":
            print(self.model, "is passenger")
        else:
            print(self.model, "is not passenger")


