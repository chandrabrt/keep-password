try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requirements = [pkg.split('=')[0] for pkg in open('requirements.txt').readlines()]


classifiers = ['Environment :: Console',
               'Programming Language :: Python :: 3'
               ]


setup(
    name='extract',

    version='1.0',  # Ideally should be same as your GitHub release tag varsion
    description='Save password for username',
    author='chandra khadka',
    author_email='chandra2khadka4@gmail.com',
    url='https://github.com/chandrabrt/keep',
    scripts=['src/ex-tract'],
    install_requires=requirements,
    package=['ex_tract'],
    package_dir={'ex_tract': 'src/ex_tract'},
    classifiers=classifiers
)

