#a built-in data type that stores set of values. it can store elements of the different types(integer,float,string etc)
marks=[34.5,45,23.4,"hello",98.89]
print(marks)
print(type(marks))
 #strings= immutable
 #list=  mutable
  #list_name[ starting_idx : ending_idx ] #ending idx is not in

"""marks = [87, 64, 33, 95, 76]

marks[ 1 : 4 ] is [64, 33, 95]

marks[ : 4 ] is same as marks[ O : 4]

marks[ 1 : ] is same as marks[ 1 : len(marks) ]

marks[ -3 : -1 ] is [33, 95]"""
tub=(2,4,5,4,1,2)
print(type(tub))
#tuple is immutable like string
tub1=(2,)
print(tub.index(1))
print(tub.count(2))
#wap to ask the user to enter names of their 3 fav movies and store them in list
movies=[]
movie1=input("enter movie 1:")
movie2= input("enter movie 2:")
movie3=input('enter movie 3:')
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)

#wap to check if a list contains a palindrome of elements. use copy() method

list1=[1,2,3,2,1]
list2=[1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("palindrom list")
else:
    print("not palindrom list1") 
