# Convolution
The purpose of this project is to demonstrate graphically how the convolution operation works.



## Usage
You can simply clone this repo and execute using the command below:
```bash
python3 main.py
```

You can also change the convoluted functions in this section:
```python
def f1(t):
    return (t > 1) * (t < 3) * abs(np.sin(2*np.pi*t))

def f2(t):
    return 0.8*(abs(t-0.2)<0.5)
```


## License
[MIT](https://choosealicense.com/licenses/mit/)
