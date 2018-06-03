import sys
from random import randint

def main():
	upperLetter="ABCDEFGHIJOKLMNOPQRSTVWXYZ"
	lowerLetter="abcdefghijklmnopqrstvwxyz"
	numeric="1234567890"
	special="!#$%&()*-+,.-;"
	password=""
	
	print("Give me the password length: ")
	length=int(input())
	while(length!=0):
		rand=randint(1,4)
		if(rand==1):
			password+= upperLetter [ randint(0, (len(upperLetter) -1)) ]
		elif(rand==2):
			password+= lowerLetter [ randint(0, (len(lowerLetter) -1)) ]
		elif(rand==3):
			password+= numeric [ randint(0, (len(numeric) -1)) ]
		elif(rand==4):
			password+= special [ randint(0, (len(special) -1)) ]
		length=length-1


	print("Your password: ", password )
if __name__ == "__main__":
    main()
