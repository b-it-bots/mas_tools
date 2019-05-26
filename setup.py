from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['mas_tools'],
    package_dir={'mas_tools': 'src/mas_tools'}
)

setup(**d)
