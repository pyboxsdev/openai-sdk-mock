from setuptools import setup, find_packages

# Read the contents of README.md
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Read the contents of __version__.py
about = {}
with open(Path(__file__).parent / "openai_mock" / "__version__.py", "r", encoding="utf-8") as f:
    exec(f.read(), about)

setup(
    name="openai-sdk-mock",
    version=about["__version__"],
    author="Your Name",
    author_email="your.email@example.com",
    description="A mock version of the OpenAI SDK for testing purposes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/openai-sdk-mock",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        "typing-extensions>=3.7.4",
    ],
)