#Python Program to implement Bubble Sort
#Program 1
list=eval(input("Enter the list of Elements: "))
size=len(list)
for i in range(size):
  for j in range(0,size-i-1):
    if list[j]>list[j+1]:
       list[j],list[j+1]=list[j+1],list[j]
print("sorted list.",list)
