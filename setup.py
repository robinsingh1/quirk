from setuptools import setup

setup(
    name='quirk',
    version='0.1.2',
    description='Build powerful predictive models with a few lines of code',
    url='https://github.com/ankane/quirk',
    author='Andrew Kane',
    author_email='andrew@chartkick.com',
    license='MIT',
    packages=['quirk'],
    install_requires=[
        'pandas',
        'seaborn',
        'sklearn',
        'matplotlib',
        'scipy'
    ],
    zip_safe=False
)
