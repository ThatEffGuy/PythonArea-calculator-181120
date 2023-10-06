#Calculate area and perimeter using methods
#after inputting length and width
 
#input length and width
def getValues():    
    length = int(input("enter length of rectangle : "))
    width = int(input("enter width of rectangle  : "))
    return length, width
#end getValues

    
#the values for length and width and passed (by value)
#into the method.  Area is calculated and displayed
def getArea(length, width):
    area = length * width
    print ("Area of rectangle = ", area)
#end getArea


#the values for length and width are passed (by value)
#into the method.  the perimeter is calculated and displayed
def getPerimeter(length, width):
    perimeter = 2 * (length + width)
    print ("Perimeter of rectangle = ", perimeter)
#end getPerimeter

#main program
length, width = getValues()   # return length and width values from getValues
getArea(length, width)        # use length and width values in getArea
getPerimeter(length, width)   # use length and width values in getPerimeter
