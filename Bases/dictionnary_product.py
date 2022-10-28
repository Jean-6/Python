"""
Produit de dictionnaires
Vous avez à votre disposition un dictionnaire (tableau associatif) nommé my_dict, et un second dictionnaire nommé correspondances, qui contient en clés toutes les valeurs de my_dict.

Créez un dictionnaire nommé results, qui contient le produit de my_dict par correspondances.

Par exemple, si :

my_dict contient "x":"y" et
correspondances contient "y":"z"
Alors results contiendra "x":"z"



L'algorithme a utiliser peut être le suivant : 

Pour chaque clé k de my_dict : 
      soit v la valeur associée à k dans my_dict
      si v est une clé dans correspondances :
           mettre la clé k avec comme valeur correspondances[v] dans results



"""


def main() :
   		 	 	  	 	  		 		  
    results={}		 	 	  	 	  		 		  
		 	 	  	 	  		 		  
    if my_dict:		 	 	  	 	  		 		  
        if correspondances:		 	 	  	 	  		 		  
            for key,value in my_dict.items():		 	 	  	 	  		 		  
                if value in correspondances:		 	 	  	 	  		 		  
                    results[key]=correspondances[value]


if __name__ == "__main__":
    main()