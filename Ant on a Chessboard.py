#Jacob Pradels
#Thomas McSwain
#Neville Lee
#3/18/19
#10161 Ant on a Chessboard
import math

def findAnt(input_num):
    sqrt_num = math.sqrt(input_num)
    nearest_num = round(sqrt_num)
    if ((nearest_num%2 == 0) and (input_num == nearest_num**2)):
        x_axis = nearest_num
        y_axis = 1
    elif ((nearest_num%2 != 0) and (input_num == nearest_num**2)):
        x_axis = 1
        y_axis = nearest_num
    elif ((nearest_num%2 == 0) and (input_num < nearest_num**2)):
        x_axis = nearest_num
        y_axis = nearest_num**2 - input_num + 1
    elif ((nearest_num%2 == 0) and (input_num > nearest_num**2)):
        x_axis = nearest_num + 1
        y_axis = input_num - nearest_num**2
    elif ((nearest_num%2 != 0) and (input_num < nearest_num**2)):
        y_axis = nearest_num
        x_axis = nearest_num**2 - input_num + 1
    elif ((nearest_num%2 != 0) and (input_num > nearest_num**2)):
        y_axis = nearest_num + 1
        x_axis = input_num - nearest_num**2
    return [x_axis,y_axis]
input_number = int(input(""))
while input_number != 0:
    point=findAnt(input_number)
    print(point[0],point[1])
    input_number = int(input(""))
    

