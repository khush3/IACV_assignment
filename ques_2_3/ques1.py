from matrix import a,b
import numpy as np

# Question 2.a
a_transpose = a.T
b_transpose = b.T

# Question 2.b : 
# Matrix a is singular matrix hence it throws and error

# a_inverse = np.linalg.inv(a)
b_inverse = np.linalg.inv(b)

# Question 2.c : Follows commutative property 

add_1 = a + b
add_2 = b + a 

# Question 2.d : Doesnt follow commutative property

sub_1 = a - b
sub_2 = b - a 

# Question 2.e : Doesnt follow commutative property

mul_1 = np.matmul(a, b,)
mul_2 = np.matmul(b, a,) 

# Question 2.f : write here

c1 = 2
a_scalar = a * c1
b_scalar = b * c1

c2 = 0.4
a_scalar = a * c2
b_scalar = b * c2

# Question 2.g : Element by element multiplication

elementwise_1 = np.multiply(a,b)
elementwise_2 = np.multiply(b,a)

# Question 2.h  : Find the specific value of X 

# x1,y1 = np.where(a == 134)
# print(f'In matrix a, found 134 at : [{x1[0]},{y1[0]}]' )


# x2,y2 = np.where(b == 134)
# print(f'In matrix b, found 134 at : [{x2[0]},{y2[0]}]' )

# Question 2.i  : Find the specific value of X and replace it

birthday = 709
a[a == 134] = birthday
print(a)

b[b == 134] = birthday
print(b)

