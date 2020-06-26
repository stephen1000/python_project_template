from setuptools import setup, find_packages


setup(
    name="project",
    version="1.0",
    description="<short project description>",
    author="<author or authors>",
    author_email="author@example.com",
    url="<project or repo url>",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["black", "python-dotenv", "pylint", "pytest",],
)

