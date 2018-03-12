// Author : anbarief@live.com
// Since 2 March 2018

#include <iostream>
#include <string>
#include <algorithm>
#include <iterator>
#include <vector>
#include <cmath>
#include <functional>

void fibo_1(int n){
	
	int f[n];
	
	f[0] = 0; f[1] = 1;

	std::cout << f[0] << "-" << f[1];
	
	for (int index = 2; index < n; index++){
		
		f[index] = f[index-1] + f[index-2];
		std::cout << "-" << f[index];
		
	}

}

void fibo_2(int n){
	
	int f[n]; int index=2;
	
	f[0] = 0; f[1] = 1;

	std::cout << f[0] << "-" << f[1];
	
	while (index < n) {
		
		f[index] = f[index-1] + f[index-2];
		std::cout << "-" << f[index];
		index = index + 1;
		
	}

}

int fibo_3(int n, int a = 0, int b = 1){
	
    std::cout << a << "-";
    
    if (n == 2){
    
    std::cout << b;
    
    return 0;
    	
    }
    
    return fibo_3(n-1, b, a+b);

}

void fibo_4(int n){
	
	std::vector<int> f(n, 0);
	f[1] = 1;
	
	std::cout << f[0] << "-" << f[1];
	
	for (int index = 2; index < n; index++){
		
		f[index] = f[index-1] + f[index-2];
		std::cout << "-" << f[index];
		
	}
	
}

void fibo_5(int n){
	
	std::vector<int> f(2, 0);
	f[1] = 1;
	
	std::cout << f[0] << "-" << f[1];
	
	for (int index = 2; index < n; index++){
		
		int val = f[index-1] + f[index-2];
		
		f.push_back(val);
		std::cout << "-" << val;
		
	}
	
}

void fibo_6(int n){
	
	std::vector<int> f(2, 0);
	f[1] = 1;
	
	std::cout << f[0] << "-" << f[1];
	
	for (int index = 2; index < n; index++){
		
		int val = f[index-1] + f[index-2];
		
		f.push_back(val);
		std::cout << "-" << f.back();
		
	}
	
}

void fibo_7(int n){
	
	float f[n];
	float sqr5 = std::sqrt(5);
	f[0] = 0; f[1] = 1;
	
	std::cout << f[0] << "-" << f[1];
	
	for (int index = 2; index < n; index++){
		
		f[index] = (1/sqr5)*(pow(0.5,index))*(pow(1+sqr5,index) - pow(1-sqr5,index));
		
		std::cout << "-" << f[index];
		
	}
	
	
}

void fibo_8(int n){
	
	float f[n];
	float sqr5 = std::sqrt(5);
	f[0] = 0; f[1] = 1;
	
	std::cout << f[0] << "-" << f[1];
	
	for (int index = 2; index < n; index++){
	
	if (index%2==0){
		f[index] = (1/sqr5)*(pow(0.5,index))*(pow(1+sqr5,index) - pow(1-sqr5,index));
	}
	else{
		f[index] = f[index-1] + f[index-2];
	};
		std::cout << "-" << f[index];
		
	}
	
}

std::vector<int> matrix_mul(int A[2][2], int B[2][2]){
	std::vector<int> res(4,  0);

	res[0] = A[0][0]*B[0][0] + A[0][1]*B[1][0];
    res[1] = A[0][0]*B[0][1] + A[0][1]*B[1][1];
    res[2] = A[1][0]*B[0][0] + A[1][1]*B[1][0];
    res[3] = A[1][0]*B[0][1] + A[1][1]*B[1][1];
    
	return res;
}

void fibo_9(int n){
	
	float f[n];
	int A[2][2], B[2][2];
	std::vector<int> M(4,0);
	
	f[0] = 0; f[1] = 1; f[2] = 1;
	
	A[0][0] = 1; A[0][1] = 1;
	A[1][0] = 1; A[1][1] = 0;
	
	B[0][0] = 1; B[0][1] = 1;
	B[1][0] = 1; B[1][1] = 0;
	
	
	std::cout << f[0] << "-" << f[1] << "-" << f[2];
	
	for (int index = 1; index < n-2; index++){
	// 2x2 Matrix multiplication 
    	M = matrix_mul(B, A);
    	B[0][0] = M[0]; B[0][1] = M[1];
    	B[1][0] = M[2]; B[1][1] = M[3];
    	
    	f[3] = M[0];
    	std::cout << "-" << f[3]; 
    }

}

// A function from www.rosettacode.org :
unsigned int fibo_rosetta(unsigned int n) {
  if (n == 1) return 0;
  std::vector<int> v(n);
  v[1] = 1;
  transform(v.begin(), v.end()-2, v.begin()+1, v.begin()+2, std::plus<int>());
  // "v" now contains the Fibonacci sequence from 0 up
  return v[n-1];
}

void fibo_10(int n){
	int f[n];
	f[0]=0; f[1]=1;
	
	std::cout << f[0] << "-" << f[1];
	
	for (int index=2; index<n; index++){
		
		std::cout << "-" << fibo_rosetta(index+1);
		
	}
	
}

// A function from www.rosettacode.org :
inline void fibmul(int* f, int* g)
{
  int tmp = f[0]*g[0] + f[1]*g[1];
  f[1] = f[0]*g[1] + f[1]*(g[0] + g[1]);
  f[0] = tmp;
}

// A function from www.rosettacode.org :
int fibo_rosetta_2(int n)
{
  int f[] = { 1, 0 };
  int g[] = { 0, 1 };
  while (n > 0)
  {
    if (n & 1) // n odd
    {
      fibmul(f, g);
      --n;
    }
    else
    {
      fibmul(g, g);
      n >>= 1;
    }
  }
  return f[1];
}

void fibo_11(int n){
	int f[n];
	f[0]=0; f[1]=1;
	
	std::cout << f[0] << "-" << f[1];
	
	for (int index=2; index<n; index++){
		
		std::cout << "-" << fibo_rosetta_2(index);
	
	}
}

int main(){
	
	int n = 20;
	
	std::string ex_1 = "fibo_1 : Using simple for-loop and fn = fn-1 + fn-2.";
	std::cout << '\n' << ex_1 << '\n';
	fibo_1(n);
	
	std::string ex_2 = "fibo_2 : Similar as fibo_1, but with while-loop.";
	std::cout << '\n' << ex_2 << '\n';
	fibo_2(n);
	
	std::string ex_3 = "fibo_3 : Using recursive method, with backward n.";
	std::cout << '\n' << ex_3 << '\n';
	fibo_3(n);
	
	std::string ex_4 = "fibo_4 : Similar as fibo_1, but using vector as container.";
	std::cout << '\n' << ex_4 << '\n';
	fibo_4(n);
	
	std::string ex_5 = "fibo_5 : Similar as fibo_4, using f.push_back method to add new Fibo number.";
	std::cout << '\n' << ex_5 << '\n';
	fibo_5(n);
	
	std::string ex_6 = "fibo_6 : Similar as fibo_5, but using f.back() to show the element.";
	std::cout << '\n' << ex_6 << '\n';
	fibo_6(n);
	
	std::string ex_7 = "fibo_7 : Using the analytical Fibo formula.";
	std::cout << '\n' << ex_7 << '\n';
	fibo_7(n);
	
	std::string ex_8 = "fibo_8 : Using combination of both Analytical formula, and the ususal fn = fn-1 + fn-2.";
	std::cout << '\n' << ex_8 << '\n';
	fibo_8(n);
	
	std::string ex_9 = "fibo_9 : Using Matrix identity of Fibonacci numbers, Fn = A^(n) F_init.";
	std::cout << '\n' << ex_9 << '\n';
	fibo_9(n);
	
	std::string ex_10 = "fibo_10 : Using an outsource function, fibonacci, from www.rosettacode.org, renamed as fibo_rosetta.";
	std::cout << '\n' << ex_10 << '\n';
        fibo_10(n);
	
	std::string ex_11 = "fibo_11 : Using another different outsource function, fibonacci, from www.rosettacode.org, renamed as fibo_rosetta_2.";
	std::cout << '\n' << ex_11 << '\n';
        fibo_11(n);
		
	return 0;
}
