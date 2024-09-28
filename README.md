# Lemon8 Wrapper for Python

A lightweight, zestful Python library for integrating with the Lemon8 API, providing an intuitive interface for developers to access the Lemon8 social media platform.

## Getting Started

### Installation

Pip

```
pip install pylemon8
```

From source

```shell
https://github.com/shotnothing/pylemon8.git
python setup.py install
```

or

```shell
pip install git+ssh://git@github.com/shotnothing/pylemon8.git
```

### Example Usage

```python
from lemon8 import Lemon8

lemon8 = Lemon8()
print(lemon8.feed('foryou').get_items())
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
