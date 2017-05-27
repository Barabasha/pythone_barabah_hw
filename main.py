# Создать класс Транспортное средство и его потомков - классы Поезд и Самолет.
# В родительском классе должно быть определено минимум 1 инициализатор, 3 атрибута и 1 метод.
# В классах-потомках должны быть добавлены минимум по 1 новому методу и по 1 новому атрибуту.

if __name__ == "__main__":
    import transport
    import train
    import plane

    t1 = train.Train ("ЧМЭЗ", "passenger", 95, "disel")
    t2 = train.Train ("ЭЭЛ", "cargo", 110, "electric")
    p1= plane.Plane ("МиГ-35", "weapons", 2560, "military")
    p2 = plane.Plane("Boeing 747-8", "passenger", 1150, "civil")
    train.Train.print_info(t1)
    train.Train.print_info(t2)
    plane.Plane.print_info (p1)
    plane.Plane.print_info (p2)