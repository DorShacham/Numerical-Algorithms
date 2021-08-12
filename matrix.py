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
        print(obj, end=" ")
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
    (first_row,last_row,first_col,last_col) = getIndex(self,row,col)
    if (soruce.row != (last_row - first_row + 1)) or (soruce.col != (last_col - first_col + 1)):
      raise Exception("Matrix Exception: dimention error")
    for r in range(first_row,last_row+1):
      for c in range(first_col,last_col+1):
        self.data[r][c] = soruce.data[r-first_row][c-first_col]
    return self


  


         

    


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

