# Started since 20 Feb, 2018
# Author : anbarief@live.com

import math


ex_1 = "1. Generate Fibonacci sequence using for loop and list. \
In each iteration the initial list append the sum \
of its last two elements.";
def fibo_1(n):
    f=[0,1];
    for i in range(n-len(f)):
        f.append(f[1+i]+f[i]);
    return f

ex_2 = "2. Generate Fibonacci sequence using while-loop. \
In each iteration, while the length of the sequence \
is less than n, the sequence append the sum of its last two elemens.";   
def fibo_2(n):
    f=[0,1];
    while len(f)<n:
        f.append(f[-1]+f[-2]);
    return f
    
ex_3 = "3. Fibonacci sequence using list comprehension.";
def fibo_3(n):
    f=[0,1];
    [f.append(sum(f[-2:])) for i in range(2,n)];
    return f
    
ex_4 = "4. Fibonacci sequence using for-loop and \
list slicing at each iteration. \
The sequence append the sumnof the slice at each iteration.";
def fibo_4(n):
    f=[0,1];
    for i in range(2,n):
        res=sum(f[-2:]);
        f.append(res);
    return f
   
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
        
ex_6 = "6. This example shows how map and list can be used \
to generate a Fibonacci number, and retrieve the value using for loop.";
def fibo_6(n):
     f=[0,1];
     for i in range(2,n):
         res=map(lambda x: x[-1]+x[-2], [f]);
         for i in res:
             f.append(i);
     return f
     
ex_7 = "7. This example shows how map and list can be used \
to generate a Fibonacci number, and retrieve the value using simple *.";
def fibo_7(n):
     f=[0,1];
     for i in range(2,n):
         res=map(lambda x: x[-1]+x[-2], [f]);
         f.append(*res);
     return f

ex_8 = "8. Fibonacci sequence using dictionary. \
In a for-loop, the dictionary will update with next Fibo number.";
def fibo_8(n):
    f ={0: 0, 1:1};
    for i in range(2,n):
        f[i]=f[i-1]+f[i-2];
    return f
    
ex_9 = "9. Fibonacci sequence using dictionary and zip. \
In a for-loop, the dictionary will update with next Fibo number.";
def fibo_9(n):
    f =dict(zip(range(2), [0,1]));
    for i in range(2,n):
        f[i]=f[i-1]+f[i-2];
    return f
    
ex_10 = "10. Fibonacci sequence using dictionary dict() with tuple. \
In a for-loop, the dictionary will update with next Fibo number.";
def fibo_10(n):
    f =dict(((0,0),(1,1)));
    for i in range(2,n):
        f[i]=f[i-1]+f[i-2];
    return f
    
ex_11 = "11. Fibonacci sequence using dictionary. \
In a for-loop, the dictionary will update, using .update(), with next Fibo number.";
def fibo_11(n):
    f ={0: 0, 1:1};
    for i in range(2,n):
        f.update({i: f[i-1]+f[i-2]});
    return f

ex_12 = "12. This shows an example of generating \
 Fibonacci sequence using generator, then retrieve the list using end of for-loop.";
def fibo_12(n):
    f=[0,1];
    def gen():
       for i in range(2,n):
           res=sum(f[-2:]);
           f.append(res);
           yield f
    for i in gen():
        pass
    return i
    
ex_13 = "13. This shows an example of generating \
 Fibonacci sequence using generator, yielding each fibonacci numbers, \
 then retrieve using list-comprehension.";
def fibo_13(n):
    f=[0,1];
    def gen():
       for i in range(2,n):
           res=sum(f[-2:]);
           f.append(res);
           yield res
    f.extend([i for i in gen()])
    return f
        
ex_14 = "14. Generate Fibonacci sequence using generator comprehension. \
But retrieve it using end of for-loop.";
def fibo_14(n):
    f=[0,1];
    gen=(f.append(sum(f[-2:])) for i in range(2,n));
    for i in gen:
        pass;
    return f
    
ex_15 = "15. Fibonacci sequence using while and dictionary, \
by .update method.";   
def fibo_15(n):
    f={0:0, 1:1};
    idx=2;
    while idx<n:
        f.update({idx: f[idx-1]+f[idx-2]});
        idx+=1;
    return f
    
ex_16 = "16. Fibonacci sequence using while and dictionary, \
by setting new key.";   
def fibo_16(n):
    f={0:0, 1:1};
    idx=2;
    while idx<n:
        f[idx]=f[idx-1]+f[idx-2];
        idx+=1;
    return f
 
ex_17 = "17. Generate Fibonacci sequence by using string, \
and its .split method."
def fibo_17(n):
    fstr="0-1";
    for i in range(2,n):
        split=fstr.split('-');
        fstr+='-'+str(int(split[-1])+int(split[-2]));
    return fstr
    
ex_18 = "18. Generate Fibonacci sequence by using string, \
and its .split, and .join method."
def fibo_18(n):
    fstr="0-1";
    for i in range(2,n):
        split=fstr.split('-');
        split.append(str(int(split[-1])+int(split[-2])));
        fstr='-'.join(split);
    return fstr

ex_19 = "19. Generate Fibonacci sequence by using string, \
and its .split method, then append using .format."
def fibo_19(n):
    fstr="0-1";
    for i in range(2,n):
        split=fstr.split('-');
        fstr+='-{}'.format(int(split[-1])+int(split[-2]));
    return fstr
    
ex_20 = "20. Generate Fibonacci sequence by using string and list comprehension. \
The function uses predefined assign (val) func, and also .split method, then append using .format."
def fibo_20(n):
    fstr="0-1";
    def assign(val):
        nonlocal fstr
        fstr=val;
    [assign('{}-{}'.format(fstr, int(fstr.split('-')[-1])+int(fstr.split('-')[-2]))) \
     for i in range(2,n)];
    return fstr
    
ex_21 = "21. (almost as same as no.20) Generate Fibonacci sequence by using string and dictionary comprehension. \
The function uses predefined assign (val) func, and also .split method, then append using .format."
def fibo_21(n):
    fstr="0-1";
    def assign(val):
        nonlocal fstr
        fstr=val;
    {assign('{}-{}'.format(fstr, int(fstr.split('-')[-1])+int(fstr.split('-')[-2]))) \
     for i in range(2,n)};
    return fstr

ex_22 = "22. (the fibGen function from www.rosettacode.org) Using generator \
to generate Fibonacci numbers, then use list comprehension.";
def fibo_22(n):
    def fibGen(n):
        a, b = 0, 1
        while n>0:
           yield a
           a, b, n = b, a+b, n-1
    return [i for i in fibGen(n)]
    
ex_23 = "23. (the fibRec function from www.rosettacode.org) Using recursive \
method generate Fibonacci number, then use list comprehension.";
def fibo_23(n):
    def fibRec(n):
        if n < 2:
            return n
        else:
            return fibRec(n-1) + fibRec(n-2)
    return [fibRec(i) for i in range(0,n)]

ex_24 = "24. (Hacked the fibRec function from www.rosettacode.org) Using recursive \
method generate Fibonacci number and list.";
def fibo_24(n):
    f=[]; 
    def fibRec(n):
        if n < 2:
            if len(f)==n:
               f.append(n);
            return n
        else:
            if len(f)==n:
                f1=fibRec(n-2);
                f2=fibRec(n-1);
                f.append(f1+f2);
            else:
                f1=fibRec(n-2);
                f2=fibRec(n-1);
            return f1 + f2
    fibRec(n)
    f.append(f[-1]+f[-2]);
    return f

ex_25 = "25. (The fibIter function from www.rosettacode.org) Using iteration \
method to generate Fibonacci number, then collect many using list comprehension.";
def fibo_25(n):
    def fibIter(n):
        if n < 2:
            return n
        fibPrev = 1;
        fib = 1;
        for num in range(2, n):
            fibPrev, fib = fib, fib + fibPrev
        return fib
    return [fibIter(i) for i in range(n)]

ex_26 = "26. (Hacked the fibIter function from www.rosettacode.org) Using iteration \
method to generate Fibonacci number, while using append(Fibo number) at each loop.";
def fibo_26(n):
    f=[];
    def fibIter(n):
        if n < 2:
            f=list(range(0,n+1));
            return f
        fibPrev = 0;
        fib = 1;
        f=[0,1];
        for num in range(2, n):
            fibPrev, fib, = fib, fib + fibPrev
            f.append(fib);
        return f
    return fibIter(n)

ex_27 = "27. (The fibFastRec function from www.rosettacode.org) Using recursive \
method to generate Fibonacci number, then use list comprehension to collect Fibo numbers.";
def fibo_27(n):
    def fibFastRec(n):
        def fib(prvprv, prv, c):
            if c < 1: 
                return prvprv
            else: 
                return fib(prv, prvprv + prv, c - 1) 
        return fib(0, 1, n)
    return [fibFastRec(i) for i in range(n)]

ex_28 = "28. (Hacked the fibFastRec function from www.rosettacode.org) Using recursive \
method to generate Fibonacci number, while use using list.append in the process.";
def fibo_28(n):
    f=[0,1];
    def fibFastRec(n):
        def fib(prvprv, prv, c):
            if c < 3: 
                return prvprv
            else: 
                f.append(prvprv + prv);
                return fib(prv, prvprv + prv, c - 1) 
        return fib(0, 1, n)
    fibFastRec(n);
    return f

ex_29 = "29. Using string to generate Fibonacci sequence. \
It uses string.find and string.format in such a way.";
def fibo_29(n):
    f="0-1";
    idx=0;
    for i in range(2,n):
        if f.count("-")<2:
            idx=f.find("-");
            f=f+"-{}".format(int(f[idx-1])+int(f[idx+1]));
        else:
           idxnew=f.find("-",idx+1);
           f=f+"-{}".format(int(f[idx+1:idxnew])+int(f[idxnew+1:]));
           idx=idxnew;
    return f
 
ex_30 = "30. Using tuple and a for-loop to generate Fibonacci sequence.";
def fibo_30(n):
    f=(0,1);
    for i in range(2,n):
        f=f+(f[-1]+f[-2],)
    return f
    
ex_31 = "31. Fibonacci sequence using fibonacci sequence sum-formula.";
def fibo_31(n, initial=[0,1]):
    f=list(initial);
    if len(f)>2:
        res = sum(f[1:-1])+f[0]+f[1];
    else:
        res = sum(f);
    f.append(res);
    if len(f)==n:
        return f
    else:
        return fibo_31(n, f)
       
ex_32 = "32. Fibonacci sequence using it's analytic formula and list."
def fibo_32(n):
    r1=1+math.sqrt(5);
    r2=1-math.sqrt(5);
    sfive=math.sqrt(5);
    f=[round((1/sfive)*((r1/2))**i - (1/sfive)*((r2/2))**i) for i in range(0, n)];
    return f
    
ex_33 = "33. Fibonacci sequence using \
it's analytic formula and dictionary comprehension."
def fibo_33(n):
    r1=1+math.sqrt(5);
    r2=1-math.sqrt(5);
    sfive=math.sqrt(5);
    f={i: round((1/sfive)*((r1/2))**i - (1/sfive)*((r2/2))**i) for i in range(0, n)};
    return f
   
ex_34 = "34. Fibonacci sequence using it's analytic formula and using map"
def fibo_34(n):
    r1=1+math.sqrt(5);
    r2=1-math.sqrt(5);
    sfive=math.sqrt(5);
    f=list(map(lambda x: round((1/sfive)*((r1/2))**x - (1/sfive)*((r2/2))**x), range(0, n)));
    return f

ex_35 = "35. Generate Fibonacci sequence using matrix form."
def fibo_35(n):
    def dot(u,v):
        return sum([i*j for i,j in zip(u,v)]);
    def fibMat(n):
        if n==1:
            return 0
        mat=[[1,1],[1,0]];
        res=[[1,1],[1,0]];
        for i in range(n-3):
           res = [[dot(res[0],[mat[0][0],mat[1][0]]), \
                   dot(res[0],[mat[0][1],mat[1][1]])], \
                  [dot(res[1],[mat[0][0],mat[1][0]]), \
                   dot(res[1],[mat[0][1],mat[1][1]])]
                   ];
        return res[0][0]
    return [fibMat(i) for i in range(1,n+1)];
    
##########

class FiboWays:
    def __init__(self):
        self.funcs=tuple([eval("fibo_{}".format(i)) for i in range(1,36)]);
        self.func_desc=tuple([eval("ex_{}".format(i)) for i in range(1,36)]);
    def call_function(self, number, n):
        return self.funcs[number](n);
    def show_all(self, n=10):
        for i in range(len(self.funcs)):
            print("\n");
            print(self.func_desc[i]);
            print(self.funcs[i](n));

F=FiboWays();
F.show_all(16)

 
