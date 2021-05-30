import setuptools
import os
import sys
from shutil import rmtree

here = os.path.abspath(os.path.dirname(__file__))

version = "1.0"

class UploadCommand(setuptools.Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds...')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution...')
        os.system('{0} setup.py sdist bdist_wheel'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine...')
        os.system('twine upload dist/*')

        self.status('Pushing git tags...')
        os.system('git tag v{0}'.format(version))
        os.system('git push --tags')

        sys.exit()

with open("README.md", "r") as fh:
    long_description = fh.read()


    setuptools.setup(
       name='bhammer',  
       version=version,
       license='GNU',
       scripts=['bhammer'] ,
       author="Noxtal",
       author_email="contact.noxtal@gmail.com",
       python_requires=">=3.6.0",
       description="Python tool to create a ASCII art banner for a command line tool.",
       long_description=long_description,
       long_description_content_type="text/markdown",
       url="https://github.com/noxtal/bhammer",
       packages=setuptools.find_packages(),
       install_requires=["art"],
       classifiers=[
       "Programming Language :: Python :: 3.6",
       "Programming Language :: Python :: 3.7",
       "Programming Language :: Python :: 3.8",
       "License :: OSI Approved :: GNU License",
       "Operating System :: OS Independent",
       'Topic :: Software Development :: Build Tools',
       'Intended Audience :: Developers',
       ],
       cmdclass={
        'upload': UploadCommand,
    }
    )