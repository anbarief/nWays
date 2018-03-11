// Author : anbarief@live.com
// Since 10 March 2018

#include <iostream>
#include <string>
#include <algorithm>
#include <iterator>
#include <vector>

float max_1(float x[], int sizex){
	float max = x[0];
	for (int index=1; index < sizex; index++){
		if (x[index] >= max) {
		max = x[index];
		}
	}
	return max;
}

float max_2(float x[], int sizex){
	float max;
	for (int index=1; index < sizex; index++){
		if (x[index] >= x[index-1]){
		max = x[index];
		}
		else {
		max = x[index-1];
		}
		x[index]=max;
	}
	return max;
}

float max_3(float x[], int sizex){
	float max = x[0];
    int index=1; 
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
	
	int mid = (sizex + (sizex%2))/2;
	
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
	int mid = (sizex+(sizex%2))/2;
	
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
	
	if (x[sizex-1]>=x[sizex-2]){
		max=x[sizex-1];
	} 
	else{
		max=x[sizex-2];
	};
	
	if (sizex == 1){
	return max;
	};
	
	x[sizex-2] = max;

	return max_6(x, sizex-1);
}

float max_7(float x[], int sizex, int index=0){
	
	float max;
	
	if (x[index+1]>=x[index]){
		max=x[index+1];
	} 
	else{
		max=x[index];
	};
	
	if (index==sizex-2){
	return max;
	};
	
	x[index+1]=max;
    
	return max_7(x, sizex, index+1);
}

float max_8(float x[], int sizex){
	
	float max;
	
	for (int index=1; index < sizex; index++){
		
		max = std::max(x[index], x[index-1]);
		x[index-1] = max;
		
	}
	
	return max;
}

float max_9(float x[], int sizex){
	
	std::vector<float> v(x, x+sizex);
	
    return	*std::max_element(v.begin(), v.end());

}

float max_10(float x[], int sizex){
	
    return	*std::max_element(x, x+sizex);

}

float max_11(float x[], int sizex){

	float max = x[0];

	std::vector<float> v(x, x+sizex);

	for (std::vector<float>::iterator it = v.begin(); it != v.end(); it++){
		
		if (*it >= max){
			max = *it;
		}
		
	}
	return max;
}

float max_12(float x[], int sizex){

	float max = x[0];

	std::vector<float> v(x, x+sizex);

	for (int index=1; index < sizex; index++){
		
		if (x[index] >= max){
			max = x[index];
		}
		
	}
	
	return max;
}

float max_13(float x[], int sizex){

	float max;

	std::vector<float> v(x, x+sizex);

	for (int index = 1; index < sizex; index++){
	
		if (v[index] >= v[index-1]){
			max = v[index];
		}
		else{
			max = v[index-1];
		}
	}
	
	return max;
}


int main(){
	
	float data[] {1, 1, 2, -2, -2233, -112.3, 3233, 3, 3, 4.123, 1, 44.234, 2.0013, 3, 5, 5, 6, 6, 3, 56, 112, 112, 112.3, 12, 3};
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
	
	std::string ex_7= "max_7 : Similar as max_6, but starts from index 0.";
	std::cout << '\n' << ex_7;
	std::cout << '\n' << max_7(data, n);
	
	std::string ex_8 = "max_8 : Using the max function from algorithm library.";
	std::cout << '\n' << ex_8;
	std::cout << '\n' << max_8(data, n);
	
	std::string ex_9 = "max_9 : Using the max_element function from algorithm library.";
	std::cout << '\n' << ex_9;
	std::cout << '\n' << max_9(data, n);
	
	std::string ex_10 = "max_10 : Similar as max_9, but with different way on the arguments.";
	std::cout << '\n' << ex_10;
	std::cout << '\n' << max_10(data, n);
	
	std::string ex_11 = "max_11 : Similar as max_1, but using iterator on vector in a for-loop.";
	std::cout << '\n' << ex_11;
	std::cout << '\n' << max_11(data, n);
	
	std::string ex_12 = "max_12 : Similar as max_1, but using vector instead of array.";
	std::cout << '\n' << ex_12;
	std::cout << '\n' << max_12(data, n);
	
	std::string ex_13 = "max_13 : Similar as max_2, but using iterator on vector in a for-loop.";
	std::cout << '\n' << ex_13;
	std::cout << '\n' << max_13(data, n);
	
	return 0;
}
