# Defining a new empty matrix for final result
new_matrix = []

# Defining square matrix function

def square_matrix_simple(matrix=[]):
# Iterating into inputted matrix row 
    for i in matrix:
# New empty list to store new row on it 
            new_row=[]
# Iterating into numbers in row 
            for j in i:
                result = j ** 2
# Add the row to new_row list
                new_row.append(result)
# Adding new_row into the new_matrix 
            new_matrix.append(new_row)
    return new_matrix  
        
        
       



