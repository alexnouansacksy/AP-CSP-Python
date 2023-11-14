import mylibrary

length = int(input("Length: "))
width = int(input("Width: "))

area = mylibrary.area(length, width)
perimter = mylibrary.perim(length, width)

print(f"Area: {area}\tPerimeter: {perimter}")