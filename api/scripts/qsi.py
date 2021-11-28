'''
** qsi
| This module finds the equations for each
| interval based on the data set using QSI.
'''
import numpy as np
import elimination as el

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
| - p: All polynomials per interval
| - y: Approximate of f_n(x) using the appropriate function of an interval (based on x)
'''
def poly_qsi(xv, yv, x):
    # ** Declaration
    m = [] # Store the matrix from the conditions.
    n = len(xv) - 1 # Store the number of intervals.
    p = [] # Store the polynomials per interval.
    y = 0 # Store the approximate value of f_n(x).

    # Return None if xv and yv are unequal in size.
    if len(xv) != len(yv):
        return None
    
    # Add rows to the matrix for condition 1.
    for _ in range(1, n):
        c = [xv[_] ** 2, xv[_], 1, yv[_]] # Store the coefficients.
        m.append(get_row(c, n, 3 * (_ - 1)))
        m.append(get_row(c, n, 3 * _))
    
    # Add rows to the matrix for condition 2.
    m.append(get_row([xv[0] ** 2, xv[0], 1, yv[0]], n))
    m.append(get_row([xv[n] ** 2, xv[n], 1, yv[n]], n, 3 * (n - 1)))

    # Add rows to the matrix for condition 3.
    for _ in range(1, n):
        # ** Declaration
        c = [2 * xv[_], 1] # Store the coefficients.
        a1 = 3 * (_ - 1) # Store the small adder.
        a2 = 3 * _ # Store the big adder.

        # Add a row to the matrix for condition 3.
        m.append([c[i - a1] if i >= a1 and i <= a1 + 1 else -c[i - a2] if i >= a2 and i <= a2 + 1 else 0 for i in range(3 * n + 1)])
    m = np.delete(np.array(m), 0, axis = 1) # Delete the first column since a1 = 0.
    solution = np.concatenate(([0], el.gauss_jordan(m)['solution'])) # Get the solution of the matrix.

    # Create the polynomials per interval.
    for _ in range(len(solution) // 3):
        # Append the polynomial to the list.
        a = 3 * (_) # Get the adder for morphing.
        test = str(solution[a]) + 'x^2 + ' + str(solution[a + 1]) + 'x + ' + str(solution[a + 2])
        p.append(str(solution[a]) + 'x^2 + ' + str(solution[a + 1]) + 'x + ' + str(solution[a + 2]))

        # Get the approximate value if it is within the interval.
        if x >= xv[_] and x <= xv[_ + 1]:
            y = (solution[a] * (x ** 2)) + (solution[a + 1] * x) + solution[a + 2]
    # Return a dictionary (polynomials and y).
    return { 'p' : p, 'y' : y }

'''
** get_row
| This is a helper function, which returns a row based on the condition.
- - -
** params
| - c: A list of coefficients
| - n: Number of intervals
| - a: Adder (Optional)
** returns
| The vector form of the equation without a1.
'''
def get_row(c, n, a = 0):
    return [c[i - a] if i >= a and i <= a + 2 else c[3] if i == 3 * n else 0 for i in range(3 * n + 1)]

# Test the function here.
poly_qsi(np.array([3.0, 4.5, 7.0, 9.0]), np.array([2.5, 1.0, 2.5, 0.5]), 5)