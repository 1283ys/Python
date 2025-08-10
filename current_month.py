month=int(input('Enter the current month :'))
if month>=1 and month<4 :
  print('Winter 🌨️')
elif month<7and month!=0 :
  print('Spring 🌱')
elif month<10and month!=0:
  print('Summer🌻')
elif month<13and month!=0 :  
  print('Autumn 🍂')
else:
  print('Invalid')   
