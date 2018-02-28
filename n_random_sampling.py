# Started since 26 Feb, 2018
# Author : anbarief@live.com

import random
import copy
import itertools

data=["data_{}".format(i) for i in range(100)];

print("Data : ")
print(data);

ex_1 = "1. Sampling by directly use the random.sample function.";
def sampling_1(data, n=10):
    data=copy.deepcopy(data);
    return random.sample(data, n)
    
ex_2 = "2. Sampling by directly use the random.sample function, but through the indexes, \
then use lust comprehension to construct the sample.";
def sampling_2(data, n=10):
    data=copy.deepcopy(data);
    idxs=random.sample(range(len(data)), n)
    sample=[data[i] for i in idxs];
    return sample

ex_3="3. Sampling the index of data's list \
in a for-loop, using random.randint, and store in a list. \
The index choosing will be repeated if index already chosen before.";
def sampling_3(data, n=10):
    data=copy.deepcopy(data);
    N=len(data);
    sample=[];
    for i in range(n):
        idx = random.randint(0,N-1);
        while data[idx] in sample:
            idx = random.randint(0,N-1);
        sample.append(data[idx]);
    return sample
    
ex_4="4. Sampling the index of data's list \
using while, using random.randint, and store in a list. \
The index choosing will be repeated if index already chosen before.";
def sampling_4(data, n=10):
    data=copy.deepcopy(data);
    N=len(data);
    sample=[]; 
    while len(sample)<n:
        idx = random.randint(0,N-1);
        if not (data[idx] in sample):
            sample.append(data[idx]);
    return sample
    
ex_5="5. Sampling the index of data's list \
in a for-loop, using random.randint, and store in a dictionary. \
The index choosing will be repeated if index already chosen before.";
def sampling_5(data, n=10):
    data=copy.deepcopy(data);
    N=len(data);
    sample={}; 
    for i in range(n):
        idx = random.randint(0,N-1);
        while data[idx] in sample:
            idx = random.randint(0,N-1);
        sample[i]=data[idx];
    return sample
    
ex_6="6. Sampling by using random.randint and store the sample in list. \
The copied-original data is popped after each sampling, to avoid repetition.";
def sampling_6(data, n=10):
    data=copy.deepcopy(data);
    sample=[];
    for i in range(n):
        idx = random.randint(0,len(data)-1);
        sample.append(data.pop(idx));
    return sample
    
ex_7="7. Sampling the index of data's list \
using random.randint, and list comprehension. \
The initial indexes list will keep being updated using .pop in the list comprehension, \
such that the sampling is without replacement.";
def sampling_7(data, n=10):
    data=copy.deepcopy(data);
    N=len(data);
    idxs=list(range(N));
    rand_idxs=[idxs.pop(random.randint(0,len(idxs)-1)) \
               for i in range(n)];
    sample=[data[i] for i in rand_idxs];
    return sample
 
ex_8 = "8. Sampling without replacement by a recursive method. \
The function take_new works as a \"cyclic\" function until we get a new sample from data."
def sampling_8(data, n=10):
    data=copy.deepcopy(data);
    N=len(data);
    sample=[];
    def take_new():
        idx=random.randint(0, N-1);
        if data[idx] in sample:
            return take_new()
        else:
            sample.append(data[idx]);
            return None
    for i in range(n): take_new();
    return sample
    
ex_9 = "9. Similar as no.8, but with additional \"cyclic\" condition \
: if number of samples less than n.";
def sampling_9(data, n=10):
    data=copy.deepcopy(data);
    N=len(data);
    sample=[];
    def take_new():
        idx=random.randint(0, N-1);
        if data[idx] in sample:
            return take_new()
        else:
            sample.append(data[idx]);
        if len(sample)<n:
            return take_new()
    take_new();
    return sample
   
ex_10 = "10. Similar as no.7, but the sampling is using map and directly from the data, not it's indexes.";
def sampling_10(data, n=10):
    data=copy.deepcopy(data);
    dummy=range(n);
    sample=list(map(lambda x: data.pop(random.randint(0,len(data)-1)),dummy));
    return sample
    
ex_11 = "11. Same as no.10, but using list comprehension.";
def sampling_11(data, n=10):
    data=copy.deepcopy(data);
    dummy=range(n);
    sample=[data.pop(random.randint(0,len(data)-1)) for i in dummy];
    return sample
    
ex_12 = "12. Similar as no.10, but using list.append in while loop.";
def sampling_12(data, n=10):
    data=copy.deepcopy(data);
    sample=[];
    while len(sample)<n:
        sample.append(data.pop(random.randint(0,len(data)-1)));
    return sample
    
ex_13 = "13. Similar as no.9, but try-except rather than using \
if len(sample)<n.";
def sampling_13(data, n=10):
    data=copy.deepcopy(data);
    N=len(data);
    sample=[];
    def take_new():
        idx=random.randint(0, N-1);
        if data[idx] in sample:
            return take_new()
        else:
            sample.append(data[idx]);
        try :
            sample[n-1]
        except:
            return take_new()
    take_new();
    return sample
    
ex_14 = "14. Using random.choice n times, while removing \
 the chosen sample from the original data.";
def sampling_14(data, n=10):
    data=copy.deepcopy(data);
    sample=[];
    for i in range(n):
        rand=random.choice(data);
        data.remove(rand);
        sample.append(rand);
    return sample
    
ex_15 = "15. Define a remove-and-return function, such that we \
can use random.choice in list comprehension to collect n samples.";
def sampling_15(data, n=10):
    data=copy.deepcopy(data);
    def rem_n_ret(x, rem):
        rem.remove(x);
        return x
    sample=[rem_n_ret(random.choice(data), data) \
            for i in range(n)]
    return sample
    
ex_16 = "16. Sampling by shuffling the data, then get only \
the first n elements.";
def sampling_16(data, n=10):
    data=copy.deepcopy(data);
    random.shuffle(data);
    sample=data[0:n];
    return sample
     
ex_17 = "17. Sampling by taking samples from a uniform distribution, \
 and treat them as the random generated index.";
def sampling_17(data, n=10):
    data=copy.deepcopy(data); 
    idxs = [];
    while len(idxs)<n:
        rand=int(random.uniform(0, len(data)))
        if rand in idxs:
            pass
        else:
            idxs.append(rand);
    sample=[data[i] for i in idxs];
    return sample

ex_18 = "18. Sampling by taking samples from random.random, multiply by N, and floor it, \
then treat them as random generated index.";
def sampling_18(data, n=10):
    data=copy.deepcopy(data);
    N=len(data);
    idxs=[];
    while len(idxs)<n:
        rand=int(random.random()*N);
        if rand in idxs:
            pass
        else:
            idxs.append(rand)
    sample=[data[i] for i in idxs];
    return sample    
    
ex_19 = "19. We can also use try-except this way, to ensure that \
the sampling is without replacement.";
def sampling_19(data, n=10):
    data=copy.deepcopy(data);
    sample=[];
    dummy=[0];
    while len(sample)<n:
        rand=random.choice(data);
        try:
            dummy[sample.count(rand)]
            sample.append(rand);
        except:
            pass
    return sample
    
ex_20 = "20. Combining the use of random.sample and random.choice. At each iteration, \
a sample is withdrawn from data, the method used is switched at next iteration.";
def sampling_20(data, n=10):
    data=copy.deepcopy(data);
    sample=[];
    for i in range(n):
        if (-1)^(i)==1:
            rand=random.sample(data,1);
        else:
            rand=random.choice(data);
        data.remove(rand);
        sample.append(rand);
    return sample          
    	
##################

class UnifSampling:
    def __init__(self):
        self.funcs=tuple([eval("sampling_{}".format(i)) for i in range(1,21)]);
        self.func_desc=tuple([eval("ex_{}".format(i)) for i in range(1,21)]);
    def call_function(self, number, n):
        return self.funcs[number](n);
    def show_all(self, data, n=10):
        for i in range(len(self.funcs)):
            print("\n");
            print(self.func_desc[i]);
            print(self.funcs[i](data, n));

Unif=UnifSampling();
Unif.show_all(data, 10)