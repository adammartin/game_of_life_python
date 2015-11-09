from paver.easy import *
from paver.setuputils import setup, find_packages


setup(
  name='game_of_life',
  packages=find_packages(exclude=['test', 'test.*']),
  namespace_packages=['game'],
  version='0.0.1.dev',
  install_requires=[
    'numpy'
  ],
  entry_points={
## example from Hisc DataCollector
#    'console_scripts': [
#      'collectdata = hisc.external.clearcare.datacollection.collectdata:run',
#    ],
  })


@task
def flake8():
  sh("flake8 game test")


@task
def test():
  sh("nosetests --with-xunit --with-cover --cover-package game --cover-inclusive")
  # Why do we have python3 specifically named and not control this from virtualenv
  sh('python3 -m coverage xml --omit "**/__init__.py"')


@task
@needs(['test', 'flake8', 'bdist_wheel'])
def default():
    pass
