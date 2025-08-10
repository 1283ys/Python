gry=0
rav=0
huf=0
sly=0
a=int(input('Do you like dawn or dusk? 1 for dawn 2 for dusk: '))
if a==1:
  gry+1
  rav+1
elif a==2:
  huf+1
  sly+1
else:
  print('wrong input')  

b=int(input('Q2) When I’m dead, I want people to remember me as: 1) The Good 2) The Great 3) The Wise 4) The Bold')) 
if b==1:
  huf+2
elif b==2:
  sly+2
elif b==3:
  rav+2
elif b==4:
  gry+2   
else:
 print('wrong input')

c=int(input('Q3) Which kind of instrument most pleases your ear 1) The violin 2) The trumpet 3) The piano 4) The drum')) 
if c==1:
  sly+4
elif c==2:
  huf+4
elif c==3:
  rav+4
elif c==4:
  gry+4
else:
  print('wrong input')   

print("your scores are:")
print("🦁 Gryffindor:")
print(gry)
print("🦅 Ravenclaw:")
print(rav)
print("🦡 Hufflepuff:")
print(huf)
print("🐍 Slytherin:")
print(sly)

  
