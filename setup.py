from setuptools import setup, find_packages

setup(name='morepathhello',
      version='0.1',
      description='morepathhello',
      author='',
      author_email='',
      url='',
      keywords='morepath',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'morepath',
            'repoze.profile',
            'waitress'
            ],
      )

