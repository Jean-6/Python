"""
Python - Condition : palindrome
Lire un mot sur l'entrée standard.

Si ce mot est un palindrome, affichez "<mot> est un palindrome".

Sinon affichez "<mot> n'est pas un palindrome"

Astuce : convertissez d'abord la chaîne de caractères tout en minuscules.


"""

def main() :
		 	 	  	 	  		 		  
    check=True		 	 	  	 	  		 		  
    word=input("")		 	 	  	 	  		 		  
    word1=word.lower()		 	 	  	 	  		 		  
    inverted_word=word1[::-1]		 	 	  	 	  		 		  
    cpt=0		 	 	  	 	  		 		  
    if word1 :		 	 	  	 	  		 		  
        while cpt<len(word1):		 	 	  	 	  		 		  
            if word1[cpt]!=inverted_word[cpt]:		 	 	  	 	  		 		  
                #print(word1[cpt]+""+inverted_word[cpt])		 	 	  	 	  		 		  
                check=False		 	 	  	 	  		 		  
            cpt=cpt+1		 	 	  	 	  		 		  
		 	 	  	 	  		 		  
    if check==True:		 	 	  	 	  		 		  
        print("{} est un palindrome".format(word))		 	 	  	 	  		 		  
    else:		 	 	  	 	  		 		  
        print("{} n'est pas un palindrome".format(word))		 	 	  	 	  		 		  
		 	 	  	 	  		 		  

if __name__ == "__main__":
    main()