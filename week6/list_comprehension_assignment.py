##Write a program list_comprehension_assignment.py with separate functions for:

##printing a list of the full path to items in a directory
import os
def fullpath():
  dir=input("Enter the directory:")
  path=[os.path.abspath(x) for x in os.listdir(dir)]
  print("List of full path to items in directory \n",path)

 ##printing a list of the full path to items in a directory (excluding directories)
def excludedir():
    dir=input("Enter the directory:")
    exclude=[file for file in os.listdir(dir) if os.path.isfile(file)]
    print("list of the full path to items in a directory (excluding directories) \n",exclude) 

##printing the list of all .jpg and .png files in a directory
def printfiles():
  dir=input("Enter the directory:")
  lis=[file for file in os.listdir(dir) if file.endswith("jpg") or file.endswith("png")]
  print("list of all .jpg and .png files in the directory \n",lis)

##printing length of each word in a sentence.
def length_word():
   sentence=input("Enter a sentence:")
   length=[len(word) for word in sentence.split(" ")]
   print("Length of each word \n",length)

    
#to print all of the words in a string that have less than 4 letters
def lessthan4_word():
    string=input("Enter the string:")
    words=[word for word in string.split(" ") if len(word)<4]
    print("All words with length less than 4 \n",words)

    
##printing the number of spaces in a string
def spaces():
    sentence=input("Enter the sentence:")
    count=len([x for x in sentence if x is " "])
    print("Number of spaces in string: ",count)


##removing vowels from a string and printing it
def remvowels():
   string=input("Enter the string:")
   # string=list(set([string.replace(x,"") for x in string if x in ("a","e","i","o","u") ]))
   s=''.join([x for x in string if x not in ("a","e","i","o","u")])
   print("String after removing vowels \n",s)

def main():
   fullpath()
   excludedir()
   printfiles()
   length_word()
   lessthan4_word()
   spaces()
   remvowels()
main()   
