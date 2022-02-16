import os
from setuptools import setup, find_packages

setup(
    name='django-cdp-sdk',
    version='1.0.1',
    url='https://github.com/orderly-com/django-cdp-sdk',
    license='BSD',
    description='CDP SDK for django.',
    author='RayYang',
    author_email='ray.yang@ezorderly.com',

    packages=find_packages('src'),
    package_dir={'': 'src'},

    install_requires=['setuptools', 'requests', 'django', 'djangorestframework'],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
    ]
)