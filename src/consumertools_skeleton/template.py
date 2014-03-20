from paste.script import templates
from random import choice

default_key = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
vars = [
    templates.var('secret_key', 'Secret key', default=default_key),
]

    
class BasicProjectTemplate(templates.Template):
    _template_dir = 'templates/basic_project'
    summary = 'Basic skeleton for Consumer Tools projects'
    vars=vars
