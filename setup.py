try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup




classifiers = ['Environment :: Console',
               'Programming Language :: Python :: 3'
               ]

#requirements = [pkg.split('=')[0] for pkg in open('requirements.txt').readlines()]

setup(
    name='keep-password',
    version='1.6',  # Ideally should be same as your GitHub release tag varsion
    description='Save password for username',
    author='chandra khadka',
    author_email='chandra2khadka4@gmail.com',
    url='https://github.com/chandrabrt/keep',
    scripts=['src/keep-password'],
    install_requires=['pyperclip'],
    package=['keep_password'],
    package_dir={'keep_password': 'src/keep_password'},
    classifiers=classifiers
)

