from setuptools import setup

package_name = 'my_nav2_pkg'

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
    maintainer='paulopadrao',
    maintainer_email='pv.padrao@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        "nav2_test = my_nav2_pkg.nav2_test:main",
        "nav2_house_patrol = my_nav2_pkg.nav2_house_patrol:main"
        ],
    },
)
