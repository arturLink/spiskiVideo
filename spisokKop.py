#spisok=[]
#abc=['a', 'b', 'c']
#slovo="kokolad"
#slovo_list=list(slovo)
#print(slovo)
#print(slovo_list)
#while True :
	#print("1 add letter to a word")
	#print("2 link spiski")
	#print("3 to delete a letter from a word")
	#valik=int(input())
	#if valik==1:
		#a=input("Enter letter")
		#slovo_list.append(a)
		#print(f"Added {a}. New spisok", slovo_list)
	#elif valik==2:
		#slovo_list.extend(abc)
		#print(slovo_list)
	#elif valik==3:
		#a=input("Enter letter that is to be deleted")
		#n=slovo_list.count(a)
		#if n>0: 
			#for i in range(n):
				#slovo_list.remove(a)
		#else:
			#print("no letter")
	#print (slovo_list)

slovo="exhausted"
slovo_list=list(slovo)
print(slovo_list, slovo)
spisk1=["GoOd","NICE","best","321","abc123"]
spisk2=["noice","NotSoNoice"]
spisk3=[22,11,78,1,2,3]
print(spisk1)
print(spisk2)
print(spisk3)
while 1:
	print("Press 1 to add up both lists")
	print("Press 2 to repeat lists")
	print("Press 3 to sort the 3rd list")
	print("Press 4 to know the length of the list")
	print("Press 5 to split the words")
	print("Press 6 to make the first letter capital")
	print("Press 7 to make the whole list not in capital letters")
	print("Press 8 to make the whole list in capital lettes")
	print("Press 9 to chech if the words are strating in capital letters")
	print("Press 10 to fill empty space with a symbol")

	dec=int(input("Wanna know stuff about the list?: "))
	if dec==1:
		spisk3=spisk1+spisk2
		print(spisk3)
	elif dec==2:
		dec1=int(input("Which list do you want to be repeated? 1 or 2: "))
		a=int(input("How much times should the programm repeat the list?: "))
		if dec1==1:
			spiskC=spisk1*a
			print(spiskC)
		elif dec1==2:
			spiskC=spisk2*a
			print(spiskC)
	elif dec==3:
		spisk3.sort()
		print(spisk3)
	elif dec==4:
		print(len(spisk1))
	elif dec == 5:
		print(slovo.split())
	elif dec == 6:
		print(slovo.capitalize()) 
	elif dec == 7:
		print(slovo.lower()) 
	elif dec == 8:
		print(slovo.upper())
	elif dec == 9:
		if slovo.istitle()==True: 
			print("There is a capital letter")
		else:
			print("There is no capital letter")
	elif dec == 10:
		print(slovo.ljust(20,"/"))
	else:
		print("You can press only number from 1-10")
