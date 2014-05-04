from distutils.core import setup

setup(
  name='Protopype',
  version='0.0.1',
  author='Mika Lackman',
  author_email='mika.lackman@gmail.com',
  scripts=['bin/protopype.py'],
  install_requires=[
    'bottle',
  ]
)
