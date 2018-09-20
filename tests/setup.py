from setuptools import setup 


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='nkrajesh',
        version='0.1',
        description = 'Return median of given list',
        long_description = readme(),
        classifiers = ['Development Status :: 3- Alpha',
            'License :: OSI Approved :: MIT License',
            'Programming Language:: Python::3.5',
            'Topic:: Text Processing :: Linguistic',
            ],
        keywords='median of given array list',
        url = 'http://',
        author = 'rajesh',
        author_email = 'rjnkvrmrjsh@gmail.com',
        license = 'MIT',
        packages = ['nkrajesh'],
        install_requires = ['statistics'],
        test_suite = 'nose.collector',
        test_require = ['nose', 'nose-cover3'],
        include_package = True,
        zip_safe = False
        )
