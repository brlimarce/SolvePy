'''
** form
| This module manipulates the forms
| in the web app.
'''
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Regexp

'''
** QSIForm
| This class contains the validation for the form.
- - -
** validators
| - xval: Contain the x values separated by a comma
| - yval: Contain the y values separated by a comma
| - value: Contain the x value
'''
class QSIForm(FlaskForm):
    # ** Declaration
    __csv_regexp = '^([0-9](,))*[0, 9]$' # Store the regex equivalent of csv.
    __msg_required = 'This field is required.' # Error message for required fields.
    __msg_regexp = 'Multiple values must be separated by commas.' # Error message for regex mismatch.

    # ** Schema
    xval = StringField('xval', validators = [DataRequired(message = __msg_required), Regexp(__csv_regexp, message = __msg_regexp)])

    yval = StringField('yval', validators = [DataRequired(message = __msg_required), Regexp(__csv_regexp, message = __msg_regexp)])

    val = IntegerField('val', validators = [DataRequired(message = __msg_required)])

    send = SubmitField('display-qsi')