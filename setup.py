from setuptools import setup

setup(
    name='AccessControl',
    version='1.0.0',
    packages=['AccessController'],
    url='https://github.com/c0ldfront/AccessControl',
    license='',
    author='David Charles Mydlarz',
    author_email='coldfront@gmail.com',
    description='easy access control for game servers',
    install_requires=[
        'beautifulsoup4==4.10.0',
        'lxml==4.6.3',
        'soupsieve==2.2.1',
    ]
)



