# Lemon8 wrapper in Python

This is an unofficial wrapper for the Lemon8 API in Python. 
    
## Getting Started
    
### Installation
Pip
```
pip install pylemon8
```

From source
```python
https://github.com/shotnothing/pylemon8.git
python setup.py install
```

### Usage
```python
from lemon8 import Lemon8

lemon8 = Lemon8()
print(lemon8.feed('foryou').get_items())
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
