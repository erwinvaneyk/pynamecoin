from distutils.core import setup

setup(
    name='PyNamecoin',
    version='0.1.0',
    author='Erwin van Eyk',
    author_email='erwinvaneyk@gmail.com',
    packages=['pynamecoin', 'pynamecoin.test'],
    scripts=['bin/namecoin/namecoind.exe','bin/pynamecoin_example.py'],
    url='...',
    license='LICENSE',
    description='A Python wrapper for the Namecoin (NMC) client API',
    long_description=open('README.md').read(),
    install_requires=[],
)