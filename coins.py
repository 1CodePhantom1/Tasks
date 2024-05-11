a=int(input())
mass=[]
for i in range(a):
    mass.append(int(input()))
for i in mass:
    print(2**(i//2+1)-2)
