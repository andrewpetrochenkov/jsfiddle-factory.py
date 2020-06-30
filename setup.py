import setuptools

setuptools.setup(
    name='jsfiddle-factory',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
