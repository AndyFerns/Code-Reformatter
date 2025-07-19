from setuptools import setup, find_packages

setup(
    name='code_formatter_cli',
    version='1.1.0',
    packages=find_packages(),
    install_requires=[
        'python-docx'
    ],
    entry_points={
        'console_scripts': [
            'formatcode=cli_tool.main:main'
        ]
    },
    author='Andrew Fernandes',
    description='CLI tool to format code with output in txt, docx, or LaTeX formats',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
        'Intended Audience :: Developers'
    ],
    python_requires='>=3.6'
)
