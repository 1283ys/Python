weight=float(input('Enter your weight: '))
num=int(input('1-Mercury 2-Venus 3-Mars 4-Jupiter 5-Saturn 6-Uranus 7-Neptune Enter the planet number: '))
if num==1:
  relative_gravity=0.38
elif num==2:
  relative_gravity=0.91
elif num==3:
  relative_gravity=0.38 
elif num==4:
  relative_gravity=2.53 
elif num==5:
  relative_gravity=1.07
elif num==6:
  relative_gravity=0.89 
elif num==7:
  relative_gravity=1.14
else:
  print('Invalid planet number')                
destination_weight=weight*relative_gravity
print(destination_weight)  
