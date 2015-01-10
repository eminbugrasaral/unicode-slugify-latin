from setuptools import setup

setup(
    name='unicode-slugify-turkish',
    version='0.1.3',
    description='A slug generator that turns strings into unicode slugs, and enables replacement for common Turkish latin letters into ascii representations.',
    long_description=open('README.md').read(),
    keywords='turkish,unicode,letter,char,replace,replacement,ascii,latin',
    author='Jeff Balogh, Dave Dash, Emin Bugra Saral',
    author_email='jbalogh@mozilla.com, dd@mozilla.com, eminbugrasaral@me.com',
    maintainer='Emin Bugra Saral',
    maintainer_email='eminbugrasaral@me.com',
    url='http://github.com/eminbugrasaral/unicode-slugify-turkish',
    license='BSD',
    packages=['slugify'],
    include_package_data=True,
    package_data={'': ['README.md']},
    zip_safe=False,
    install_requires=['six'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: Mozilla',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django'
    ]
)


