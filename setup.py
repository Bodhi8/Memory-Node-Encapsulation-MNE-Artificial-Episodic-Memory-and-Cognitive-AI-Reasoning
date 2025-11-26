"""
Setup script for Memory-Node Encapsulation (MNE) package
"""

from setuptools import setup, find_packages
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="mne-memory",
    version="0.1.0",
    author="Brian Curry",
    author_email="brian@vector1.ai",
    description="Memory-Node Encapsulation: Artificial Episodic Memory for Cognitive AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mne-project",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/mne-project/issues",
        "Documentation": "https://github.com/yourusername/mne-project/docs",
        "Research": "https://vector1.ai",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20.0",
        "python-dateutil>=2.8.0",
    ],
    extras_require={
        "full": requirements,
        "dev": [
            "pytest>=7.2.0",
            "pytest-cov>=4.0.0",
            "black>=22.10.0",
            "flake8>=6.0.0",
            "mypy>=0.990",
        ],
        "embeddings": [
            "sentence-transformers>=2.2.0",
            "transformers>=4.20.0",
        ],
        "databases": [
            "weaviate-client>=3.18.0",
            "neo4j>=5.5.0",
            "qdrant-client>=1.1.0",
        ],
    },
    keywords="artificial intelligence, episodic memory, cognitive AI, memory systems, AGI",
)
