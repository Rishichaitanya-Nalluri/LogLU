from setuptools import setup, find_packages

setup(
    name='loglu',  
    version='1.0.0',
    description='The Logarithmic Linear Unit (LogLU) is a novel activation function designed for deep neural networks, improving convergence speed, stability, and overall model performance',
    long_description=open('README.md', encoding='utf-8').read() + "\n\n## Patent Notice\n\nThis software implements methods covered by Indian Published Patent Application No. 202341087256, currently published but not yet granted. Use of the patented methods may require a separate license. Please refer to the LICENSE file for more details.",
    long_description_content_type='text/markdown',
    author='Rishi Chaitanya Sri Prasad Nalluri',
    author_email='rishichaitanya888@gmail.com',
    packages=find_packages(),
    classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research', 
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='>=3.6',
)
