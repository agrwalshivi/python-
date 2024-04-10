import math
def triangle_area_heron(a,b,c):
    s=((a+b+c)/2)
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area
a=float(input("enter the first side:"))
b=float(input("enter the second side:"))
c=float(input("enter the third side:"))

area=triangle_area_heron(a,b,c)
print("area of triangle is:",area)
