#yacht dice game v1.02

import random
import os

yrdice = [0, 0, 0, 0, 0]
rule = ['-' for _ in range(12)]

def roll() :
	global yrdice
	for i in range(len(yrdice)) : yrdice[i] = random.randrange(1,7)
	
	return yrdice

def sheet() :
	print("---------------------------------------")
	print("                 점수표")
	print("1. Ones                              {}".format(rule[0]))
	print("2. Twos                              {}".format(rule[1]))
	print("3. Threes                            {}".format(rule[2]))
	print("4. Fours                             {}".format(rule[3]))
	print("5. Fives                             {}".format(rule[4]))
	print("6. Sixes                             {}".format(rule[5]))
	print("")
	print("7. Choice                            {}".format(rule[6]))
	print("8. 4 of Kind                         {}".format(rule[7]))
	print("9. Full House                        {}".format(rule[8]))
	print("10. Little Straight                  {}".format(rule[9]))
	print("11. Big Straight                     {}".format(rule[10]))
	print("12. Yacht                            {}".format(rule[11]))
	
	sum = 0
	for i in rule :
		if str(type(i)) == "<class 'int'>" : sum += i
		
	print("\nSCORE                              {}".format(sum))
	print("---------------------------------------")

def calc(a) :
	global rule
	
	while True :
		try : 
			a = int(a)
			break
		except : 
			print("[sys]잘못 입력하셨습니다.")
			a = input("적용할 규칙을 선택하십시오 >>")
	
	if a > 12 or a < 1 :
		print("[sys]잘못 입력하셨습니다.")
		a = input("적용할 규칙을 선택하십시오 >>")
		return calc(a)
	
	if str(type(rule[a-1])) == "<class 'int'>" :
	
		print("이전에 선택했던 규칙을 선택하셨습니다.")
		a = input("적용할 규칙을 선택하십시오 >> ")
		return calc(a)
		
	for i in range(1,7) :
		if a == i : 
			rule[i-1] = 0
			for j in yrdice :
				if j == i : rule[i-1] += i
			
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
				if yrdice.count(i) == 3 and yrdice.count(j) == 2 : rule[8] = sum(yrdice)
				
	if a == 10 :
		rule[9] = 0
		if sorted(yrdice) == [1,2,3,4,5] :
			rule[9] = 30
		
	if a == 11 :
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
	
	while True :
		yourchoice = input(">> ")
		if yourchoice == '0' : quit() #1 > 0(프로그램 종료)
		
		if yourchoice == '1' : #1 > 1(주사위 굴리기)
			print("\n아래가 당신이 굴린 주사위입니다.")
			print(roll())
			print("\n0. 프로그램 종료\n1. 이대로 진행\n2. 변경할 주사위 선택")
			break
			
		else:
			print("[sys]잘못 입력하셨습니다.")
			
	while True :
		yourchoice = input(">> ")
		if yourchoice == '0' : quit() #1 > 1 > 0(프로그램 종료)
		
		if yourchoice == '1' : #1 > 1 > 1(이대로 진행)
			sheet()
			
			a = input("적용할 규칙을 선택하십시오 >> ")		
			calc(a)
			
			temp = 0
			for i in rule :
				if str(type(i)) == "<class 'int'>" :
					temp += 1
			
			if temp == 12 : 
				sheet()
				print("yacht dice game 이 끝났고 결과는 위와 같습니다.")
				return
				
			else : return game()
			
		if yourchoice == '2' : #1 > 1 > 2(변경할 주사위 선택)
			for i in range(2) :
				temp = 1
				riddice = []
		
				while temp != 0 :
					try :
						print("\n변경할 주사위를 선택해주세요(1-5)\n더이상 선택할 주사위가 없으면 0을 눌러주세요.")
						temp = int(input(">> "))
				
						if temp > 5 : print("[sys]잘못 입력하셨습니다.")
				
						elif riddice.count(temp) == 1 : print("중복된 숫자를 입력하셨습니다.")
					
						elif temp != 0 : riddice.append(temp)
			
					except:
						print("[sys]잘못 입력하셨습니다.")
				
				for dienum in riddice :
					yrdice[dienum - 1] = random.randrange(1,7)
				print("\n아래가 당신이 굴린 주사위입니다.")
				print(yrdice)
			
				if i == 0:
					print("\n0. 프로그램 종료\n1. 이대로 진행\n2. 변경할 주사위 선택")
					yourchoice = input(">> ")
					
					if yourchoice == '0' : quit()
					if yourchoice == '1' : break
					
			break
					
		else : print("[sys]잘못 입력하셨습니다.")
				
	sheet()
		
	a = input("적용할 규칙을 선택하십시오 >> ")	
	calc(a)
			
	temp = 0
	for i in rule :
		if str(type(i)) == "<class 'int'>" : temp += 1
		
	if temp == 12 :
		sheet()
		print("yacht dice game 이 끝났고 결과는 위와 같습니다.")
		return
			
	else :return game()
		
print("---------------------------------------")
print("              yacht v1.02")
print("              made by kim")
print("---------------------------------------")
print("0. 프로그램 종료\n1. 게임 시작")

while True:
	yc = input(">> ")
	if yc == '0' :
		break
	if yc == '1' :
		game()
		break
	else:
		print("[sys]잘못 입력하셨습니다.")