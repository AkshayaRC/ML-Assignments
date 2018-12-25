##first function returns a list with 2-tuples. Each tuple consists of the order number, the product of the price per items and the quantity.
##The product should be increased by 10, if the value of the order is smaller than 100.00. (Must use lambda functions)
##Input list :

##Expected Output: [('34587', 163.8), ('98762', 284.0), ('77226', 108.85000000000001), ('88112', 84.97)]

##second function returns a list of two tuples with (order number, total amount of order). The same bookshop, but this time we work on a different list.
##The sublists of our lists look like this: [ordernumber, (article number, quantity, price per unit), ... (article number, quantity, price per unit) ]
##Input list:
##Expected Output: [[1, 678.3299999999999], [2, 494.46000000000004], [3, 364.79999999999995], [4, 492.57]]
from functools import reduce
def func1():
    input_list=[ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
           ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein",     3, 24.99]]
    output_list=list(map(lambda x:(x[0],(x[2]*x[3])+10) if (x[2]*x[3])<100 else (x[0],x[2]*x[3]),input_list))
    print("Order no., Product: \n",output_list)

def func2():
   input_list=[ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
           [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
           [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
           [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
   explist=list(map(lambda x:[x[0]] + list(map(lambda y:y[1]*y[2],x[1:])),input_list))
   output_list=list(map(lambda x:[x[0]] + [reduce(lambda y,z: y+z,x[1:])],explist))
   print("Order number, total amount of order: \n",output_list)
    


func1()
func2()
   
    
