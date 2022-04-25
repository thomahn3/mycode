point3a = int(input())
point2a = int(input())
point1a = int(input())
point3b = int(input())
point2b = int(input())
point1b = int(input())

if point3a*3+point2a*2+point1a*1 > point3b*3+point2b*2+point1b*1:
    print("A")
elif point3a*3+point2a*2+point1a*1 < point3b*3+point2b*2+point1b*1:
    print("B")
else:
    print("T")