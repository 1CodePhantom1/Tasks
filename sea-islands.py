#input sea
size_x=int(input())
size_y=int(input())
sea=[]
for i in range(size_y):
    sea.append(list(input()))

#checking ilands around
def check_around(size_x, size_y, sea, i, island):
    sea[i//size_x][i%size_x]="0"
    row=sea[i//size_x]
    #check right
    if i%size_x<size_x-1:
        if row[i%size_x+1]=="1":
            island.append(i+1)
            check_around(size_x, size_y, sea, i+1, island)
    #check left
    if i%size_x>0:
        if row[i%size_x-1]=="1":
            island.append(i-1)
            check_around(size_x, size_y, sea, i-1, island)
    #check up
    if i//size_x>0:
        row=sea[i//size_x-1]
        if row[i%size_x]=="1":
            island.append(i-size_x)
            check_around(size_x, size_y, sea, i-size_x, island)
    #check down
    if i//size_x<size_y-1:
        row=sea[i//size_x+1]
        if row[i%size_x]=="1":
            island.append(i+size_x)
            check_around(size_x, size_y, sea, i+size_x, island)
    return island

#main
islands=[]
for i in range(size_x*size_y):
    row=sea[i//size_x]
    cell=row[i%size_x]
    if cell!="1":
        continue
    island=check_around(size_x, size_y, sea, i, [i])
    islands.append(island)
print(len(islands))