import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pylemon8",
    packages=setuptools.find_packages(),
    version="0.1.0",
    license='MIT',
    author="Saw Jing Wen",
    author_email="shotnothinggg@gmail.com",
    description="Lemon8 Wrapper in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shotnothing/pylemon8",
    download_url='WIP',
    keywords=[
        'python', 
        'lemon8', 
        'pylemon8', 
        'bytedance', 
        'api',
        'lemon',
        '8',
        'wrapper',
        'py-lemon8',
        'pythonlemon8',
        'eight'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
    ],
    include_package_data=True
)