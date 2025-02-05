from setuptools import setup, find_packages

setup(
    name='cis301',
    version='0.1.0',
    license='MIT',
    description='CIS301 Projects and Examples',
    author='Ali Sazegar',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['pytest-runner', 'pytest'],
    entry_points={
        'console_scripts': [
            'project1 = cis301.project1.__main__:main',
        ]
    },
)