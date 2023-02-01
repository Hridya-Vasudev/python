#write a program to accept two values from user and retursntheirmproduct only if the product is equal to or less than 1000 else returs their sum
x=int(input("Enter a number :"))
y=int(input("Enter a number :"))
z=x*y
if z <= 1000:
    print(z)
    
else:
    print(x+y)

#write a program remove chars from a string startin from zero up to n and return a new srng
x="chemical"
print(x[4:])

#write a program to accept a strin from user and dsply chr that are present at an even index num
a=str(input("enter a string :"))
print(a[::2])

#write a program to itrate the first 10 numbers and print the sum of the current num and the previous num
i=0
while i < 10:
    print("current number is:",i)
    
    print("sum is:",i+i)
    i=i+1
#write a program to find the numbers in the given list which are divisible by 5
num = [10,20,33,45,36,46,55]
for x in num:
  if x%5==0:
      print(x)

#write a prpgrame to count howmany times a sub string "emma " occuers in the given string
str="Emma is a good developer. Emma is a writer"
d=str.count("Emma")
print(" Emma appeard",d,"times")

#write a program to get a new list from the first list and second list, the odd number frm first list and even number from second list
list1=[10,20,25,30,35]
list2=[40,45,60,75,90]
newlist=[]
for x in list1:
    if x%2!=0:
        newlist.append(x)
       
for y in list2:
    if y%2==0:
        newlist.append(y)
print(newlist)

#write a function which return true if the first and last element is same or return false
nlist=[10,20,30,40,10]
nlist2=[10,20,40,50,30]
def first_last_same(nlist,nlist2):
  if nlist[0]==nlist[-1]:
    print("on the list:",nlist)
    print("result is true",True)
  else:
    print("on the list:",nlist)
    print("result is false",False)
  if nlist2[0]==nlist2[-1]:
    print("on the list:",nlist2)
    print("result is true",True)
  else:
    print("on the list:",nlist2)
    print("result is false",False)
  return
first_last_same(nlist,nlist2)


#print the following pattern 1
                            #22
                            #333 up to 5
for x in range(1,6):
    for y in range(1,x+1):
        print(x,end='')
    print(end='\n')


#checking a number is paliandrome or not

number=int(input("Enter the number:"))
temp=number
reverse=0
while temp>0:
    digit=temp%10
    reverse=(reverse*10)+digit
    temp=temp//10
if number==reverse:
    print('yes it is a paliandrome')
else:
     print('no it is not a paliandrome')



#extracting the digits from a number and reverse it with space bw the numbers
num=int(input('enter a number:'))
result=[]
while num>0:
    result.append(num%10)
    num=(num-num%10)//10
print(*result)


#multiplication table from 1 to 10
for i in range(1,11):
    print()
    for y in range(1,11):
        print(i*y,end='\t')




#print downward half pyramid wit *

for i in range(5,0,-1):
    print('*'*i,end='')
    print('\t')


#exponent(base,exp) function
def exponent(base,exp):
    result=1
    for i in range(exp):
        result=result*base
    return result
base=int(input("enter the base:"))
exp=int(input("enter the exponent:"))
print(base,"rases to the power of",exp,"is",exponent(base,exp))


#income tax calculation
income=float(input("enter your annual income:"))
income=round(income,2)
tax=0.0
if(income<=100000):
    tax=0
elif income<=200000:
    tax=(income-100000)*0.10
else:
    tax=10000+(income-200000)*.20
print("income tax:",tax)






