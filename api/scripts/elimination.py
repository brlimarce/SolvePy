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
| This function performs the method of Gauss-Jordan Elimination.
- - -
** params
| m: A matrix of n x m size
- - -
** returns
| - solution: An array of the system's solution
| - m: The identity matrix after elimination
'''
def gauss_jordan(m):
    # ** Declaration
    nrow = len(m) # Stores the number of rows.

    # 'pptr' serves as the pointer of the pivot row.
    for pptr in range(nrow):
        # Pivot if pptr isn't pointing to the last row.
        if pptr != (nrow - 1):
            m = pivot(m, pptr) # Employ partial pivoting.
            if m is None:
                return None
        # Normalize the pivot row.
        m[pptr, :] = m[pptr, :] / m[pptr, pptr]

        # Eliminate the other rows.
        for eptr in range(nrow):
            if eptr != pptr:
                m[eptr, :] = m[eptr, :] - (m[pptr, :] * m[eptr, pptr])
    # Return a dictionary (solution and identity matrix).
    return { 'solution' : m[:, len(m[0]) - 1], 'resulting_matrix' : m }

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
    # Pivot only if PE is 0.
    if m[pptr, pptr] == 0:
        # Get the row.
        temp_row = m[pptr:len(m), pptr]

        # -> Find the row of the maximum number.
        # -> This depends if all values are negative or not.
        row = np.where(m[:, pptr] == max(abs(temp_row[temp_row != 0])))[0][0] if len(temp_row) == len(temp_row[temp_row < 0]) else np.where(m[:, pptr] == max(temp_row[temp_row != 0]))[0][0]
        
        # If the maximum value is 0, return None.
        if m[row, pptr] == 0:
            return None
        m[[row, pptr]] = m[[pptr, row]] # Swap the rows in the matrix.
    return m # Return the updated matrix.