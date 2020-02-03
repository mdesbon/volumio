import setuptools

setuptools.setup(
    name='volumio',
    version='0.0.1',
    description='Volumio REST API client.',
    url=None,
    author='Manuel Desbonnet',
    author_email='manueld@gmail.com',
    license='MIT',
    packages=['volumio'],
    install_requires=[
        'simple_rest_client',
    ],
    python_requires=">=3.6",
    zip_safe=False,
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ]
)
