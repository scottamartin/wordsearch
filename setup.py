from setuptools import setup

setup(
    name='wordsearch',
    version='0.1',
    description='Search word.docx files in a directory for phrases and output them to a csv file',
    py_modules=['wordsearch'],
    author='Scott Martin',
    license='MIT',
    install_requires=[
        'python-docx==0.8.6',
        'click==6.7'
    ],
    entry_points={
        'console_scripts': ['wordsearch=wordsearch:main'],
    },
)
