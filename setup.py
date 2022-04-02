from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'command sim and logging'
LONG_DESCRIPTION = 'Create servers and easily have logging'

# Setting up
setup(
    name="servert",
    version=VERSION,
    author="wellsilver",
    author_email="<wellsilver2016@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['colorama', 'pyautogui', 'pyaudio'],
    keywords=['python', 'logged', 'log', 'logging', 'logger', 'server'],
    classifiers=[
        "Development Status :: BETA",
        "Intended Audience :: All",
        "Programming Language :: Python3",
        "Operating System :: Linux",
        "Operating System :: Microsoft :: Windows",
    ]
)
