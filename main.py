def square():
    i = int(input("How big do you want your square? "))
    for x in range(i):

     symbol = "██"

     print(symbol*i)

def rightTriangle():
    i = int(input("How big do you want your right triangle? "))
    for x in range(i):
     sideGap = i - x
     innerGap = x

     symbol = " "

     if sideGap == 1:
         symbol = "_"

     sideGap *= " "
     innerGap *= symbol

     print("|", innerGap, "\ ", sep="")

def triangle():
    i = int(input("How big do you want your triangle? "))
    for x in range(i):
     sideGap = i - x
     innerGap = x * 2

     symbol = " "

     if sideGap == 1:
         symbol = "_"

     sideGap *= " "
     innerGap *= symbol

     print(sideGap, "/", innerGap, "\ ", sep="")


def chooseShape():
    shape = input("Choose a shape to draw! (Triangle, RightTriangle, Square) ").lower()

    if shape == "righttriangle":
        rightTriangle()
    elif shape == "triangle":
        triangle()
    elif shape == "square":
        square()
    else:
        print("That's not one of the shapes, silly!")
        chooseShape()

print("Howdy! Welcome to the Shape Drawer!")
chooseShape()