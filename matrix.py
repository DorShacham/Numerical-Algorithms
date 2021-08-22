from copy import deepcopy


#auxeliri function, parsing the indexes
  # row and col are tuple indecatig the range, or int if meens a single row or
  # col. empty tuple means the entire range
def getIndex(matrix,row,col):
    if (type(row) == int):
      first_row = row
      last_row = row
    elif (type(row) == tuple):
      if(len(row) == 0):
       first_row = 0
       last_row = matrix.row - 1
      if(len(row) == 1):
       first_row = row[0]
       last_row = matrix.row - 1
      if(len(row) == 2):
       first_row = row[0]
       last_row = row[1]
    else:
      raise Exception("Matrix Exception: dimention error")
   
    if (type(col) == int):
      first_col = col
      last_col = col
    elif (type(col) == tuple):
      if(len(col) == 0):
       first_col = 0
       last_col = matrix.col - 1
      if(len(col) == 1):
       first_col = col[0]
       last_col = matrix.col - 1
      if(len(col) == 2):
       first_col = col[0]
       last_col = col[1]
    else:
     raise Exception("Matrix Exception: dimention error")
    return (first_row,last_row,first_col,last_col)


class matrix:
  def __init__(self,source):
        self.row = len(source)
        self.col = len(source[0])
        self.data = source
        for row in source:
            if self.col != len(row):
                raise Exception("Matrix Exception: dimention error")

  def size(self):
    return (self.row,self.col)
  def hight(self):
    return (self.row)
  def width(self):
    return (self.col)
  def print(self):
    for row in self.data:
      for obj in row:
        if int(obj)==float(obj):
          print("%4.1d" %obj, end=" ")
        else:
          print("%4.1f" %obj, end=" ")
      print()
  
  # row and col are tuple indecatig the range, or int if meens a single row or
  # col. empty tuple means the entire range
  def __call__(self, row,col): 
    (first_row,last_row,first_col,last_col) = getIndex(self,row,col)
    new_mat = []
    for r in range(first_row,last_row+1):
      new_row = []
      for c in range(first_col,last_col+1):
        new_row.append(self.data[r][c])
      new_mat.append(new_row)
    return(matrix(new_mat))
  
  def edit(self,soruce,row,col):
    if type(soruce) != type(self): # i.e not a matrix
      soruce = matrix([[soruce]])
    (first_row,last_row,first_col,last_col) = getIndex(self,row,col)
    if (soruce.row != (last_row - first_row + 1)) or (soruce.col != (last_col - first_col + 1)):
      raise Exception("Matrix Exception: dimention error")
    for r in range(first_row,last_row+1):
      for c in range(first_col,last_col+1):
        self.data[r][c] = soruce.data[r-first_row][c-first_col]
    return self

# append to the self matrix the source matrix, return the new matrix
  def appendBelow(self,source):
    if (self.col != source.col):
      raise Exception("Matrix Exception: dimention error")
    self.data += deepcopy(source.data)
    self.row += source.row
    return self

  def appendRight(self, source):
    if (self.row != source.row):
      raise Exception("Matrix Exception: dimention error")
    for r in range(self.row):
      self.data[r] += deepcopy(source.data[r])
    self.col += source.col
    return self

# returned the transposed matrix 
  def transpose(self):
    new_mat = []
    for c in range(self.col):
      new_row = []
      for r in range(self.row):
        new_row.append(self.data[r][c])
      new_mat.append(new_row)
    return (matrix(new_mat))

  ## add for each
  def __add__(self,other):
    if (self.size() != other.size()):
      raise Exception("Matrix Exception: dimention error")
    new_mat = []
    for r in range(self.row):
      new_row = []
      for c in range(self.col):
        new_row.append(self.data[r][c]+other.data[r][c])
      new_mat.append(new_row)
    return (matrix(new_mat))

  def __sub__(self,other):
    return(self + (-1)*other)

  ## mult for each
  def __pow__(self,other):
    if (self.size() != other.size()):
      raise Exception("Matrix Exception: dimention error")
    new_mat = []
    for r in range(self.row):
      new_row = []
      for c in range(self.col):
        new_row.append(self.data[r][c]*other.data[r][c])
      new_mat.append(new_row)
    return (matrix(new_mat))
  
  def __mul__(self,other):
    if type(other) != type(self): # i.e not a matrix
      return(self**uniform(other,self.row,self.col))
    
    else:
      if(self.col != other.row):
        raise Exception("Matrix Exception: dimention error")
      new_mat = uniform(0,self.row,other.col)
      for r in range(new_mat.row):
        for c in range(new_mat.col):
          sum = 0
          for k in range(self.col):
            sum += self.data[r][k]*other.data[k][c]
          new_mat.edit(sum,r,c)
      return new_mat

  def __rmul__(self,other):
    if type(other) != type(self): # i.e not a matrix
      return(self**uniform(other,self.row,self.col))
  
  # return the Formbinus norm of the matrix
  def norm(self):
    sum = 0
    for r in range(self.row):
      for c in range(self.col):
        sum += self.data[r][c]**2
    return sum**(1/2)

# return a tuple of the max element and a tuple of its position
  def max(self):
    m = self.data[0][0]
    arg = (0,0)
    for r in range(self.row):
      for c in range(self.col):
        if self.data[r][c] > m:
          m = self.data[r][c]
          arg = (r,c)
    return (m,arg)

  def maxAbs(self):
    m = abs(self.data[0][0])
    arg = (0,0)
    for r in range(self.row):
      for c in range(self.col):
        if abs(self.data[r][c]) > m:
          m = abs(self.data[r][c])
          arg = (r,c)
    return (m,arg)

  def det(self):
    if self.row != self.col:
      raise Exception("Matrix Exception: Determinent only defiend for sqrue matresices")
    from lu import lu
    (L,U,P) = lu(self)
    det = 1
    for i in range(self.row):
      det *= U.data[i][i]

      for i in range(self.row):
        if P.data[i][i] == 1:
          continue
        else:
          pivot = P((i,),i).maxAbs()
          pivot = pivot[1][0] + i #takes the row from the arg
          tmp_line = P(pivot,(0,))
          P.edit(P(i,(0,)),pivot,(0,))
          P.edit(tmp_line,i,(0,))
          det *= (-1)
    return det

         

    


def uniform(value,row_num,col_num):
  mat = []
  for r in range(row_num):
    row = []
    for c in range(col_num):
      row.append(value)
    mat.append(row)
  return(matrix(mat))


def ones(size):
  return(uniform(1,size,size))

def zeros(size):
  return(uniform(0,size,size))

def eye(size):
  mat = zeros(size)
  for i in range(size):
    mat.data[i][i] = 1
  return mat

