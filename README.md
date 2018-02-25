# nWays
There are many ways to write a code for a particular task. This project starts with (may be updated) 35 ways to generate Fibonacci sequence in Python, includes using list, tuple, generator, etc., and some examples from www.rosettacode.org, the others are original.

`n_fibo_ways.py` consists of 35 different functions that generate the same Fibonacci numbers. To see the results, simply run it. `F.show_all(m)` will show 35 same results of first m Fibonacci numbers calculation.


```python ex_1 = "1. Generate Fibonacci sequence using for loop and list. \
In each iteration the initial list append the sum \
of its last two elements.";
def fibo_1(n):
    f=[0,1];
    for i in range(n-len(f)):
        f.append(f[1+i]+f[i]);
    return f```
    
