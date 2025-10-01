
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "End-to-end-ML-Project-with-MLflow"
AUTHOR_USER_NAME = "Jayshree Pawar"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "jayshreepawar1612@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author="Jayshree Pawar",
    author_email="jayshreepawar1612@gmail.com",
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/Jayshree16/End-to-end-Machine-Learning-Project-with-MLflow.git",
    project_urls={
        "Bug Tracker": f"https://github.com/Jayshree16/End-to-end-Machine-Learning-Project-with-MLflow.git/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
