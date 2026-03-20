from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    description="A sample test package",
    author="jhue",
    author_email="jhue@student.42Lyon.fr",
    url="https://github.com/thebugseven",
    license="MIT",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.7",
    classifiers=["Programming Language :: Python :: 3"],
)
