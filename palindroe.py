#Varad dhat
# roll no:14, gr no: 11810137 
# To check for palindrome
def palindrome(num): 
 a=num[::-1] 
 if num==a: 
     print (num,"is palindrome") 
 else: 
     print (num,"is not palindrome") 
x=input("Enter to check palindrome:")
palindrome (x) 