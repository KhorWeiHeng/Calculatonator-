import math
print('Calculator')
print('')
no1= input ('First Number: ')
E=input('Equation Operation (+,-,x /,^, √): ')
no2= input('Second number: ')

if E == '+':
  print(float(no1) + float(no2))

elif E == '-':
  print(float(no1) - float(no2))

elif E == 'x':
  print(float(no1) * float(no2))

elif E == '/':
  print(float(no1) / float(no2))

elif E == '^':
  print(float(no1) ** float(no2))

elif E == '√':
  print(math.sqrt(float(no1)))

else: print ('Error')




