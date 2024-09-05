class Room:
    def __init__(self, name, description, connections, objects):
        self.name = name
        self.description = description
        self.connections = connections
        self.objects = objects


class Object:
    def __init__(self, name):
        self.name = name

    def interact(self):
        return


class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage