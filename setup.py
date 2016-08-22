from setuptools import setup

setup(name='firepi',
      version='0.1',
      description='FireServiceRota home automation integration using Raspberry Pi',
      url='http://github.com/rhomeister/firepi',
      author='Ruben Stranders',
      author_email='ruben@fireservicerota.co.uk',
      license='MIT',
      packages=['firepi'],
      install_requires=[
          'requests', 
          'dateutils',
          'rpi.gpio'
      ],
      zip_safe=False
)

