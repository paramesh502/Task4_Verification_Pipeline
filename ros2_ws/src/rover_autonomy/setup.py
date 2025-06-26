from setuptools import setup

package_name = 'rover_autonomy'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=['scripts.arrow_detection'],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Team',
    maintainer_email='team@example.com',
    description='Automation tasks for IRC 2025 rover',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'arrow_detection = scripts.arrow_detection:main',
        ],
    },
)
