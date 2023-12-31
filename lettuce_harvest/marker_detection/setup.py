from setuptools import setup

package_name = 'marker_detection'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tone',
    maintainer_email='tone@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'marker_detection_node = marker_detection.marker_detection_node:main',
            'marker_detection_test = marker_detection.marker_detection_test:main',
            'ar_marker_node = marker_detection.ar_marker_node:main',
            'operation_inst_node = marker_detection.operation_inst_node:main',
            'qr_code_detection = marker_detection.qr_code_detection_node:main',
        ],
    },
)
