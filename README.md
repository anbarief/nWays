



There are many ways to write a code for a particular task. This project starts with (may be updated) 35 ways to generate Fibonacci sequence in Python, includes using list, tuple, generator, etc. This is followed by another task, random sampling, (may also be updated) 20 ways to random sampling from a set of data. 

*Currently written in Python, Matlab, or C++. (Looking forward for contributions in Java)

E-mail: anbarief@live.com

-----



## F
 Fibonacci Numbers Generation
 [(n_fibo_ways.py)](https://github.com/anbarief/nWays/blob/master/n_fibo_ways.py)
 [(n_fibo_ways.m)](https://github.com/anbarief/nWays/blob/master/n_fibo_ways.m)
 [(n_fibo_ways.cpp)](https://github.com/anbarief/nWays/blob/master/n_fibo_ways.cpp)

## M
 Maximum Value
 [(n_max.cpp)](https://github.com/anbarief/nWays/blob/master/n_max.cpp)
 
## R
 Random Sampling without Replacement
 [(n_random_sampling.py)](https://github.com/anbarief/nWays/blob/master/n_random_sampling.py)

-----

## A Manifestation

## (35 functions that perform Fibo numbers):
`n_fibo_ways.py` consists of 35 different functions that generate the same Fibonacci numbers. To see the results, simply run it. `F.show_all(m)` will show 35 same results of first m Fibonacci numbers calculation.


### Examples:


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
1. Generate Fibonacci sequence using for loop and list. In each iteration the initial list append the sum of its last two elements.
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
