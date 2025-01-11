from setuptools import setup

setup(
    name="MarketDataLib",
    version="0.1.4",
    author="Jason",
    author_email="",
    description="Market Data API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/toaster-robotics/MarketDataLib",
    py_modules=["MarketDataLib"],
    install_requires=[
        "requests>=2.0.0",
        "pandas>=2.0.0"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
