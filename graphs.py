class Point():
    def __init__(self):
        self.connections=[]
    
class Node():
    def __init__(self, firtsP, secondP):
        self.firstP=firtsP
        self.secondP=secondP
    
        
point_max, conn_qty = map(int, input().split())
glob_start_Point, glob_end_Point = map(int, input().split())
points=[]

for i in range(point_max):
    thP = Point()
    points.append(thP)

for i in range(conn_qty):
    this_conn=input()
    start_Point=int(this_conn[0])
    end_Point=int(this_conn[2])
    this_Node=Node(points[start_Point], points[end_Point])
    points[start_Point].connections.append(this_Node)
    points[end_Point].connections.append(this_Node)

weights=[]
passed=[]
weight=0
def go(startP, endP, passed_points):
    global weight, weights
    weight+=1
    for i in startP.connections:
        if i.firstP==endP:
            weights.append(weight)
            weight-=1
            return
        if i.secondP==endP:
            weights.append(weight)
            weight-=1
            return
        if i.firstP not in passed_points:
            passed_points_copy=list(passed_points)
            passed_points_copy.append(i.firstP)
            go(i.firstP, endP, passed_points_copy)
        if i.secondP not in passed_points:
            passed_points_copy=list(passed_points)
            passed_points_copy.append(i.secondP)
            go(i.secondP, endP, passed_points_copy)
    weight-=1

go(points[glob_start_Point], points[glob_end_Point], passed)
print(min(weights))
        