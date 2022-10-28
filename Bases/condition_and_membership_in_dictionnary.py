"""
Enoncé
Python - Condition : appartenance à un dictionnaire
Vous avez à votre disposition un dictionnaire (tableau associatif) nommé my_dict.

Lire un mot sur l'entrée standard en utilisant input()).

Si ce mot correspond à une clé de my_dict, affichez "<mot> vaut <valeur> dans my_dict".

Sinon affichez "<mot> n'est pas une cle de my_dict"
"""

def main() :
    check=False		 	 	  	 	  		 		  
    value=input("")		 	 	  	 	  		 		  
    for key in  my_dict:		 	 	  	 	  		 		  
        if value==key:		 	 	  	 	  		 		  
            check=True		 	 	  	 	  		 		  
            print("{} vaut {} dans my_dict".format(key,my_dict[key]))		 	 	  	 	  		 		  
		 	 	  	 	  		 		  
    if check==False:print("{} n'est pas une cle de my_dict".format(value))		 	 	  	 	  		 		  

if __name__ == "__main__":
    main()