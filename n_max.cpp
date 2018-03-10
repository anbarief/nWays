// Author : anbarief@live.com
// Since 10 March 2018

#include <iostream>
#include <string>


float max_1(float x[], int sizex){
	float max = x[0];
	for (int index=0; index < sizex; index++){
		if (x[index] >= max) {
		max = x[index];
		}
	}
	return max;
}

float max_2(float x[], int sizex){
	float max;
	for (int index=0; index < sizex; index++){
		if (x[index+1] >= x[index]) {
		max = x[index+1];
		}
		else {
		max = x[index];
		}
		x[index+1]=max;
	}
	return max;
}

float max_3(float x[], int sizex){
	float max = x[0];
    int index=0; 
	while (index < sizex)
	{
    	if (x[index] >= max) {
		max = x[index];
		}
		index = index+1;
    }
	return max;
}

float max_4(float x[], int sizex){
	float max, maxx, maxxx;
	
	if (x[0] >= x[sizex-1]){
		max = x[0];
	}
	else{
		max = x[sizex-1];
	};
	
	int mid=(sizex+(sizex%2))/2;
	
	for (int index=1; index < mid; index++){
		
		if (x[sizex-index-1] >= x[index]) {
		maxx = x[sizex-index-1];
		}
		else {
		maxx = x[index];
		}
		
		if (maxx >= max){
			maxxx = maxx;
		}
		else{
			maxxx = max;
		}
		
		max = maxxx;
	
	}
	return maxxx;
}

float max_5(float x[], int sizex){
	float max, maxx, maxxx;
	
	if (x[0] >= x[sizex-1]){
		max = x[0];
	}
	else{
		max = x[sizex-1];
	};
	
	int index = 1;
	int mid=(sizex+(sizex%2))/2;
	
	while(index < mid){
		
		if (x[sizex-index-1] >= x[index]) {
		maxx = x[sizex-index-1];
		}
		else {
		maxx = x[index];
		}
		
		if (maxx >= max){
			maxxx = maxx;
		}
		else{
			maxxx = max;
		}
		
		max = maxxx;
	    
	    index=index+1;
	}
	return maxxx;
}

float max_6(float x[], int sizex){
	
	float max;
	
	if (x[sizex]>=x[sizex-1]){
		max=x[sizex];
	} 
	else{
		max=x[sizex-1];
	};
	
	if (sizex == 1){
	return max;
	};
	
	x[sizex-1] = max;

	return max_6(x, sizex-1);
}


int main(){
	
	float data[] {1, 1, 2, -2, -2233, -112.3, 3, 3, 3, 4.123, 1, 44.234, 2.0013, 3, 5, 5, 6, 6, 3, 56, 112, 112, 112.3, 12, 3};
	const int n = sizeof(data)/sizeof(*data);
	
	std::string ex_1 = "max_1 : Comparing per-element in a for-loop to get the maximum val.";
	std::cout << '\n' << ex_1;
	std::cout << '\n' << max_1(data, n);
	
	std::string ex_2 = "max_2 : Comparing two adjacent elements of the data in a for-loop to get the maximum val.";
	std::cout << '\n' << ex_2;
	std::cout << '\n' << max_2(data, n);
	
	std::string ex_3 = "max_3 : Similar as max_1, but using while-loop";
	std::cout << '\n' << ex_3;
	std::cout << '\n' << max_3(data, n);
	
	std::string ex_4 = "max_4 : Comparing end-to-end elements of the data in a for-loop to get the maximum.";
	std::cout << '\n' << ex_4;
	std::cout << '\n' << max_4(data, n);
	
	std::string ex_5 = "max_5 : Similar as max_4, but using while-loop.";
	std::cout << '\n' << ex_5;
	std::cout << '\n' << max_5(data, n);
	
	std::string ex_6 = "max_6 : Using a recursive method to find the maximum.";
	std::cout << '\n' << ex_6;
	std::cout << '\n' << max_6(data, n);
	
	return 0;
}
