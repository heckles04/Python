def reverseString(text):
	word=""
	txet=""
	i=0
	while(i < len(text)):
		word+=text[i]
		if(text[i]==" " or i == len(text) -1):
			#word= txet
			txet=word + " " + txet
			word=""
		i+=1
	return txet

def main():
	text = "Do or do not but no try"
	print(reverseString(text) )



		
if __name__ == "__main__":
    main()
