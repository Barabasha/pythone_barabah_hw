import transport
class Train (transport.Transport):

    def __init__(self, model, type_cargo, maximum_speed, engine_type):
        transport.Transport.__init__(self, model, type_cargo, maximum_speed)
        self.engine_type = engine_type

    def print_info(self):
        transport.Transport.print_info(self)
        print(transport.Transport.FORMAT_ALL %("Engine_type:  ", self.engine_type))

