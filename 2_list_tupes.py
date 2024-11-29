l = [ 1,233.45,"dsfs",True,5+7,344.256]

l[0]
l[5]
len(l)

#list ke ander kuch bhi rakh shakte ho in python 

l[0:5]#slicing is same as in string

l[::]
l[::2]
l[::-1]

s = "pwskills"
# l+s list + list

list(s)#list s a function --passing string,therfore it will make the list of substring of s

s[5]

l1 =list(s) +l
len(l1)
l1

type(l1[3])
l1[11]


# product to replicate
l2= [3,4,5]
l2*3

len(l2*3)

# append at end of the list
l2.append(6)
l2.append(6)
l2

v = "pwskills"
l2.append(v)
l2 #list ke ander string ay another list kuch bhi append kr shakte   

l1.append(l2) #appending --nesteed list w/o break
l1

# extend list by appending elements from the iterable.
# l.extend(4) not for int 
l.extend("sudh")# break into substring and store as list
l


l.extend([234,32,42])
l

# append store list/str in another list as it is but extend will be iterable and break them before storing
#both store in last index 

# data duplicacy is not a big issue in list


#at given position????? -- insert
l1.insert(1,"wea") #(index,things)
l1

l1.insert(2,[245,234,234])#2nd index pe as it is put kr dega w/o breaking it 
l1


l1.insert(-1,"vikash")#last second index and not at the last index
l1
# logically can say like given index pe datad do aur us index ka data ek position move kr do


l4 =[3,2,4,True,8,4,8,"Efv",35.225]
l4.pop()
l4.pop(3)#3rd index ko pop krega
l4

l4.remove(3)#first occurance of given values
l4
l4.remove(6654)#error


l4.append("sudha")
l4.append([3,24,54])
l4
l4.remove(3)#nested list me agar vale present h tho use directly remove nhi kr shakte
len(l4)
l4
l4[7].remove(3)#for removing from nexted loop
l4

#but for nested_string->in list , its not possible

l4.reverse()#original list ko hi reverse kr dega but by slicing its temporarly
l4


l4.sort()#only for list of int nd decimal

l5 =[25,215,245,223.25,5]
l5.sort()
l5
l5.sort(reverse=True)
l5#sort the original list


l6= ["vikash","bbf","safds","wfe"]
l6.sort()#sort if only string type #increasing order
l6

l6.sort(reverse=True)#decreasing order
l6

l6.index("vikash")

l6.count("bbf")


s = "sudh"
s[0]
s[0] = "a" #'str' object does not support item assignment

l7= [3,4,5 ]
l7[0] = 30
l7# list me eske items assign kr shakte h


#   ???  ==> mutability :: string is unmutable  whereas list is mutabel
  
s.replace("s","a")#temporarly and not in-place  ie. original is not change
# (mutability means inplace changes krna)
s

# ============tuples

t = (2,3,4,5,"sudha",45.565,45+25,[3,4,5])
type(t)
t
t[0]
t[-1]


# tuple vs list ?? mutability
l6[0] = "vianvks"
l6
t[0] = 565 # 'tuple' object does not support item assignment  -->its unmutabel 


# tuple does not have many built in function   there is only two functions for tuples -count and index 


t.count(5)
t.index("sudha")
len(t)


# dictionary 
s1={}# blank set == its dict
type(s1)
s2  = {1,2,35,554,54}
type(s2)#set

s3 = {122,55,25,"sudha",45 + 58j,55.25}
type(s3) 
s3
 
s4 = {122,55,25,"sudha",45 + 58j,55.25,[525,54,215]} # unhashable type ---set cannot store list but can store tuples and str


s5 = {122,55,25,"sudha",45 + 58j,55.25,(525,54,210)} 
s5 #tuples ko pehel dega uske and last m str
 
###????? bcs set can only store unutabel data types

#set removes duplicacy automaticaly
s6 = {1,2,3,1,2,3,4,1,2,3,1,1,4,2,3,2,"sudh","sudh","Sudh"}
s6 # set(pyton itself) is case-sensitive

l8 = [1,2,3,1,2,3,4,1,2,3,1,1,4,2,3,2,"sudh","sudh","Sudh"]
set(l8) #l8 =  set(l8)#but conver the l8  to the set  --temporary
#set as a buit in function is also availbale
l8

#  to remove duplaicauy in original list using set restoring the list property

l8 = list(set(l8))
l8

# set definition ::  unordered collection of unique elements

s6[0]#no indexing,no slicing--not subsciptable


s6.add(552)
s6.add(4)
s6
s6.remove(552)#vales provide krenge to delete
s6
# since no indexing in set so neither add/remove at specific postion 




# =====================
# .split()  to create the list from string 
g="egg,mango,bana"
gl = g.split(",")
gl


"a;b;c".split(";")


"The quick brown fox".split()

"abbaabba".split("ba")


#check existence in list 
"bob"  in g
"egg" in g


colors = ["red","yellow","green","blue"]
colors[1:3] = ["orange","mageta","aqua","blue"]
colors 


colors[1:4] = ["yellow","green"]
colors



#list comprehension --short hand of for loop

numbers = [1,2,3,4,5]
squares = [num **2 for num in numbers]
squares

# List of string numbers
str_num = ["1.3", "2.4", "5.234"]
# Convert strings to floats and then square each number
float_num = [float(num) ** 2 for num in str_num]
print(float_num)
formatted_float_num = [f"{num:.2f}" for num in float_num]
formatted_float_num