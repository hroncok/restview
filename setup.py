#!/usr/bin/env python
import os

from setuptools import setup


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


def get_version(filename='src/restview/restviewhttp.py'):
    for line in read(filename).splitlines():
        if line.startswith('__version__'):
            d = {}
            exec(line, d)
            return d['__version__']
    raise AssertionError("couldn't find __version__ in %s" % filename)


version = get_version()

setup(
    name='restview',
    version=version,
    author='Marius Gedminas',
    author_email='marius@gedmin.as',
    url='https://mg.pov.lt/restview/',
    project_urls={
        'Source': 'https://github.com/mgedmin/restview',
    },
    description='ReStructuredText viewer',
    long_description=read('README.rst') + '\n\n' + read('CHANGES.rst'),
    long_description_content_type='text/x-rst',
    license='GPL',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Documentation',
        'Topic :: Text Processing :: Markup',
    ],
    keywords='rst restructuredtext preview',

    packages=['restview'],
    package_dir={'': 'src'},
    package_data={'restview': ['*.css', '*.ico']},
    include_package_data=True,
    install_requires=['docutils', 'readme_renderer', 'pygments'],
    extras_require={'syntax': [], 'test': ['mock']},
    test_suite='restview.tests.test_suite',
    tests_require=['mock'],
    zip_safe=False,
    entry_points="""
    [console_scripts]
    restview = restview.restviewhttp:main
    """,
)
