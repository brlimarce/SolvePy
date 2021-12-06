'''
** form
| This module manipulates the forms
| in the web app.
'''
from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, Form, RadioField, BooleanField
from wtforms.validators import DataRequired, ValidationError

'''
** is_number
| This is a custom validator, which checks
| if the value is numerical.
- - -
** params
| - form: The current form
| - field: The input field of the data
'''
def is_number(form, field):
    try:
        num = float(field.data)
    except:
        raise ValidationError('❌ Enter a number.')

'''
** QSIForm
| This class contains the validation for the form of QSI.
- - -
** input
| - xv: A vector of x values separated by a comma
| - yv: A vector of y values separated by a comma
| - x: The x value (to be evaluated by a function)
'''
class QSIForm(FlaskForm):
    '''
    ** is_csv
    | This is a custom validator, which checks
    | if the values are separated by a comma.
    - - -
    ** params
    | - form: The current form
    | - field: The input field of the data
    '''
    def is_csv(form, field):
        try:
            # Split the data; then, convert each into a float.
            splitter = [float(num) for num in (field.data).split(',')]

            # Raise an exception if there is only 1 data point.
            if len(splitter) <= 1:
                raise Exception()
        except:
            raise ValidationError('❌ Enter values separated by a comma.')
    
    # ** Error Messages
    __msg_required = '❌ Field is empty.'

    # ** Schema
    xv = StringField('xv', validators = [DataRequired(message = __msg_required), is_csv])
    yv = StringField('yv', validators = [DataRequired(message = __msg_required), is_csv])
    x = StringField('x', validators = [DataRequired(message = __msg_required), is_number])
    send = SubmitField('display-qsi')

'''
** Demand
| This class contains the single schema for the warehouse's
| number of demands.
- - -
** input
| demand: The number of demands and supplies or the shipping cost
'''
class Demand(Form):
    # ** Error Messages
    __msg_required = '❌ Field is empty.'

    # ** Schema
    demand = StringField('', validators = [DataRequired(message = __msg_required), is_number])

'''
** Supply
| This class contains the single schema for the plant's
| number of supply.
- - -
** input
| supply: The number of demands and supplies or the shipping cost
'''
class Supply(Form):
    # ** Error Messages
    __msg_required = '❌ Field is empty.'

    # ** Schema
    supply = StringField('', validators = [DataRequired(message = __msg_required), is_number])

'''
** ShippingCost
| This class contains the single schema for the shipping cost
| from a plant to a warehouse.
- - -
** input
| cost: The number of demands and supplies or the shipping cost
'''
class ShippingCost(Form):
    # ** Error Messages
    __msg_required = '❌ Field is empty.'

    # ** Schema
    cost = StringField('', validators = [DataRequired(message = __msg_required), is_number])

'''
** SimplexForm
| This class contains the validation for the form of Simplex Method.
- - -
** input
| - demands: A list containing the number of demand for each warehouse
| - supplies: A list containing the number of supply for each plant
| - costs: A list containing the shipping cost from a plant to a warehouse
| - method: The type of method used (Default: Maximization)
| - options: A list containing the user's choices
'''
class SimplexForm(FlaskForm):
    # ** Schema
    demands = FieldList(FormField(Demand), min_entries = 5, max_entries = 5)
    supplies = FieldList(FormField(Supply), min_entries = 3, max_entries = 3)
    costs = FieldList(FormField(ShippingCost), min_entries = 15, max_entries = 15)

    method = RadioField('method', choices = [('maximization', 'Maximization'), ('minimization', 'Minimization')], default = 'maximization')

    display_tableau = BooleanField('Display Initial Tableau')
    get_shipped_items = BooleanField('Get Number of Shipped Items')

    send = SubmitField('display-simplex')