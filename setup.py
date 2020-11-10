import os.path

from setuptools import setup

setup(
    name="django-timedeltafield",
    version=open(os.path.join(os.path.dirname(__file__), 'timedelta', 'VERSION')).read().strip(),
    description="TimedeltaField for django models",
    long_description=open("README").read(),
    url="https://github.com/alexsilva/django-timedeltafield",
    author="Matthew Schinckel",
    author_email="matt@schinckel.net",
    packages=[
        "timedelta",
        "timedelta.templatetags",
    ],
    include_package_data=True,
    package_data={'timedelta': ['VERSION']},
    classifiers=[
        'Framework :: Django :: 2.2',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    test_suite='tests.main',
)
