// Started since 2 Mar, 2018
// Author: anbarief@live.com

#include <iostream>
#include <vector>
#include <string>

void fibo_1(int n){
  int f[n];
  f[0]=0; 
  f[1]=1;
  std::cout << "\n 0 1 ";
  for (int i=2; i<n; i++){
     f[i]=f[i-1]+f[i-2];
     std::cout << f[i] << " ";
       }
}


void fibo_2(int n){
  int f[n];
  int count=2;
  f[0]=0; 
  f[1]=1;
  std::cout << "\n 0 1 ";
  while(count<n){ f[count]=f[count-1]+f[count-2];
     std::cout << f[count] << " ";
        count=count+1;
        }
  }
  

void fibo_3(int n){
  int first, second, f;
  second=0; 
  first=1;
  std::cout << "\n 0 1 ";
   for (int i=2; i<n; i++){
     f=first+second;
     std::cout << f << " ";
        second=first; first=f;
            }
}


int fibo4(int n, int first, int second){
if (n==2){
 return first+second;}
return fibo4(n-1, first+second, first);
}

void fibo_4(int n){
std::cout << "\n 0 1 ";
for (int i=2; i<n; i++){
std::cout << fibo4(i, 1, 0) << " ";
}
}


void fibo_5(int n){
std::vector<int> v (n, 1);
v[0]=0;
v[1]=1;
std::cout << "\n 0 1 ";
for (int i=2; i<n; i++){
 v[i] = v[i-1]+v[i-2];
std::cout << v[i] << " ";
}
}


void fibo_6(int n){
std::vector<int> v (2, 1);
v[0]=0;
v[1]=1;
std::cout << "\n 0 1 ";
for (int i=2; i<n; i++){
 v.push_back(v[i-1]+v[i-2]);
std::cout << v[i] << " ";
}
}


void fibo_7(int n){
std::vector<int> v (2, 1);
v[0]=0;
v[1]=1;
std::cout << "\n 0 1 ";
for (int i=2; i<n; i++){
 v.insert(v.end(), v[i-1]+v[i-2]);
std::cout << v[i] << " ";
}
}


int main(){
fibo_1(16);
fibo_2(16);
fibo_3(16);
fibo_4(16);
fibo_5(16);
fibo_6(16);
fibo_7(16);
return 0;
}
