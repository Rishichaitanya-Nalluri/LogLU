from setuptools import setup, find_packages
setup(
    name='loglu',  
    version='0.1.0',
    description='The Logarithmic Linear Unit (LogLU) is a novel activation function designed for deep neural networks, improving convergence speed, stability, and overall model performance',
    long_description=open('README.md').read() + "\n\n## Patent Notice\n\nThis software implements methods covered by Indian Published Patent Application No. 202341087256, currently published but not yet granted. Use of the patented methods may require a separate license. Please refer to the LICENSE file for more details.",
    long_description_content_type='text/markdown',
    author='Rishi Chaitanya Sri Prasad Nalluri',
    author_email='rishichaitanya888@gmail.com',
    license='MIT (with patent notice)',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.20.0',      
        'tensorflow>=2.10.0',  
        'keras>=2.10.0'       
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License with patent notice',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research', 
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='>=3.6',
)