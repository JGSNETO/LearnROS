from setuptools import find_packages, setup

package_name = 'turtlebot3_services'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jgsnto',
    maintainer_email='theautojourney.ab@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'reset_server = turtlebot3_services.reset_server:main',
            'reset_client = turtlebot3_services.reset_client:main',
        ],
    },
)
