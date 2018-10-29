import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_breathe",
    version="0.0.1",
    author="Kieran Hogg",
    author_email="kieran.hogg@gmail.com",
    description="A Python wrapper for the Breathe HR API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kieranhogg/breathe",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)