import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
def dot_product(vector_one, vector_two):
    """
        Calculates the dot product of two vectors.
    """
    if len(vector_one) != len(vector_two):
            raise(ValueError, "Cannot calculate dot-product of two vectors with different sizes.")

    dotProduct = 0
    for i in range(len(vector_one)):
        dotProduct += vector_one[i]*vector_two[i]
    
    return dotProduct
    
    
class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        
        # 1 x 1 Matrix
        if self.h == 1:
            return self.g[0]
        
        # 2 x 2 Matrix
        if self.h == 2:
            
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            
        return a*d-b*c
        
        
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        
        #For trace of matrix
        traceOfMat = 0
        
        for i in range(self.w):
             traceOfMat += self.g[i][i]
                
        return traceOfMat

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        
        
        ### For inverse of matrix
        
        #  1x1 matrix          
        if (self.w == 1 and self.h==1):
            return Matrix(1/self.g[0][0])
  
        
        #  2x2 matrix
        
        if(self.w == 2 and self.h==2):
            
            #For detA
            determinantOfMat = self.determinant()
            #For trA
            traceOfMat = self.trace()
            #For  I
            identityMat = identity(self.h)
            
            #For trA*I
            traceOfMat_I = traceOfMat * identityMat
            
            #For trA*I-A
            changeMatrix = traceOfMat_I - self
            
            #For (1/detA)*[trA*I-A]
            inverseOfMat = (1.0/determinantOfMat)*changeMatrix
        
        return inverseOfMat

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        
        #For transpose of matrix
        matrix_trans = zeroes(self.w,self.h)
        for r in range(self.h):
            for c in range(self.w):
                matrix_trans.g[c][r] = self.g[r][c]
    
        return matrix_trans

    def is_square(self):
        #square matrix
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        
        #Sum of matrices
        sumOfMat = zeroes(self.h, self.w)
        for r in range(self.h):
            for c in range(self.w):
                sumOfMat.g[r][c] = self.g[r][c]+other.g[r][c]
        
        return sumOfMat
    
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        
        #negation of matrix
        negOfMat = zeroes(self.h, self.w)
        for r in range(self.h):
            for c in range(self.w):
                negOfMat.g[r][c] = -self.g[r][c]
        
        return negOfMat

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        
        #For substraction of matrices
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same")
        
        diffOfMat = zeroes(self.h, self.w)
        for r in range(self.h):
            for c in range(self.w):
                diffOfMat.g[r][c] = self.g[r][c]-other.g[r][c]
        
        return diffOfMat

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        #for multiplication of matices
        grid = zeroes(self.h, other.w)
        
        for x in range(self.h):
            for y in range(other.w):
                for z in range(other.h):
                    grid[x][y] += self.g[x][z] * other.g[z][y]
        return grid
    

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            #   
            # TODO - your code here
            #
            #multiplication of matrix with number
            product = zeroes(self.h, self.w)
            for r in range(self.h):
                for c in range(self.w):
                    product.g[r][c] = self.g[r][c]*other
            return product