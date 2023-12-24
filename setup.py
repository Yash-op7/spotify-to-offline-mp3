# a python script which can be used in any project to install all required libraries and setup a project with initial metadata
# to run use the command: python setup.py install

from setuptools import setup, find_packages

requires = [
    'flask',
    'spotipy',
    'html5lib',
    'requests',
    'beautifulsoup4',
    'requests_html',
    'youtube_dl',
    'pathlib',
    'pandas',
    'AppDirs',
    'pyee',
    'tqdm',
    'lxml',
    'cssselect'
]

setup(
    name = 'SpotifyToYoutubeMP3',
    version='1.0',
    description='An app that downloads songs from a user\'s spotify playlist',
    author='Yash Meena',
    author_email='ymsc98@gmail.com',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)