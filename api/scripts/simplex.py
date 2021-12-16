'''
** simplex
| This module performs the simplex method
| based on the given matrix.
'''
import numpy as np
import math as mt
import re

# ** Constants
# This contains the methods and constraint identifiers for the Simplex method.
METHOD_MAX = 'maximization'
METHOD_MIN = 'minimization'
CONSTRAINT_MAX = '<='
CONSTRAINT_MIN = '>='

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
    nrow, ncol = np.shape(tableau)[0], np.shape(tableau)[1]
    basic_solution, shipped_items = [], []
    brow = tableau[nrow - 1, :] # Store the bottom row of the tableau.

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
        pptr = min(np.where(ratio == min(filtered)))[0] if len(filtered) > 0 else None

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
        for _ in range(0, ncol - 1):
            if (tableau[:, _] == 1).sum() == 1 and (tableau[:, _] == 0).sum() == len(tableau) - 1:
                basic_solution.append(tableau[np.where(tableau[:, _] == 1)[0][0]][ncol - 1])
            else:
                basic_solution.append(0)
        
        # Store the number of shipped items.
        basic_solution = np.delete(tableau[nrow - 1, :], ncol - 2) # Delete the extra column.
        shipped_items = basic_solution[0:15]
    else:
        basic_solution = np.delete(tableau[nrow - 1, :], ncol - 2)

        # Store the number of shipped items.
        shipped_items = basic_solution[len(basic_solution) - 16:len(basic_solution) - 1]
    
    # Return a dictionary of the return values.
    return {
        'final_tableau' : tableau,
        'basic_solution' : basic_solution,
        'optimal' : basic_solution[len(basic_solution) - 1],
        'shipped_items' : np.array(shipped_items, dtype = float).reshape((3, 5)) if problem else None,
        'is_max' : is_max
    }

'''
** create_problem_tableau
| This is a helper function to create the initial tableau
| for the problem.
- - -
** params
| - demands: A list containing the number of demand for each warehouse
| - supplies: A list containing the number of supply for each plant
| - costs: A list containing the shipping cost from a plant to a warehouse
| - method: A string of the type of method of Simplex
- - -
** returns
| - initial_tableau: The initial tableau for the problem
| - colnames: The column names for the initial tableau
| - is_max: A boolean value to determine if maximization/minimization is applied
'''
def create_problem_tableau(demands, supplies, costs, method):
    # ** Declaration
    # This also contains the cleaned input from the form.
    parray = [[float(d) for d in demands], [float(c) for c in costs], [float(s) for s in supplies]]
    is_max = True if method == METHOD_MAX else False
    tableau, colnames = [], []

    # Check if the initial tableau is for maximization or minimization.
    if is_max:
        # Append the rows for maximization constraints.
        tableau = [[1 if j >= (i * 5) and j <= (i * 5) + 4 else parray[2][i] if j == 24 else 1 if j == 15 + i else 0 for j in range(0, 25)] for i in range(0, len(parray[2]))]

        # -> Append the rows for minimization constraints.
        # -> Multiply the coefficients by -1.
        [tableau.append([-1 if j in [i, i + 5, i + 10] else -parray[0][i] if j == 24 else 1 if j == 18 + i else 0 for j in range(0, 25)]) for i in range(0, len(parray[0]))]

        # Append the last row (objective function).
        tableau.append([-parray[1][_] if _ >= 0 and _ <= 14 else 1 if _ == 23 else 0 for _ in range(0, 25)])

        # Append the column names of the tableau.
        colnames = ['x' + str(_ + 1) for _ in range(0, 15)] + ['s' + str(_ + 1) for _ in range(0, 8)] + ['Z', 'Solution']
    else:
        # Append the columns for maximization constraints.
        tableau = [[-1 if j >= (i * 5) and j <= (i * 5) + 4 else parray[2][i] if j == 15 else 0 for j in range(0, 16)] for i in range(0, 3)]

        # Append the columns for minimization constraints.
        [tableau.append([1 if j in [i, i + 5, i + 10] else -parray[0][i] if j == 15 else 0 for j in range(0, 16)]) for i in range(0, 5)]

        # Append the columns for the slack variables.
        [tableau.append([1 if j == i else 0 for j in range(0, 16)]) for i in range(0, 15)]

        # Append the Z column.
        tableau.append([1 if i == 15 else 0 for i in range(0, 16)])

        # Append the solution column (Append the solution then 0).
        solution = parray[1] + [0]
        tableau.append(solution)

        # Append the column names of the tableau.
        colnames = ['s' + str(_ + 1) for _ in range(0, 8)] + ['x' + str(_ + 1) for _ in range(0, 15)] + ['Z', 'Solution']

    # Return a dictionary of the result.
    return {
        'tableau' : np.array(tableau, dtype = float).transpose() if not is_max else np.array(tableau, dtype = float),
        'colnames' : colnames,
        'is_max' : is_max
    }

'''
** create_initial_tableau
| This is a helper function to clean the data from
| the form of the generic solver.
- - -
** params
| - obj_function: A string containing the objective function
| - constraints: A list containing the constraints
| - method: The method to be used in Simplex
- - -
** returns
| - initial_tableau: The initial tableau based on the problem
| - colnames: The column names for the initial tableau
| - is_max: Returns True if it's maximization else False
'''
def create_initial_tableau(obj_function, constraints, method):
    # Determine if maximization or minimization is applied.
    is_max = True if method == METHOD_MAX else False
    initial_tableau, colnames = [], None

    # Get the variables from the objective function.
    var_checker, int_checker = re.compile('x[0-9]+'), re.compile('[0-9]+')
    variables = var_checker.findall(obj_function)

    # Get the terms and RHS from each equation.
    extracted = [] # Store the extracted terms and RHS.
    for _ in range(0, len(constraints)):
        # -> Split the equations and RHS via the constraint.
        # -> Then, split the terms in the equation.
        is_max_constraint = True if CONSTRAINT_MAX in constraints[_] else False
        eq = constraints[_].split(CONSTRAINT_MAX) if is_max_constraint else constraints[_].split(CONSTRAINT_MIN)
        terms = [t.replace(' ', '') for t in eq[0].split('+')]

        # Check if the variables fit the objective function.
        for t in terms:
            if re.search(var_checker, t).group(0) not in variables:
                return None
        # Extract the terms and store them into a list.
        temp_array = [0 for _ in range(0, len(variables))]
        for _ in range(0, len(terms)):
            temp_array[int(re.search(int_checker, re.search(var_checker, terms[_]).group(0)).group(0)) - 1] = (float(re.sub(var_checker, '', terms[_])) if is_max_constraint == is_max else -float(re.sub(var_checker, '', terms[_]))) if re.sub(var_checker, '', terms[_]).isnumeric() else (1 if is_max_constraint == is_max else -1)
        # Append the terms to the extracted array.
        extracted.append([temp_array, -float(eq[1]) if is_max_constraint == is_max and not is_max else float(eq[1])])
    
    # Get the numerical values from the objective function.
    constants = [] # Store the values from the objective function.
    for _ in (obj_function.split('=')[1]).split('+'):
        _ = re.sub(var_checker, '', _)
        constants.append(float(_))
    
    # Create the primal problem for maximization.
    if is_max:
        # Append the constraints in the initial tableau.
        [initial_tableau.append([(extracted[_])[0][i] if i >= 0 and i < len(variables) else (extracted[_])[1] if i == len(variables) + len(extracted) + 1 else 1 if i == _ + len(variables) else 0 for i in range(0, len(variables) + len(extracted) + 2)]) for _ in range(0, len(extracted))]

        # Append the last row.
        initial_tableau.append([-constants[i] if i >= 0 and i < len(variables) else 1 if i == len(variables) + len(extracted) else 0 for i in range(0, len(variables) + len(extracted) + 2)])

        # Create the column names.
        colnames = ['x' + str(_ + 1) for _ in range(0, len(variables))] + ['s' + str(_ + 1) for _ in range(0, len(constraints))] + ['Z', 'Solution']
    else:
        # Append the constraints and solution.
        [initial_tableau.append((extracted[_])[0] + [(extracted[_])[1]]) for _ in range(0, len(extracted))]
        initial_tableau.append(constants + [0])

        # Tranpose the initial matrix.
        initial_tableau = [list(row) for row in np.array(initial_tableau).transpose()]

        # Append the created array for the slack variables to the tableau.
        slack_array = [[1 if j == i else 0 for j in range(0, len(variables))] for i in range(0, len(variables))]
        slack_array.append([0 for _ in range(0, len(variables))])
        
        # Remake the matrix by inserting the slack variables.
        initial_tableau = [initial_tableau[_][0:len(constraints)] + slack_array[_] + [0 if _ >= 0 and _ < len(initial_tableau) - 1 else 1] + [initial_tableau[_][len(initial_tableau[_]) - 1]] for _ in range(0, len(initial_tableau))]
        
        # Append the column names of the tableau.
        colnames = ['s' + str(_ + 1) for _ in range(0, len(constraints))] + ['x' + str(_ + 1) for _ in range(0, len(variables))] + ['Z', 'Solution']
    return { 'initial_tableau' : np.array(initial_tableau, dtype = float), 'is_max' : is_max, 'colnames' : colnames }