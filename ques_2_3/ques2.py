import numpy as np
import cv2

lenna = 'images/lenna.jpg'
cameraman = 'images/cameraman.jpg'

class Assignment():

    def __init__(self, a,b):
        self.a = cv2.imread(a,0)
        self.b = cv2.imread(b,0)
        self.i = 0

    def show_images(self,a,b):
        cv2.imshow('a '+str(self.i),a)
        cv2.imshow('b '+str(self.i),b)
        self.i += 1

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def transpose(self):
        # Question 3.a : Transpose of  images
        lenna_transpose = self.a.T
        camera_transpose = self.b.T
        return lenna_transpose,camera_transpose

    def inverse(self):
        # Question 3.b : Inverse of  images
        lenna_inv = np.linalg.inv(self.a) 
        camera_inv = np.linalg.inv(self.b)
        return lenna_inv , camera_inv
    
    def add(self):
        # Question 3.c : Addition of images (both)
        add_1 = self.a + self.b
        add_2 = self.b + self.a 
        return add_1,add_2

    def sub(self):
        # Question 3.d : Subtraction of images (both)
        sub_1 = self.a - self.b
        sub_2 = self.b - self.a 
        return sub_1,sub_2

    def mul(self):
        # Question 3.e : Multiplication of images
        mul_1 = np.matmul(self.a, self.b)
        mul_2 = np.matmul(self.b, self.a)
        return mul_1,mul_2

    def mul_scalar(self,c):
        # Question 3.f 2.g: Multiplication of images by scalar greater and less than 1
        a_scalar = self.a.astype(int) * c
        a_scalar = np.clip(a_scalar,0,255).astype(np.uint8)

        b_scalar = self.b.astype(int) * c
        b_scalar = np.clip(b_scalar,0,255).astype(np.uint8)

        return a_scalar,b_scalar

    def elementwise_mul(self):
        # Question 2.h : Element by element multiplication
        elementwise_1 = np.multiply(a,b)
        elementwise_2 = np.multiply(b,a)
        return elementwise_1,elementwise_2

    def value_finder(self,key):
        # Question 2.i 2.j  : Find the specific value of X 
        x1,y1 = np.where(a == key)
        print(f'In matrix a, found {key} at : [{x1[0]},{y1[0]}]' )
        
        x2,y2 = np.where(b == key)
        print(f'In matrix b, found {key} at : [{x2[0]},{y2[0]}]' )

    def find_and_replace(self, key, replace_by):
        # Question 2.k  : Find the specific value of X and replace it
        x1,y1 = np.where(a == key)
        for c,i,j in enumerate(zip(x1,y1)):
            a[i][j] = replace_by
            print(f'In matrix a, replaced {key} at : [{i+1},{j+1}]' )
        print(f'In matrix a, {key} found {c} times' )

        x2,y2 = np.where(b == key)
        
        for c,i,j in enumerate(zip(x2,y2)):
            print(f'In matrix b, replaced {key} at : [{i+1},{j+1}]' )
        print(f'In matrix b, {key} found {c} times' )
            
        return a, b

class Operations(Assignment):
    
    def __init__(self,a,b):
        super().__init__(a,b)
        
    def greater_replace(self, key, val):
        self.a[self.a > key] = val
        self.b[self.b > key] = val
        return self.a,self.b
    
    def less_replace(self, key, val):
        self.a[self.a < key] = val
        self.b[self.b < key] = val
        return self.a,self.b
    
    def greater_less_replace(self, greater_key, greater_val, less_key, less_val):
        self.a[self.a > greater_key] = greater_val
        self.a[self.a < low_key] = low_val

        self.b[self.b > greater_key] = greater_val
        self.b[self.b < low_key] = low_val

        return self.a,self.b
            
if __name__ == "__main__":
    
    asg = Assignment(lenna,cameraman)
    a, b = asg.mul_scalar(2)
    op = Operations(lenna,cameraman)
    a , b = op.greater_replace(63,0)
    print(a)
    # asg.show_images(a,b)

    # a, b = asg.mul_scalar(0.5)
    # asg.show_images(a,b)



# Question 3.g : Division of images by scalar

# Question 3.h : Elementwise mul of images both




