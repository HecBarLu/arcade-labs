class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

def main():

    room_list = []
    room = Room("You're in Bedroom 2 there's a bed at your right and a big cupboard behind you",
                north=3,
                east=1,
                south=None,
                west=None)
    room_list.append(room)
    room1 = Room("You're in the South hall there's a draw of Ronaldo at your left",
                north=4,
                east=2,
                south=None,
                west=0)
    room_list.append(room1)
    room2 = Room("You're in the dinning room where you can have a great meal",
                 north=5,
                 east=None,
                 south=None,
                 west=1)
    room3 = Room("You're in Bedroom 1 where you can have a placid nap",
                 north=None,
                 east=4,
                 south=0,
                 west=None)
    room_list.append(room3)
    room4 = Room("You're in the north hall where is a big sculpture from Messi",
                 north=6,
                 east=5,
                 south=1,
                 west=3)
    room_list.append(room4)
    room5 = Room("You're in the kitchen do a fucking pasta with tomate",
                 north=None,
                 east=None,
                 south=2,
                 west=4)
    room_list.append(room5)
    room6 = Room("You're in the balcony look at this beautiful landscape",
                 north=None,
                 east=None,
                 south=4,
                 west=None)
    room_list.append(room6)
    current_room = 0
    room_list[0] = current_room
    done = False
    while(done != False):
        print(" ")
        print(room_list[0].description)
        print(input("Where do you want to go next: "))

main()