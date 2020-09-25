from setuptools import setup, find_packages

dev_req = [
    "black>=19.10b0",
    "pylint>=2.5.3",
]

test_req = [
    "pytest>=5.4.3",
]



setup(
    name="project",
    version="1.0",
    description="<short project description>",
    author="<author or authors>",
    author_email="author@example.com",
    url="<project or repo url>",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[], # app dependencies
    extras_require={"dev": test_req + dev_req, "test": test_req,}, 
)

