class Room:
    name = ""
    description = ""
    north = 0
    east = 0
    south = 0
    west = 0
    secret = False

    def __init__(self, name ="", description ="" ,north = None, east = None, south = None, west = None, secret:bool = False):
        self.name = name
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.secret = secret
def main():
    roomList = []

    lobby = Room("Lobby","Main entrance to the building.",3,4,2,0)
    balcony = Room("Balcony", "Balcony with good views to the West.", None, 1, None)
    bedroom1 = Room("Main Bedroom", "Big bed.", None, None, 1)
    storage = Room("Storage", "Why there is a storage in the middle of the house?", None,5,None,1)
    hall = Room("Hallway", "Another hallway.", None, 6, None, 4)
    bigRoom = Room("Big Empty Room", "Could have some lighting in here.", 7, 9, None, 5)
    paintingRoom = Room("Painting Room", "Why all the paintings are cats and feet???", None, 8, 6)
    storage2 = Room("Small Storage", "Who designed this house???", None, None, None, 7)
    secret1 = Room("Secret Room", "... What is this?? ... There is a lighting over there.", None, None, 10, 6,True)
    secret2 = Room("Hideout", "HADDAN HUSSEIN????!?!?!?!?!?", 9, None, None, None)




main()