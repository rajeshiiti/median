from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()
setup(
    name='median',
    version='0.1',
    license='MIT',
    description='An example python package median',
    long_description=open('README.rst').read(),
    install_requires=['statistics'],
    url='https://github.com/rajeshiiti/median.git',
    author='Rajesh Verma',
    author_email='rjnkvrmrjsh@gmail.com'
)
