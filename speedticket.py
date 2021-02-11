#speedticket.py
name=""
speed_limit=0.00
speed_vehicle=0.00
difference=0.00
fine=0.00

#warrant_list
warrant_list = ["Alex", "Anson", "Josh"]

#define function
def calculatefine(speed_vehicle, speed_limit):
    difference = speed_vehicle - speed_limit
    fine= difference*10
    if difference > 0:
        if difference > 50:
            if difference < 80:
                print(name, "You loose license")
            else:
                print(name, "You are going to jail !")
        else:
            print(name, "The fine is {}".format(fine))
    else:
        print("You are driving under speed limit")

while name=="":
    name=input("Enter the name of the driver")
    if name in warrant_list:
      print("You're under arrest")
      exit()
    else:
      print("You're not in the warrant list, You're free to continue")
      continue 

speed_vehicle=float(input("please enter your vehicle speed"))
speed_limit= float(input("please enter speed limit"))

# calling function
calculatefine(speed_vehicle, speed_limit)





    