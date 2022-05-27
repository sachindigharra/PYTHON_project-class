with open('sachin.txt','r') as f:
    data =f.read().split(' ')
    lower_alpha=0
    upper_alpha=0
    digit=0
    specialChar=0
    for i in data:
        for ch in i:
            if ( (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z') ):
                if (ch >= 'a' and ch <= 'z'):
                    lower_alpha+=1
                else:
                    upper_alpha+=1
            elif(ch >= '0' and ch <= '9'):
                    digit+= 1
		    else:
                    specialChar+=1