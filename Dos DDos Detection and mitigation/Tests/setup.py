from setuptools import setup, find_packages

setup(
    name='dos_ddos_detection',
    version='1.0.0',
    description='Real-time DoS/DDoS detection and mitigation tool.',
    author='Bonu Swetha Devi Sai Priya',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'scapy',
        'argparse',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
