#Cassidy Bickler and Tyler Else
#CPE-551-WS Final Project
#I pledge my honor that I have abided by the Stevens Honor System
import math
from decimal import Decimal

print("Welcome to the Ductwork Sizing Tool")

#Ask for four inputs: Air Flow and Usage
AirFlow = input("Please provide the Air Flow (CFM):")
print("AirFlow: " + AirFlow)

Usage = input("Please provide the Usage:")
print("Usage: " + Usage)

Shape = input("Please select the letter of the required Duct Shape: \na. Rectangular \nb. Circular \nc. Oval \nd. Oblong \n(Lower case letter only please): ")
print("Shape: " + Shape)

Location1 = input("Please choose \ne. Exposed, \nf. Above Ceiling \ng. In Shaft \n(Lower case letter only please): ")
print("Location1: " + Location1)

Location2 = input("Please choose \nh. Main \ni. Branch \n(Lower case letter only please): ")
print("Location2: " + Location2)

#initialize our testing variables
w = 2
d = 0
PassingList = []
PassingTest = 0

#First loop for interval w, once every interval of d (2-100) has been tested against that w value
while (w<102):
#Once w has been tested against each even number in d to 100, w is intervaled and d is reset to 0
    if (w==100) and (d==100):
        print('Calculations complete, all Depths and Widths that passed all test cases are stored in PassingResults.txt')
        quit()
#Program complete condition
    elif (d==100):
        w=w+2
        d=0
    else:
#1st calculating the Equivalent D (in)[Shape specific]
        while (d<100):
            d=d+2
            print('\nTesting D = ' + str(d))
            print('Testing W = ' + str(w))
            if Shape == 'a':
                EqD=0
                EqD=(1.3*((w*d)**0.625))/((w+d)**0.25)
            elif Shape == 'b':
                EqD = d
            elif Shape == 'c':
                EqD = (1.55*(w)**(0.625))/(2(math.pi)(1/2((w/2)**(2)+(d/2)**(2))))**0.5
            elif Shape == 'd':
                EqD = (1.55*(((math.pi)*((d**2)/4)+(w*d)-(d**2))**0.625)/((((math.pi)*d)+(2*w)-(2*d))**0.25))
            else:
                print("Error, valid option not available. Exiting Program.")
                quit()
#2nd Calculate Velocity (FPM) [EVERYONE]
            v=(144*int(AirFlow))/((math.pi)*((EqD/2)**2))
#3rd Calculate Friction (in.wg/100ft) [EVERYONE]
            f=((0.109136*(int(AirFlow)**1.9))/(EqD**5.02))
#W:D Ratio
            if Shape == 'b':
                wdRatio = 0
            else:
                wdRatio = w/d
#Friction Loss Pass/Fail Criteria
    #Return, OA, Gen. Exhaust
            if int(AirFlow)<1000:
                f1=((10**(math.log(0.02,10)-((math.log(4,10)*math.log(50,10))/math.log(20,10))))*(int(AirFlow)**(math.log(4,10)/math.log(20,10))))
            elif int(AirFlow)>30000:
                f1=((10**(math.log(0.08,10)-((math.log(0.01875,10)*math.log(30000,10))/math.log(40/3,10))))*(int(AirFlow)**(math.log(0.01875,10)/math.log(40/3,10))))
            elif int(AirFlow)>1000 and int(AirFlow)<30000:
                f1=0.8000
                f1=int(f1)
            elif int(AirFlow)>40000:
                print("AirFlow is out of bounds. Exiting Program.")
                quit()
            else:
                print("Error, AirFlow is not valid. Exiting Program.")
                quit()
    #Test
            if f1>f:
                break            
            else:
                FinalF='Pass'
    #Supply Low
            if int(AirFlow)<1000:
                s1=((10**(math.log(0.05,10)-((math.log(2,10)*math.log(50,10))/math.log(20,10)))))*(int(AirFlow)**(math.log(2,10)/math.log(20,10)))
            elif int(AirFlow)>50000:
                s1=((10**(math.log(0.1,10)-((math.log(0.25,10)*math.log(50000,10))/math.log(20,10))))*(C10**(math.log(0.25,10)/math.log(20,10))))
            elif int(AirFlow)>1000 and int(AirFlow)<50000:
                s1=0.1000
            elif int(AirFlow)>400000:
                print("Error, AirFlow is not valid. Exiting Program.")
                quit()
            else:
                print("Error, AirFlow is not valid. Exiting Program.")
                quit()
    #Test
            if s1<f:
                break            
            else:
                Finals1='Pass'
    #VAV Supply
            s2=s1+0.05
    #Test
            if s2<f:
                break            
            else:
                Finals2='Pass'
    #Supply Medium
            if int(AirFlow)<1000:
                m1=((10**(math.log(0.15,10)-((math.log(5/3,10)*math.log(50,10))/math.log(20,10))))*(C10**(math.log(5/3,10)/math.log(20,10))))
            elif int(AirFlow)>10000:
                m1=((10**(math.log(0.25,10)-((math.log(0.1,10)*math.log(10000,10))/math.log(40,10))))*(C10**(math.log(0.1,10)/math.log(40,10))))
            elif int(AirFlow)>1000 and int(AirFlow)<10000:
                m1=0.25
            elif int(AirFlow)>400000:
                print("Error, AirFlow is not valid. Exiting Program.")
                quit()
            else:
                print("Error, AirFlow is not valid. Exiting Program.")
                quit()
    #Test    
            if m1<f:
                break            
            else:
                m1 = 'Pass'
#Velocity Pass/ Fail Criteria
            if Shape == 'a':
                if Location1 == 'e':
                    if Location2 == 'h':
                        if v<1450:
                            Velocity = 'Pass'
                        else:
                            break
                    elif Location2 == "i":
                        if v<950:
                            Velocity = 'Pass'
                        else:
                            break
                    else:
                        break
                elif Location1 == "f":
                    if Location2 == "h":
                        if v<1750:
                            Velocity = 'Pass'
                        else:
                            break
                            
                    elif Location2 == "i":
                        if v<1200:
                            Velocity = 'Pass'
                        else:
                            break
                            
                    else:
                        break
                elif Location1 == "g":
                    if Location2 == "h":
                        if v<2500:
                            Velocity = 'Pass'
                        else:
                            break
                            
                    elif Location2 == "i":
                        if v<1700:
                            Velocity = 'Pass'
                        else:
                            break
                    else:
                        break
                else:
                    break
            elif Shape == "b":
                if Location1 == "e":
                    if Location2 == "h":
                        if v<2600:
                            Velocity = 'Pass'
                        else:
                            break
                    elif Location2 == "i":
                        if v<1700:
                            Velocity = 'Pass'
                        else:
                            break
                    else:
                        break
                elif Location1 == "f":
                    if Location2 == "h":
                        if v<3000:
                            Velocity = 'Pass'
                        else:
                            break
                    elif Location2 == "i":
                        if v<2000:
                            break
                        else:
                            Velocity = 'Pass'
                    else:
                        break
                elif Location1 == "g":
                    if Location2 == "h":
                        if v<3500:
                            Velocity = 'Pass'
                        else:
                            break
                    elif Location2 == "i":
                        if v<2500:
                            Velocity = 'Pass'
                        else:
                            break 
                    else:
                        break
                else:
                    break
            elif Shape == "c" or "d":
                if Location1 == "e":
                    if Location2 == "h":
                        if v<2025:
                            Velocity = 'Pass'
                        else:
                            break
                    elif Location2 == "i":
                        if v<1325:
                            Velocity = 'Pass'
                        else:
                            break
                    else:
                        break
                elif Location1 == "f":
                    if Location2 == "h":
                        if v<2375:
                            Velocity = 'Pass'
                        else:
                            break
                    elif Location2 == "i":
                        if v<1600:
                            Velocity = 'Pass'
                        else:
                            break
                    else:
                        break
                elif Location1 == "g":
                    if Location2 == "h":
                        if v<3000:
                            Velocity = 'Pass'
                        else:
                            break
                    elif Location2 == "i":
                        if v<2100:
                            Velocity = 'Pass'
                        else:
                            break
                    else:
                        break
                else:
                    break         
#Test and create output
            PassingTest = ('Width(in): ' + str(d) +'  Depth(in): ' + str(w) + '  EqD(in): ' + str(EqD) + '  Velocity(FPM): ' + str(v) + '  Friction(in.wg/100ft): ' + str(f) + '  W:D Ratio: '+ str(wdRatio) + '\n--Friction Loss Pass/Fail Criteria\n ' + 'Return, OA, Gen. Exhaust: ' + FinalF + '  Supply Low: ' + Finals1 + '  VAV Supply: ' + Finals2 + '  Supply Medium: ' + m1 + '\nVelocity Pass/Fail: ' + Velocity)
            with open("PassingResults.txt", "a") as txt:
                txt.write("\n")
                txt.write(PassingTest)
