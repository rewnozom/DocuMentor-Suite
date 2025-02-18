# setup.py
from setuptools import setup, find_packages

setup(
    name="markdown-analyzer",
    version="0.1.0",
    description="Analyserar markdown-dokument och genererar träningsdata för LLM",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "tqdm>=4.65.0",
        "pytest>=7.0.0",
        "typing-extensions>=4.5.0"
    ],
    entry_points={
        "console_scripts": [
            "markdown-analyzer=markdown_analyzer.__main__:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)