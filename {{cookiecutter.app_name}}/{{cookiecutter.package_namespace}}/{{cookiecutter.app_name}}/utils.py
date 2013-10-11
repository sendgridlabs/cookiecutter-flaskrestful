'''Helper utilities and decorators.'''
from flask import session, flash
from functools import wraps


def flash_errors(form):
    '''Flash all errors for a form.'''
    for field, errors in form.errors.items():
        for error in errors:
            flash("Error in the {0} field - {1}"
                  .format(getattr(form, field).label.text, error), 'warning')


def auth_required(test):
    '''Decorator that makes a view require authentication.'''

    @wraps(test)
    def wrap(*args, **kwargs):
        if 'auth_key' in session:
            return test(*args, **kwargs)
        else:
            raise Exception("authorization failed")

    return wrap
