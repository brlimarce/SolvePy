'''
** form
| This module manipulates the forms
| in the web app.
'''
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

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
    
    # ** Declaration
    __msg_required = '❌ Field is empty.'

    # ** Schema
    xv = StringField('xv', validators = [DataRequired(message = __msg_required), is_csv])
    yv = StringField('yv', validators = [DataRequired(message = __msg_required), is_csv])
    x = StringField('x', validators = [DataRequired(message = __msg_required), is_number])
    send = SubmitField('display-qsi')

'''
** SimplexForm
| This class contains the validation for the form of Simplex Method.
- - -
** validators
| - xval: A vector of the x values separated by a comma
| - yval: Contain the y values separated by a comma
| - value: Contain the x value
'''