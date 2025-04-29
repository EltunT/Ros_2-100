from glob import glob
from setuptools import setup
import os

package_name = 'ros_project'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],           # ← сам python-пакет (папка ros_project)
    data_files=[
        # маркер пакета
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),

        # package.xml
        ('share/' + package_name, ['package.xml']),

        # >>> добавляем нужные каталоги <<<
        (os.path.join('share', package_name, 'launch'),
         glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'rviz'),
         glob('rviz/*.rviz')),
        (os.path.join('share', package_name, 'urdf'),
         glob('urdf/*.xacro')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='elt',
    maintainer_email='elt@todo.todo',
    description='Package for robot visualization in RViz2',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
