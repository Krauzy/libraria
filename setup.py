from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="libraria",
    version="0.1",
    author="Krauzy",
    author_email="caiomarin26@gmail.com",
    description="An application with multiples IA app ideas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Krauzy/libraria",
    project_urls={
        "Source Code": "https://github.com/Krauzy/libraria",
        "Documentation": "https://github.com/Krauzy/libraria/README.md",
        "Bug Tracker": "https://github.com/Krauzy/libraria/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
)
