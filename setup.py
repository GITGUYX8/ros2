from setuptools import find_packages, setup

package_name = 'my_controller'

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
    maintainer='vboxuser',
    maintainer_email='vboxuser@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    
    entry_points={
        'console_scripts': [
            "test_node = my_controller.hello_world:main",
            "draw_cirle = my_controller.draw_circle:main",
            "pose_sub = my_controller.pose_subscriber:main",
            "spiral_code  = my_controller.spiral_motion:main"
        ],
    },
)
