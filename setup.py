
from setuptools import setup

setup(
    name='reg_form_additional_fields_plugin',
    version='1.0',
    description='OpenEdx - Custom Fields for Registration Form',
    packages=['reg_form_additional_fields'],
    install_requires=[
        'Django',
        'django-countries'
    ],
)

