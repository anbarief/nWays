# nWays
There are many ways to write a code for a particular task. This project starts with (may be updated) 35 ways to generate Fibonacci sequence in Python, includes using list, tuple, generator, etc., and some examples from www.rosettacode.org, the others are original.

`n_fibo_ways.py` consists of 35 different functions that generate the same Fibonacci numbers. To see the results, simply run it. `F.show_all(m)` will show 35 same results of first m Fibonacci numbers calculation.

Manifestation:

Function:

```python 
ex_1 = "1. Generate Fibonacci sequence using for loop and list. \
In each iteration the initial list append the sum \
of its last two elements.";
def fibo_1(n):
    f=[0,1];
    for i in range(n-len(f)):
        f.append(f[1+i]+f[i]);
    return f 
```
   
Output:

```python
Generate Fibonacci sequence using for loop and list. In each iteration the initial list append the sum of its last two elements.
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
```

Function:

```python 
ex_5 = "5. Generate Fibonacci sequence using recursive method and list. \
The function only append the sequence final two elements, \
and then check its length, and recall the function \
with the updated sequence as input until n-terms.";
def fibo_5(n, initial=[0,1]):
    f=initial;
    res = f[-1]+f[-2];
    f.append(res);
    if len(f)==n:
        return f
    else:
        return fibo_5(n, f)
```

Output:

```python 
5. Generate Fibonacci sequence using recursive method and list. The function only append the sequence final two elements, and then check its length, and recall the function with the updated sequence as input until n-terms.
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
```

an example from www.rosettacode.org :

```python 
ex_22 = "22. (the fibGen function from www.rosettacode.org) Using generator \
to generate Fibonacci numbers, then use list comprehension.";
def fibo_22(n):
    def fibGen(n):
        a, b = 0, 1
        while n>0:
           yield a
           a, b, n = b, a+b, n-1
    return [i for i in fibGen(n)]
```

Output:

```python 
22. (the fibGen function from www.rosettacode.org) Using generator to generate Fibonacci numbers, then use list comprehension.
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
```

