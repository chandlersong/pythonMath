from setuptools import setup, find_packages

intall_requires = [
    'pandas>=0.18.1',
    'numpy>=1.11.0',
    'matplotlib>=3.0.2',
    'scipy>=1.2.0', 'sympy'
]

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    licence = f.read()

setup(
    name='pythonMath',
    packages=find_packages(exclude=['python_math', 'python_math.*']),
    version='0.1',
    license=licence,
    author='Chandler Song',
    install_requires=intall_requires,
    author_email='chandler605@outlook.com',
    long_description=readme,
    description='use python to handler math'
)
