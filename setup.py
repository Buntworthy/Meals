from distutils.core import setup

setup(
    name='Meals',
    version='0.1dev',
    description='A meal index',
    author='Justin Pinkney',
    author_email='justinpinkney@gmail.com',
    packages=['meals',],
    scripts=['bin/meals'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
)