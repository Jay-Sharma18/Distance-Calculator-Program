import math
print("The starting point is (0,0)")
user_input=input("Please enter the direction and distance:")
user_input_list=user_input.split(' ')
xdist=0
ydist=0
for i in range(0,len(user_input_list),2):
    a=user_input_list[i]
    b=user_input_list[i+1]
    if a=="up" or a=='UP':
        ydist+=int(b)
    elif a=="down" or a=="DOWN":
        ydist-=int(b)
    elif a=='right' or a=="RIGHT":
        xdist+=int(b)
    elif a=="left" or a=="LEFT":
        xdist-=int(b)
    else:
        pass
user_input_list=round(int(math.sqrt((xdist*xdist)+(ydist*ydist))))
print("You are {} distance away from (0,0)".format(user_input_list))




