import time

Tabuleiro = [[" "]*20 for i in range(10)]
Boot = 1
Columns = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
Near = [] 
Placed = []
PlacedNeighbors = []




def Screen(): 
    if Boot == 1:
        print("  " + "".join(Columns))

    for i in range(10):
        print(str(i)*Boot + " " +"".join(Tabuleiro[i]))
    print("-"*20)




def Start():
    global Boot, Near,Placed, PlacedNeighbors
    Coords = []

    ans = str(input("Column and Line (Ex:D1):")).upper()
    Coords.append(ans)
    while ans != "DONE":
        Id = int(str(Columns.index(ans[0])) + ans[1])
        Placed += [Id]
        ans = str(input("Column and Line (Ex:D1):")).upper()
        Coords.append(ans)

    del Coords[-1]
    print(Placed)
    

    
        
    for i in range(len(Placed)):
        Buff = [Placed[i]-11,Placed[i]-10,Placed[i]-9,Placed[i]-1,Placed[i]+1,Placed[i]+11,Placed[i]+10,Placed[i]+9]
        PlacedNeighbors += [i for i in Buff if i in Placed]
        Near += [i for i in Buff if i not in PlacedNeighbors]
        Tabuleiro[int(Coords[i][1])][Columns.index(Coords[i][0])] = "X"

    
    
    
    Screen()
    Boot = 0
    
    

Start()


def Rules():
    global PlacedNeighbors, Near, Placed
    
    ToRevive = list(set([i for i in Near if Near.count(i) == 3]))
    ToDie = list(set([i for i in PlacedNeighbors if PlacedNeighbors.count(i) != 2 and PlacedNeighbors.count(i) != 3]))
    ToDie += [i for i in Placed if i not in PlacedNeighbors]
    Placed = [i for i in Placed if i not in ToDie]
    Placed += ToRevive
    PlacedNeighbors, Near = [], []
    

    for i in range(len(ToRevive)):
        Tabuleiro[int(str(ToRevive[i])[-1])][int(str(ToRevive[i])[:-1])] = "X"

    for i in range(len(ToDie)):
        Tabuleiro[int(str(ToDie[i])[-1])][int(str(ToDie[i])[:-1])] = " "
    
    for i in range(len(Placed)):
        Buff = [Placed[i]-11,Placed[i]-10,Placed[i]-9,Placed[i]-1,Placed[i]+1,Placed[i]+11,Placed[i]+10,Placed[i]+9]
        PlacedNeighbors += [x for x in Buff if x in Placed]
        Near += [x for x in Buff if x not in PlacedNeighbors]
    
    

    time.sleep(5)
    Screen()
    Rules()
        
Rules()