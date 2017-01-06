from setuptools import setup, find_packages

setup(name='torchcraft_py',
      version='0.0.1',
      description='Python wrapper for TorchCraft, a bridge between Torch and StarCraft for AI research.',
      url='http://gitlab.alibaba-inc.com/cogcom/torchcraft-py',
      author='Long Haitao',
      author_email='askoliver@gmail.com',
      license='MIT License',
      packages=find_packages(),
      zip_safe=False)
