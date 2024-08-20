from array import*
student_data = [[90,89,30,27,90], [23,45,67,89,90], [12,23,45,67,81], [13,56,78,14,45], [34,65,12,11,10]]

# Traversing the element in 2D (two dimensional)

# write a program to traverse every element of the two-dimensional array in Python.

# Use for loop to print the entire elements of the two dimensional array.
#for x in student_data:
    #print(x) # prints the matrix
    #for i in x:
       # print(i, end=',') # prints all elements in 2d array

# Insert elements in a 2D (Two Dimensional) Array
# Write a program to insert the element into the 2D (two dimensional) array of Python. 
#import all packages related to the array should be done on top of the programme

# before inserting element into the array
#print("before inserting elemnts into the array")
#print(student_data)

# # Use the insert() function to insert the element that contains two parameters. 
#student_data.insert(2, [100,200,300,400,500])
# for i in student_data:
#    for j in i:
#        print(j, end=',')

# Update elements in a 2 -D (Two Dimensional) Array
#print("before updating the element in array")
#print(student_data)

#student_data[0] = [120,160,200,6000,700]
#student_data[1] = [1100,3412,2000,4000,4500]
#for i in student_data:
#    for j in i:
#        print("after updating elements in a 2d array")
#        print(j, end=',')

# Delete values from a 2D (two Dimensional) array in Python
#del(student_data[0][4])
#del(student_data[1])
#print(len(student_data))
#for i in student_data:
#    for j in i:
#        print(j, end=' ')

# Write a program to print the sum of the 2-dimensional arrays in Python.

def two_d_matrix(m, n): # define the function  
    Outp = []  # initially output matrix is empty  
    for i in range(m): # iterate to the end of rows  
        row = []  
        for j in range(n): # j iterate to the end of column  
            num = int(input(f"Enter the matrix [{0}][{j}]"))  
            row.append(num) # add the user element to the end of the row  
        Outp.append(row) # append the row to the output matrix  
    return Outp      
  
def sum(A, B): # define sum() function to add the matrix.  
    output = [] # initially, it is empty.  
    print("Sum of the matrix is :") 
    for i in range(len(A)): # no. of rows  
        row = []  
        for j in range(len(A[0])): # no. of columns  
              
            row.append(A[i][j] + B[i][j]) # add matrix A and B  
        output.append(row)  
    return output    # return the sum of both matrix  
  
m = int(input("Enter the value of m or Row\n")) # take the rows  
n = int(input("Enter the value of n or columns\n")) # take the columns  
  
print("Enter the First matrix ") # print the first matrix  
A = two_d_matrix(m, n) # call the matrix function  
print("display the first (A) matrix")  
print(A) # print the matrix  
  
print("Enter the Second (B) matrix ")  
B = two_d_matrix(m, n) # call the matrix function  
print("display the Second (B) matrix")  
print(B) # print the B matrix  
  
s= sum(A, B) # call the sum function  
print(s) # print the sum of A and B matrix.  

