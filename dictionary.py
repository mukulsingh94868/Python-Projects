file = open("mukki2.txt","r")
x = file.read()

def mukki():
	word = word.lower()
	
	if word in x:
		return ["ha yaha hai"]
	elif word.title() in x:
	    return ["ha yaha h"]
	elif word.upper() in x:
	    return ["ha yaha hai"]    	
	   	

	else:
	    print("nahi hai")

word = input("enter the word:")

output = mukki()
print(output)