#Python - 01
#Q2. You will be given a list. You have to print a list whose 1st element should be largest and 2nd should be the smallest then the 3rd should be 2nd largest and 4th should be 2nd smallest and so on.
#Input Format:
#The first line will have space-separated elements of the list.
#Output Format:
#Print the required list.
#Sample Input 0:
#1 2 3 4 5 6
#Sample Output 0:
#6 1 5 2 4 3
# Python prog to illustrate the following in a list
def find_len(list1):
    length = len(list1)
    list1.sort()
    print(list1[length-1])
    print(list1[0])
    print(list1[length-2])
    print(list1[1])
    print(list1[3])
    print(list1[2])
 
# Driver Code
list1=[1, 2, 3, 4, 5, 6]
Largest = find_len(list1)
list.sort
print(list1)