from setuptools import setup, find_packages
import os

setup(
    name='consumertools-skeleton',
    version = "0.10",
    description="Paster templates for creating consumer team projects",
    author='Ali Jetha',
    author_email='ajetha@xprima.com',
    url='http://www.xprima.com/',
    packages = find_packages('src'),
    package_dir = {'':'src'},
    license = "",
    keywords = "",
    install_requires=[
        'setuptools',
	      'Paste',
	      'PasteDeploy',
        'PasteScript>=1.3',
        'Cheetah',
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points="""
        [paste.paster_create_template]
        basic_project=consumertools_skeleton.template:BasicProjectTemplate
    """,
)
