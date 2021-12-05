'''
** simplex
| This module performs the simplex method
| based on the given matrix.
'''
import numpy as np
import math as mt

'''
** simplex
| This function performs the simplex method.
- - -
** params
| - tableau: The initial tableau for the problem
| - is_max: A boolean value to determine if maximization/minimization is applied
| - problem: A boolean value to determine if a value d is returned
- - -
** returns
| - final_tableau: A matrix of the final tableau
| - basic_solution: A matrix of the basic solution
| - optimal: The maximum/minimum value
| - shipped_items: A matrix of the number of shipped items from a plant to a warehouse
'''
def simplex(tableau, is_max, problem):
    # ** Declaration
    nrow = np.shape(tableau)[0] # Store the tableau's row number.
    ncol = np.shape(tableau)[1] # Store the tableau's column number.
    brow = tableau[nrow - 1, :] # Store the bottom row of the tableau.
    basic_solution = [] # Store the final basic solution.
    shipped_items = [] # Store the number of shipped items.

    # Perform Simplex until the bottom row has no negative value.
    while (len(brow[brow < 0]) > 0):
        # Get the pivot column.
        pptc = min(np.where(brow == -max(abs(brow[brow < 0]))))[0]

        # -> Get the smallest time positive ratio for the pivot row.
        # -> Then, transform the negative values into infinity (invalid).
        ratio = [mt.inf if tableau[:, pptc][i] == 0 else tableau[:, ncol - 1][i] / tableau[:, pptc][i] for i in range(0, nrow - 1)]
        ratio = [mt.inf if num <= 0 or mt.isnan(num) else num for num in ratio]
        
        # Get the pivot row.
        filtered = [_ for _ in ratio if not mt.isinf(_)]
        pptr = None if len(filtered) == 0 or len(filtered) == len(ratio) else min(np.where(ratio == min(filtered)))[0]

        # If all test ratios are negative, return None.
        if pptr == None:
            return None
        
        # Normalize the pivot row.
        tableau[pptr, :] = tableau[pptr, :] / tableau[pptr, pptc]

        # Eliminate the other rows.
        for eptr in range(0, nrow):
            # Don't eliminate the pivot row.
            if eptr != pptr:
                tableau[eptr, :] = tableau[eptr, :] - (tableau[pptr, :] * tableau[eptr, pptc])
        brow = tableau[nrow - 1, :] # Update the bottom row.
    
    # Get the basic solution for maximization/minimization.
    if is_max:
        # The long line in the row index unlists the result, which is an array.
        basic_solution = [tableau[(np.array(np.where(tableau[:, i] == 1), dtype = int)[0])[0], ncol - 1] if len((tableau[:, i])[tableau[:, i] == 1]) == 1 and len((tableau[:, i])[tableau[:, i] == 0]) == nrow - 1 else 0 for i in range(7, ncol - 1)]

        # Store the number of shipped items.
        shipped_items = basic_solution[0:14]
    else:
        basic_solution = np.delete(tableau[nrow - 1, :], ncol - 2)

        # Store the number of shipped items.
        shipped_items = basic_solution[len(basic_solution) - 17:len(basic_solution) - 2]
    
    # Return a dictionary of the return values.
    return {
        'final_tableau' : tableau,
        'basic_solution' : basic_solution,
        'optimal' : basic_solution[len(basic_solution) - 1],
        'shipped_items' : np.array(shipped_items, dtype = float).reshape((3, 5))
    }

'''
** create_initial_tableau
| This is a helper function to create the initial tableau based
| on the data. This is problem-specific,  as it only helps in
| translating the data.
- - -
** params
| - m: A matrix of the problem's data set
| - is_max: A boolean value to determine if maximization/minimization is applied
- - -
** returns
| - tableau: The initial tableau for the problem
| - colnames: The column names for the initial tableau
'''
def create_initial_tableau(m, is_max):
    # Store the problem's initial tableau.
    tableau = []

    # Morph the minimization constraints.
    tableau = [[(1 if is_max else -1) if j >= (i * 5) and j <= (i * 5) + 4 else (-m[2][i] if is_max else m[2][i]) if j == 15 else 0 for j in range(0, 16)] for i in range(0, 3)]

    # Morph the maximization constraints.
    [tableau.append([(-1 if is_max else 1) if j in [i, i + 5, i + 10] else (m[0][i] if is_max else -m[0][i]) if j == 15 else 0 for j in range(0, 16)]) for i in range(0, 5)]

    # Morph the slack variables.
    [tableau.append([1 if j == i else 0 for j in range(0, 16)]) for i in range(0, 15)]

    # Morph the Z column.
    tableau.append([1 if i == 15 else 0 for i in range(0, 16)])

    # Morph the solution column.
    solution = m[1]
    solution.append(0)
    tableau.append(solution)

    # Return a dictionary (tableau and colnames).
    return { 'tableau' : np.array(tableau, dtype = float).transpose(),  'colnames' : ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14', 'x15', 'Z', 'Solution'] }

# Test the function here.
m = [[431, 332, 350, 450, 400],  [30, 29, 31, 35, 33, 26, 24, 23, 25, 27, 11, 13, 15, 20, 17], [1400, 400, 200]]
print(simplex(create_initial_tableau(m, False)['tableau'], False, False))