rows=int(input("Enter number of rows "))
for i in range(rows*2):
    if i%2!=0:
        print(" "*int(rows-(i+1)/2)+"*"*(i))