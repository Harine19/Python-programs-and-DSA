#Programs for questions 1-10 on Python strings

#Q1) Given a string of odd length greater than 7, form a string made of the middle three characters of the given string. 

s=input("Enter string with odd length more than 7:")
mid=len(s)//2
print(“New string :”,s[mid-1:mid+2])

#Q2) Given 2 strings s1,s2 create a new string by appending s2 in the middle of s1.

s1=input("Enter string 1 :")
s2=input("Enter string 2 :")
mid=len(s1)//2
print(“New string :”,s1[:mid]+s2+s1[mid:])

#Q3) Given 2 strings, s1,s2, return a new string made of the first,middle and last characters of each input string.

s1=input("Enter string 1 :")
s2=input("Enter string 2 :")
mid1=len(s1)//2
mid2=len(s2)//2
s3=s1[0]+s2[0]+s1[mid1]+s2[mid2]+s1[-1]+s2[-1]
print(“New string :”,s3)

#Q4) Arrange the characters in a string such that lowercase letters should come first followed by other characters.

s2=s3=""
s1=input("Enter string :")
for i in s1:
    if i.islower():
        s2+=i
    else:
        s3+=i
print(“New string :”,s2+s3)

#Q5) Given two strings s1,s2, create a mixed string consisting of the 1st character of s1 followed by the last character of s2 and so on. If there are leftover characters in any string they are placed at the end of the new string.

l3=[]
s3=""
s1=input("Enter string 1 :")
s2=input("Enter string 2 :")
l1=list(s1)
l2=list(s2)
l2.reverse()
for i in range(0,len(l1)):
    l3+=l1[i]
    for j in range(0,len(l2)):
        l3+=l2[j]
        l2.pop(j)
        break
l3+=l2
for k in (l3):
    s3+=k
print(“New string :”,s3)

#Q6) Given a string and a substring find all occurrences of substring in given string ignoring the case.

str=input("Enter string :")
sbstr=input("Enter substring :")
temp1=str.lower()
temp2=sbstr.lower()
n=temp1.count(temp2)
print("No of occurrences are :",n)

#Q7) Given a string, print the sum and average of the digits that appear in the string, ignoring all the other characters.

l=[]
tot=n=0
s=input("Enter string :")
l=list(s)
for i in l:
    if i.isdigit():
        tot=tot+int(i)
        n+=1
print("Sum is :",tot)
avg=tot/n
print("Average is :",avg)

#Q8) Perform a string characters balance test by reading 2 strings s1,s2. 2 strings are set to be balanced if all the chars in the string 1 are there in s2. The Character's position doesn't matter.

s1=input("Enter string 1 :")
s2=input("Enter string 2 :")
flag=0
for i in s1:
    if i in s2:
        continue
    else:
        flag=1
        break
if flag==0:
    print("Balanced")
else:
    print("Not balanced")

#Q9) Accept string from a user and display only those characters which are present at an even index number and if the even index has a space then print $ sign in that place.

l1=[]
s=input("Enter string :")
l=list(s)
for i in range(0,len(l)):
    if i%2==0 and l[i]==" ":
        l[i]="$"        
l2=[]
for i in range(0,len(l)):
    if i%2==0:
        l2+=l[i]
print(l2)


#Q10) Given a string and an integer number n, remove characters from the string starting from zero up to n and return a new string.

s=input("Enter string :")
n=int(input("Enter index :"))
print(s[n::])
