from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description= fh.read(),

setup(
    name='AlertPy',
    version='1.0',
    author='Kornelijus Gizys Studio',
    author_email='kornelijusgizyslight@gmail.com',
    description='Библиотека предназначена для веб-разработки, а именно для контроля Alert-окон.',
    long_description_content_type='text/markdown',
    python_requires='>=3.11.1',
    packages=find_packages()
)