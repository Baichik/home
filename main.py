from random import randint

i = 1
point2 = []
point = 0

while i <= 5:
  num = randint(1, 6)
  user = int(input('Отгадайте число от 1 до 6>> '))
  pointsumm = abs(user - num)
  i += 1

  if pointsumm == 0:
    point = 6
    point2.append(point)
  elif pointsumm == 1:
    point = 5
    point2.append(point)
  elif pointsumm == 2:
    point = 4
    point2.append(point)
  elif pointsumm == 3:
    point = 3
    point2.append(point)
  elif pointsumm == 4:
    point = 2
    point2.append(point)
  elif pointsumm == 5:
    point = 1
    point2.append(point)
  else:
    point = 0

  endpoint = sum(point2)

print("Общее количество очков: ", endpoint)

if endpoint < 25:
  print("Вы проиграли! Вы не набрали достаточное количество очков.")
else:
  print("Поздравляю! Вы победили!")




  
  


  
  