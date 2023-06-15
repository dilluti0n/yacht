#yacht dice game v1.01

import random

yrdice = [0, 0, 0, 0, 0]
rule = []
for i in range(12) :
  rule.append('-')

def roll() :
  global yrdice
  for i in range(len(yrdice)) :
    yrdice[i] = random.randrange(1,7)
  return yrdice

def sheet() :
  print("---------------------------------------")
  print("                 점수표")
  print("1. Ones :",rule[0])
  print("2. Twos :",rule[1])
  print("3. Threes :",rule[2])
  print("4. Fours :",rule[3])
  print("5. Fives :",rule[4])
  print("6. Sixes :",rule[5])
  print("")
  print("7. Choice :",rule[6])
  print("8. 4 of Kind :",rule[7])
  print("9. Full House :",rule[8])
  print("10. Little Straight :",rule[9])
  print("11. Big Straight :",rule[10])
  print("12. Yacht :",rule[11])
  sum = 0
  for i in rule :
    if str(type(i)) == "<class 'int'>" :
      sum += i
  print("sum :",sum)
  print("---------------------------------------")

def calc(a) :
  global rule

  if str(type(rule[a-1])) == "<class 'int'>" :
    print("이전에 선택했던 규칙을 선택하셨습니다.")
    a = input("적용할 규칙을 선택하십시오 >> ")
    return calc(a)

  for i in range(1,7) :
    if a == i :
      rule[i-1] = 0
      for j in yrdice :
        if j == i :
          rule[i-1] += i

  if a == 7 :
    rule[6] = sum(yrdice)

  if a == 8 :
    rule[7] = 0
    for i in range(1,7) :
      if yrdice.count(i) == 4 or yrdice.count(i) == 5:
        rule[7] = sum(yrdice)

  if a == 9 :
    rule[8] = 0
    for i in range(1,7) :
      for j in range(1,7) :
        if yrdice.count(i) == 3 and yrdice.count(j) == 2 :
          rule[8] = sum(yrdice)

  if a == 10 :
    rule[9] = 0
    if sorted(yrdice) == [1,2,3,4,5] :
      rule[9] = 30

  if a  == 11 :
    rule[10] = 0
    if sorted(yrdice) == [2,3,4,5,6] :
      rule[10] = 30

  if a == 12 :
    rule[11] = 0
    for i in range(1,7) :
      if yrdice.count(i) == 5 :
        rule[11] = 50

def game() :
  sheet()
  print("\n0. 프로그램 종료\n1. 주사위 굴리기")
  yourchoice2 = input(">> ")
  if yourchoice2 == '0' :
    quit()
  elif yourchoice2 == '1' :
    print("\n아래가 당신이 굴린 주사위입니다.")
    print(roll())
    print("\n0. 프로그램 종료\n1. 이대로 진행\n2. 변경할 주사위 선택")
    yourchoice3 = input(">> ")
    if yourchoice3 == '0' :
      quit()
    elif yourchoice3 == '1' :
      sheet()
      a = int(input("적용할 규칙을 선택하십시오 >> "))
      calc(a)
      temp = 0
      for i in rule :
        if str(type(i)) == "<class 'int'>" :
          temp += 1
      if temp == 12 :
        sheet()
        print("yacht dice game 이 끝났고 결과는 위와 같습니다.")
        return
      else :
        return game()
    elif yourchoice3 == '2' :
      for i in range(2) :
        temp = 1
        riddice = []
        while temp != 0 :
          try :
            print("\n변경할 주사위를 선택해주세요(1-5)\n더이상 선택할 주사위가 없으면 0을 눌러주세요.")
            temp = int(input(">> "))
            if temp > 5 :
              print("잘못 입력하셨습니다.")
            elif riddice.count(temp) == 1 :
              print("중복된 숫자를 입력하셨습니다.")
            elif temp != 0 :
              riddice.append(temp)
          except:
            print("잘못 입력하셨습니다.")
        for dienum in riddice :
            yrdice[dienum - 1] = random.randrange(1,7)
        print("\n아래가 당신이 굴린 주사위입니다.")
        print(yrdice)
        if i == 0:
          print("\n0. 프로그램 종료\n1. 이대로 진행\n2. 변경할 주사위 선택")
          yourchoice4 = input(">> ")
          if yourchoice4 == '0' :
            quit()
          elif yourchoice4 == '1' :
            break
      sheet()
      a = int(input("적용할 규칙을 선택하십시오 >> "))
      calc(a)
      temp = 0

      for i in rule :
        if str(type(i)) == "<class 'int'>" :
          temp += 1
      if temp == 11 :
        sheet()
        print("yacht dice game 이 끝났고 결과는 위와 같습니다.")
        return
      else :
        return game()

while True :
  print("---------------------------------------")
  print("              yacht V 1.0")
  print("              made by kim")
  print("---------------------------------------")
  print("0. 프로그램 종료\n1. 게임 시작")
  yourchoice = input(">> ")
  if yourchoice == '0' :
    break
  elif yourchoice == '1' :
    game()
    break


