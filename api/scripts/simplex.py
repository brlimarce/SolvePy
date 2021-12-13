'''
** simplex
| This module performs the simplex method
| based on the given matrix.
'''
import numpy as np
import math as mt
import re

from numpy.core.fromnumeric import var

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
| - is_max: A boolean value to determine if maximization/minimization is applied
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

        # If all test ratios are negative, return -1 (Output).
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
        for _ in range(0, ncol):
            if (tableau[:, _] == 1).sum() == 1 and (tableau[:, _] == 0).sum() == len(tableau) - 1:
                basic_solution.append(tableau[np.where(tableau[:, _] == 1)[0][0]][ncol - 1])
            else:
                basic_solution.append(0)
        # Store the number of shipped items.
        shipped_items = basic_solution[0:14]
    else:
        basic_solution = np.delete(tableau[nrow - 1, :], ncol - 2)

        # Store the number of shipped items.
        shipped_items = basic_solution[len(basic_solution) - 17:len(basic_solution) - 2]
    
    # Return a dictionary of the return values.
    return {
        'final_tableau' : tableau,
        'basic_solution' : basic_solution[0:len(basic_solution) - 1],
        'optimal' : basic_solution[len(basic_solution) - 2],
        'shipped_items' : np.array(shipped_items, dtype = float).reshape((3, 5)) if problem else None,
        'is_max' : is_max
    }

'''
** create_problem_tableau
| This is a helper function to create the initial tableau
| for the problem.
- - -
** params
| - m: A nested list of the problem's parameters
| - is_max: A boolean to identify if maximization/minimization is applied
- - -
** returns
| - initial_tableau: The initial tableau for the problem
| - colnames: The column names for the initial tableau
'''
def create_problem_tableau(m, is_max):
    tableau = [] # Store the problem's tableau.

    # Append the columns for minimization constraints.
    tableau = [[(1 if is_max else -1) if j >= (i * 5) and j <= (i * 5) + 4 else (-m[2][i] if is_max else m[2][i]) if j == 15 else 0 for j in range(0, 16)] for i in range(0, 3)]

    # Append the columns for maximization constraints.
    [tableau.append([(-1 if is_max else 1) if j in [i, i + 5, i + 10] else (m[0][i] if is_max else -m[0][i]) if j == 15 else 0 for j in range(0, 16)]) for i in range(0, 5)]

    # Append the columns for the slack variables.
    [tableau.append([1 if j == i else 0 for j in range(0, 16)]) for i in range(0, 15)]

    # Append the Z column.
    tableau.append([1 if i == 15 else 0 for i in range(0, 16)])

    # Append the solution column (Append the solution then 0).
    solution = m[1]
    solution.append(0)
    tableau.append(solution)

    # Return a dictionary of the result.
    return {
        'tableau' : np.array(tableau, dtype = float).transpose(),
        'colnames' : ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14', 'x15', 'Z', 'Solution']
    }

'''
** create_initial_tableau
| This is a helper function to create the initial tableau
| for the generic solver.
- - -
** params
| - m: A nested list of the problem's parameters
| - is_max: A boolean to identify if maximization/minimization is applied
- - -
** returns
| - initial_tableau: The initial tableau for the problem
| - colnames: The column names for the initial tableau
'''
def create_initial_tableau(m, is_max):
    # TODO: Implementation.
    print('Placeholder')

'''
** clean_problem_input
| This is a helper function to clean the data from
| the form of the problem-specific solver.
- - -
** params
| - demands: A list containing the number of demand for each warehouse
| - supplies: A list containing the number of supply for each plant
| - costs: A list containing the shipping cost from a plant to a warehouse
| - method: A string of the type of method of Simplex
- - -
** returns
| - All parameters in the correct data type.
| - problem_array: A matrix containing a problem-specific format
| - is_max: Returns True if it's maximization else False
'''
def clean_problem_input(demands, supplies, costs, method):
    return { 'problem_array' :  [[float(d) for d in demands], [float(c) for c in costs], [float(s) for s in supplies]], 'is_max' : True if method == 'maximization' else False}

'''
** clean_generic_input
| This is a helper function to clean the data from
| the form of the generic solver.
- - -
** params
| - equations: A list containing the objective function and constraints
| - method: The method to be used in Simplex
- - -
** returns
| - initial_tableau: The initial tableau based on the problem
| - is_max: Returns True if it's maximization else False
'''
def clean_generic_input(equations, method):
    # Determine if maximization or minimization is applied.
    is_max = True if method == 'maximization' else False
    constraint = '<=' if is_max else '>='
    initial_tableau = [] # Store the initial tableau.

    # Get the variables from the objective function.
    var_checker = re.compile('x[0-9]+')
    int_checker = re.compile('[0-9]+')
    variables = var_checker.findall(equations[0])

    # Get the terms and RHS from each equation.
    extracted = [] # Store the extracted terms and RHS.
    for _ in range(1, len(equations)):
        eq = equations[_].split(constraint) # Split the equation and RHS.
        terms = [t.replace(' ', '') for t in eq[0].split('+')] # Split the terms.

        # Check if the variables fit the objective function.
        for t in terms:
            if re.search(var_checker, t).group(0) not in variables:
                return None
        # Extract the terms and store them into a list.
        temp_array = [0 for _ in range(0, len(variables))]
        for _ in range(0, len(terms)):
            temp_array[int(re.search(int_checker, re.search(var_checker, terms[_]).group(0)).group(0)) - 1] = float(re.sub(var_checker, '', terms[_])) if re.sub(var_checker, '', terms[_]).isnumeric() else 1
        extracted.append([temp_array, float(eq[1])])
    
    # Get the numerical values from the objective function.
    constants = [] # Store the values from the objective function.
    for _ in (equations[0].split('=')[1]).split('+'):
        _ = re.sub(var_checker, '', _)
        constants.append(float(_))
    
    # Create a primal problem for maximization.
    if is_max and sum([e.count(constraint) for e in equations]) == len(equations) - 1:
        # Append the constraints in the initial tableau.
        for _ in range(0, len(extracted)):
            initial_tableau.append([(extracted[_])[0][i] if i >= 0 and i < len(variables) else (extracted[_])[1] if i == len(variables) + len(extracted) + 1 else 1 if i == _ + len(variables) else 0 for i in range(0, len(variables) + len(extracted) + 2)])
        # Append the last row.
        initial_tableau.append([-constants[i] if i >= 0 and i < len(variables) else 1 if i == len(variables) + len(extracted) else 0 for i in range(0, len(variables) + len(extracted) + 2)])

        # Create the column names.
        colnames = ['x' + str(_ + 1) if _ >= 0 and _ < len(variables) else 's' + str(_ - len(variables) + 1) for _ in range(0, len(variables) + len(extracted))]
        colnames.append('Z')
        colnames.append('Solution')
    
    # TODO: Create the dual problem.
    return { 'initial_tableau' : np.array(initial_tableau, dtype = float), 'is_max' : is_max, 'colnames' : colnames }

# Test the function here.
equations = ['Z = 150x1 + 175x2\r', '7x1 + 11x2 <= 77\r', '10x1 + 8x2 <= 80\r', 'x1 <= 9\r', 'x2 <= 6']
result = clean_generic_input(equations, 'maximization')
simplex(result['initial_tableau'], result['is_max'], False)