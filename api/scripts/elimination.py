'''
** elimination
| This module contains the functions for
| solving the system using Gaussian and
| Gauss-Jordan elimination.
'''
import numpy as np

'''
** gaussian
| This function performs the method of Gaussian elimination.
- - -
** params
| m: A matrix of n x m size
- - -
** returns
| - solution: An array of the system's solution
| - m: The resulting matrix after forward elimination
'''
def gaussian(m):
    # ** Declaration
    nrow = len(m) # Stores the number of rows.
    solution = list(range(nrow)) # Stores the solution of the system.

    # ** Forward Elimination
    # 'pptr' serves as the pointer of the pivot row.
    for pptr in range(nrow):
        # Employ partial pivoting.
        m = pivot(m, pptr)

        # If m is None, return None.
        if m is None:
            return None
        
        # Eliminate the rows.
        for eptr in range(pptr + 1, nrow):
            # Subtract the pivot row (multiplied by a multiplier) from the eval row.
            m[eptr, :] = m[eptr, :] - ((m[eptr, pptr] / m[pptr, pptr]) * m[pptr, :])
    
    # ** Backward Substitution
    for _ in range(nrow - 1, -1, -1):
        solution[_] = (m[_, len(m[0]) - 1] - sum(m[_, _ + 1:nrow] * solution[_ + 1:nrow])) / m[_, _]
    
    # Return a dictionary (solution and matrix after forward elimination).
    return { 'solution' : solution, 'resulting_matrix' : m }
'''
** gauss_jordan
| <>
'''
def gauss_jordan(m):
    print('Gauss-Jordan')

'''
** pivot
| - This is a helper function to execute partial pivoting.
| - This excludes steps that are distinct in both methods.
- - -
** params
| - m: A matrix of n x m size
| - pptr: The pivot pointer
- - -
** returns
| m: The updated matrix after pivoting
'''
def pivot(m, pptr):
    # Find the row of the maximum number.
    row = np.where(m[:, pptr] == max(abs(m[pptr:len(m), pptr])))[0][0]
    
    # If the maximum value is 0, return None.
    if m[row, pptr] == 0:
        return None
    m[[row, pptr]] = m[[pptr, row]] # Swap the rows in the matrix.
    return m # Return the updated matrix.

# Test the function here.
m = np.array([[0.1, 7, -0.3, -19.3], [3, -0.1, -0.2, 7.85], [0.3, -0.2, 10, 71.4]])
print(gaussian(m))