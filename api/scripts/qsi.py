'''
** qsi
| This module finds the equations for each
| interval based on the data set using QSI.
'''
import numpy as np
from api.scripts import elimination as el

'''
** poly_qsi
| This function creates polynomials per intervals.
- - -
** params
| - xv: A vector containing the x values
| - yv: A vector containing the y values
| - x: Value to be evaluated using the appropriate polynomial
- - -
** returns
| - polynomials: All polynomials per interval
| - intervals: All intervals for each polynomial
| - intindex: The index of the chosen equation in the list
| - y: Approximate of f_n(x) using the appropriate function of an interval (based on x)
'''
def poly_qsi(xv, yv, x):
    # ** Declaration
    m = [] # Store the matrix from the conditions.
    n = len(xv) - 1 # Store the number of intervals.
    
    polynomials = [] # Store the polynomials per interval.
    intervals = [] # Store the intervals for each polynomial.
    intindex = 0 # Store the index of the equation in the list.
    y = 0 # Store the approximate value of f_n(x).
    
    # Add rows to the matrix for condition 1.
    for _ in range(1, n):
        coefficients = [xv[_] ** 2, xv[_], 1, yv[_]] # Store the coefficients.
        m.append(get_row(coefficients, n, 3 * (_ - 1)))
        m.append(get_row(coefficients, n, 3 * _))
    
    # Add rows to the matrix for condition 2.
    m.append(get_row([xv[0] ** 2, xv[0], 1, yv[0]], n))
    m.append(get_row([xv[n] ** 2, xv[n], 1, yv[n]], n, 3 * (n - 1)))

    # Add rows to the matrix for condition 3.
    for _ in range(1, n):
        # ** Declaration
        coefficients = [2 * xv[_], 1] # Store the coefficients.
        a1 = 3 * (_ - 1) # Store the small adder.
        a2 = 3 * _ # Store the big adder.

        # Add a row to the matrix for condition 3.
        m.append([coefficients[i - a1] if i >= a1 and i <= a1 + 1 else -coefficients[i - a2] if i >= a2 and i <= a2 + 1 else 0 for i in range(3 * n + 1)])
    m = np.delete(np.array(m), 0, axis = 1) # Delete the first column since a1 = 0.
    solution = [np.round(num, 4) for num in np.concatenate(([0], el.gauss_jordan(m)['solution']))]

    # Create the polynomials per interval.
    for _ in range(len(solution) // 3):
        # Append the polynomial to the list.
        a = 3 * (_) # Get the adder for morphing.
        test = str(solution[a]) + 'x^2 + ' + str(solution[a + 1]) + 'x + ' + str(solution[a + 2])
        polynomials.append(str(solution[a]) + 'x^2 + ' + str(solution[a + 1]) + 'x + ' + str(solution[a + 2]))
        intervals.append([xv[_], xv[_ + 1]]) # Append the intervals.

        # Get the approximate value if it is within the interval.
        if x >= xv[_] and x <= xv[_ + 1]:
            y = (solution[a] * (x ** 2)) + (solution[a + 1] * x) + solution[a + 2]
            intindex = _
    # Return a dictionary (polynomials and y).
    return { 'polynomials' : polynomials, 'intervals' : intervals, 'intindex' : intindex, 'y' : np.round(y, 4) }

'''
** get_row
| This is a helper function, which returns a row based on the condition.
- - -
** params
| - coefficients: A list of coefficients
| - n: Number of intervals
| - a: Adder (Optional)
** returns
| The vector form of the equation without a1.
'''
def get_row(coefficients, n, a = 0):
    return [coefficients[i - a] if i >= a and i <= a + 2 else coefficients[3] if i == 3 * n else 0 for i in range(3 * n + 1)]

'''
** clean_input
| This is a helper function to clean the data
| from the form.
- - -
** params
| - xv: A vector containing the x values
| - yv: A vector containing the y values
| - x: Value to be evaluated using the appropriate polynomial
- - -
** returns
| All parameters in the correct data type.
'''
def clean_input(xv, yv, x):
    return { 'xv' :  np.array([float(num) for num in xv.split(',')], dtype = float), 'yv' : np.array([float(num) for num in yv.split(',')], dtype = float), 'x' : float(x) }