'''
** form
| This module manipulates the forms
| in the web app.
'''
from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, RadioField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Regexp
import re

'''
** Validator
| This class contains the custom validators
| and error messages for form validation.
- - -
** properties
| - msg_required: Error message for required fields
- - -
** methods
| - is_number: Check if a value is numerical
| - is_csv: Check if multiple values are separated by a comma
'''
class Validator():
    # ** Properties
    MSG_REQUIRED = '❌ Field is empty.'
    MSG_REGEXP = '❌ The format is incorrect. Check the input tab for more information.'

    METHOD_MAX = 'maximization'
    METHOD_MIN = 'minimization'

    # ** Methods
    '''
    ** is_number
    | This is a custom validator, which checks
    | if the value is numerical.
    - - -
    ** params
    | - form: The current form
    | - field: The input field of the data
    '''
    @staticmethod
    def is_number(form, field):
        try:
            num = float(field.data)
        except:
            raise ValidationError('❌ Enter a number.')
    
    '''
    ** is_csv
    | This is a custom validator, which checks
    | if the values are separated by a comma.
    - - -
    ** params
    | - form: The current form
    | - field: The input field of the data
    '''
    @staticmethod
    def is_csv(form, field):
        try:
            # Split the data; then, convert each into a float.
            splitter = [float(num) for num in (field.data).split(',')]

            # Raise an exception if there is only 1 data point.
            if len(splitter) <= 1:
                raise Exception()
        except:
            raise ValidationError('❌ Enter multiple numbers separated by commas.')
    
    '''
    ** is_integer
    | This is a custom validator, which checks
    | if the value is an integer.
    - - -
    ** params
    | - form: The current form
    | - field: The input field of the data
    '''
    @staticmethod
    def is_integer(form, field):
        try:
            num = int(field.data)
        except:
            raise ValidationError('❌ Enter an integer.')
    
    '''
    ** is_many
    | This is a custom validator, which checks
    | if the value is greater than 0.
    - - -
    ** params
    | - form: The current form
    | - field: The input field of the data
    '''
    @staticmethod
    def is_many(form, field):
        try:
            # Raise an exception if there is only 1 data point.
            if int(field.data) < 1:
                raise Exception()
        except:
            raise ValidationError('❌ Number should be greater than 1.')

    '''
    ** is_equations
    | This is a custom validator, which checks
    | if the constraints are obtained.
    - - -
    ** params
    | - form: The current form
    | - field: The input field of the data
    '''
    @staticmethod
    def is_equations(form, field):
        try:
            # Get the data and store them in an array.
            d = (field.data).split('\n')

            # Check if the number of constraints <= 1.
            if len(d) <= 1:
                raise Exception()
            # Check if the constraints have the correct format.
            for _ in range(1, len(d)):
                if not re.match('^((((([0-9]+(.[0-9]+)?))?x[0-9]+ \+ )+(([0-9]+(.[0-9]+)?))?x[0-9]+)|((([0-9]+(.[0-9]+)?))?x[0-9]+)) (>=|<=) ([0-9]+(.[0-9]+)?)(\\r)?$', d[_]):
                    raise Exception()
        except:
            raise ValidationError(Validator.MSG_REGEXP)

'''
** QSIForm
| This class contains the validation for the form of QSI.
- - -
** properties
| - xv: A vector of x values separated by a comma
| - yv: A vector of y values separated by a comma
| - x: The x value (to be evaluated by a function)
'''
class QSIForm(FlaskForm):
    xv = StringField('', validators = [DataRequired(message = Validator.MSG_REQUIRED), Validator.is_csv])
    yv = StringField('', validators = [DataRequired(message = Validator.MSG_REQUIRED), Validator.is_csv])
    x = StringField('', validators = [DataRequired(message = Validator.MSG_REQUIRED), Validator.is_number])

    '''
    ** validate
    | This overrides the validate function to
    | validate xv and yv at the same time.
    - - -
    ** params
    | self: The class in question
    '''
    def validate(self):
        # Store the error message for the custom validator.
        msg_size = '❌ Both vectors should have equal sizes.'

        # Use the normal validation for the form.
        if not FlaskForm.validate(self):
            return False
        # Check if xv and yv have equal sizes.
        if len((self.xv.data).split(',')) != len((self.yv.data).split(',')):
            # Append the error messages.
            self.xv.errors.append(msg_size)
            self.yv.errors.append(msg_size)
            return False
        return True
    send = SubmitField('display-qsi')

'''
** Demand
| This class contains the single schema for the warehouse's
| number of demands.
- - -
** properties
| demand: The number of demands of each warehouse
'''
class Demand(FlaskForm):
    demand = StringField('', validators = [DataRequired(message = Validator.MSG_REQUIRED), Validator.is_number])

'''
** Supply
| This class contains the single schema for the plant's
| number of supply.
- - -
** properties
| supply: The number of supplies of each plant
'''
class Supply(FlaskForm):
    supply = StringField('', validators = [DataRequired(message = Validator.MSG_REQUIRED), Validator.is_number])

'''
** ShippingCost
| This class contains the single schema for the shipping cost
| from a plant to a warehouse.
- - -
** properties
| cost: The shipping cost from a plant to a warehouse
'''
class ShippingCost(FlaskForm):
    cost = StringField('', validators = [DataRequired(message = Validator.MSG_REQUIRED), Validator.is_number])

'''
** ProblemForm
| This class contains the validation for the form of Simplex Method (Problem).
- - -
** properties
| - demands: A list containing the number of demand for each warehouse
| - supplies: A list containing the number of supply for each plant
| - costs: A list containing the shipping cost from a plant to a warehouse
| - method: The type of method used (Default: Maximization)
'''
class ProblemForm(FlaskForm):
    # ** Field List Schema
    demands = FieldList(FormField(Demand), min_entries = 5, max_entries = 5)
    supplies = FieldList(FormField(Supply), min_entries = 3, max_entries = 3)
    costs = FieldList(FormField(ShippingCost), min_entries = 15, max_entries = 15)

    # ** Radio Schema
    method = RadioField('method', choices = [(Validator.METHOD_MAX, 'Maximization'), (Validator.METHOD_MIN, 'Minimization')], default = Validator.METHOD_MAX)
    send = SubmitField('display-problem')

'''
** SimplexForm
| This class contains the initial tableau.
- - -
** properties
| - obj_function: A string containing the objective function
| - constraints: A list of equations for the constraints
| - method: The type of method used (Default: Maximization)
'''
class SimplexForm(FlaskForm):
    obj_function = TextAreaField('objective function', validators = [DataRequired(message = Validator.MSG_REQUIRED), Regexp('^Z = ((([0-9]+(.[0-9]+)?))?x[0-9]+ \+ )+(([0-9]+(.[0-9]+)?))?x[0-9]+(\\r)?$', message = Validator.MSG_REGEXP)])
    constraints = TextAreaField('constraints', validators = [DataRequired(message = Validator.MSG_REQUIRED), Validator.is_equations])
    method = RadioField('method', choices = [(Validator.METHOD_MAX, 'Maximization'), (Validator.METHOD_MIN, 'Minimization')], default = Validator.METHOD_MAX)
    send = SubmitField('display-simplex')