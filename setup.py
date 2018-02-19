from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='ets_pull',
      version='0.1',
      description='Interfaces for ETS GRE and TOEFL API',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
      ],
      keywords='ets gre toefl api ',
      url='http://github.com/jamie-r-davis/ets_pull',
      author='Jamie Davis',
      author_email='jamjam@umich.edu',
      license='MIT',
      packages=['ets_pull'],
      install_requires=[
          'zeep',
      ],
      include_package_data=True,
      zip_safe=False)
