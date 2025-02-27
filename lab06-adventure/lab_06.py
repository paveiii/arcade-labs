from pycparser.c_ast import Switch


class Room:
    name = ""
    description = ""
    north = 0
    east = 0
    south = 0
    west = 0
    secret = False
    axe = False

    def __init__(self, name ="", description ="" ,north = None, east = None, south = None, west = None, secret:bool = False, axe = False):
        self.name = name
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.secret = secret
        self.axe = axe
    def return_adjacent_rooms(self):
        return (self.north,self.east,self.south,self.west)
    def desecretify(self):
        self.secret = False
def main():
    roomList = []

    balcony = Room("Balcony", "Balcony with good views to the West.", None, 1, None)
    roomList.append(balcony)
    lobby = Room("Lobby","Main entrance to the building.",3,4,2,0)
    roomList.append(lobby)
    bedroom2 = Room("Guest Bedroom", "Smol bed.", 1)
    roomList.append(bedroom2)
    bedroom1 = Room("Main Bedroom", "Big bed.", None, None, 1)
    roomList.append(bedroom1)
    storage = Room("Storage", "Why there is a storage in the middle of the house?", None,5,None,1)
    roomList.append(storage)
    hall = Room("Hallway", "Another hallway.", None, 6, None, 4)
    roomList.append(hall)
    bigRoom = Room("Big Empty Room", "Could have some lighting in here.", 7, 9, None, 5)
    roomList.append(bigRoom)
    paintingRoom = Room("Painting Room", "Why all the paintings are cats and feet???", None, 8, 6,None,False,True)
    roomList.append(paintingRoom)
    storage2 = Room("Small Storage", "Who designed this house???", None, None, None, 7)
    roomList.append(storage2)
    secret1 = Room("Secret Room", "... What is this?? ... There is a lighting over there.", None, None, 10, 6,True)
    roomList.append(secret1)
    secret1 = Room("Hideout", "HADDAN HUSSEIN????!?!?!?!?!?", 9, None, None, None)
    roomList.append(secret1)

    playerHasAxe = False
    currentRoom = 1

    print("FIND HIM")

    while(True):
        print(roomList[currentRoom].name)
        print(roomList[currentRoom].description)
        possible_rooms = roomList[currentRoom].return_adjacent_rooms()

        if(playerHasAxe):
           print("Swing axe through walls?")
           decision = input("(Y/N)")
           if (decision == "Y"):
               secrets = False
               for room in possible_rooms:
                   if(room != None and roomList[room].secret == True):
                       roomList[room].desecretify()
                       print("You found a secret!")
                       secrets = True
               if(secrets == False):
                   print("You just destroyed private propety. Too bad.")
           else:
               pass
        if(roomList[currentRoom].axe and playerHasAxe == False):
           print("There is an axe laying around. Do you want to pick it up?")
           decision = input("(Y/N)")
           if(decision=="Y"):
               playerHasAxe = True
           else:
                pass

        print(return_possible_ways(roomList[currentRoom]))
        nextRoom = move_room(roomList[currentRoom],input())
        if(nextRoom == -1):
            print("You cant go there!")
        else:
            if(roomList[nextRoom].secret):
                print("You cant go there silly. There is no door!")
            else: currentRoom = nextRoom
        print("\n")


def return_possible_ways(room):
    adjacents = room.return_adjacent_rooms()
    output = "You can go to:"
    for i in range(len(adjacents)):
        match(i):
            case 0:
                if(adjacents[i] != None):
                    output += " North "
            case 1:
                if (adjacents[i] != None):
                    output += " East "
            case 2:
                if (adjacents[i] != None):
                    output += " South "
            case 3:
                if (adjacents[i] != None):
                    output += " West "

    return output
def move_room(currentRoom, decision):
    available_directions = currentRoom.return_adjacent_rooms()
    match(decision):
        case "N" | "North" | "north":
            if(available_directions[0] != None):
                return currentRoom.north
        case "E" | "East" | "east":
            if(available_directions[1] != None):
                return currentRoom.east
        case "S" | "South" | "south":
            if(available_directions[2] != None):
                return currentRoom.south
        case "W" | "West" | "west":
            if(available_directions[3] != None):
                return currentRoom.west
    return -1
main()