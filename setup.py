"""Setup script for yolov5."""
import distutils
import os
from setuptools import find_packages
from setuptools import setup

distutils.dir_util.copy_tree('models', os.path.join('yolov5', 'models'))
distutils.dir_util.copy_tree('utils', os.path.join('yolov5', 'utils'))
distutils.dir_util.copy_tree('data', os.path.join('yolov5', 'data'))
for f in [f for f in os.listdir('.') if os.path.isfile(f)]:
  distutils.file_util.copy_file(f, 'yolov5')

def get_requirements():
  with open('requirements.txt') as f:
    return f.read().splitlines()

setup(
    name='yolov5',
    version='5.0',
    install_requires=get_requirements(),
    packages=[
      'yolov5',
      'yolov5.models',
      'yolov5.utils',
      'yolov5.utils.aws',
      'yolov5.utils.loggers',
      'yolov5.utils.loggers.wandb'
    ],
    package_data={
      'yolov5': ['data/*', 'data/*/*'] +
        [os.path.basename(f) for f in os.listdir('.')
        if os.path.isfile(f) and
        not os.path.basename(f).startswith('.') and
        os.path.splitext(f)[1] != '.py'],
      'yolov5.models': ['*', '*/*'],
      'yolov5.utils': ['*', '*/*'],
    },
    include_package_data=True,
    description='Yolov5 Object Detection Library',
    python_requires='>3.6',
)
