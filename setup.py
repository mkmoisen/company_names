from setuptools import setup 

setup(name='companynames',
    version='0.1',
    description='Random company names from the S&P 500',
    url='https://github.com/mkmoisen/company_names',
    author='Matthew Moisen',
    author_email='mkmoisen@gmail.com',
    license='MIT',
    packages=['companynames'],
    zip_safe=False,
    package_data={'companynames':['companynames.txt']},
    include_package_data=True)