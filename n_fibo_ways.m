# Started since 3 Mar, 2018
# Author : anbarief@live.com

ex_1='1. Using Fibonacci function in a for-loop.';
disp(ex_1)
disp(fibo_1(16))

ex_2='2. Using Fibonacci formula fn=fn-1+fn-2 in a for-loop. ';
disp(ex_2)
disp(fibo_2(16))

ex_3='3. Similar as no.2, but using while-loop.';
disp(ex_3)
disp(fibo_3(16))

ex_4='4. Using recursive method.';
disp(ex_4)
disp(fibo_4(16))

ex_5='5. Using the sum function in a for-loop.';
disp(ex_5)
disp(fibo_5(16))

ex_6='6. Using Fibonacci function with vector input.';
disp(ex_6)
disp(fibo_6(16))

ex_7='7. Using Fibonacci alternative formula, the summation difference.';
disp(ex_7)
disp(fibo_7(16))

ex_8='8. Using a string to contain and generate Fibonacci numbers.';
disp(ex_8)
disp(fibo_8(16))

ex_9='9. Using the Fibonacci matrix form.';
disp(ex_9)
disp(fibo_9(16))




function f=fibo_1(n)
    
 for i=0:n-1
     f(i+1)=fibonacci(i);
 end
 
end
    
    
function f=fibo_2(n)
    
 f=[0,1];

 for i=3:n
    f(i)=f(i-1)+f(i-2);
 end

end


function f=fibo_3(n)
    
 f=[0,1];
 i=3;

 while (i<n+1)
    f(i)=f(i-1)+f(i-2);
    i=i+1;
 end

end


function f=fibo_4(n)
    
 f=[0,1];

 function y=recursive(m, a, b)
    
     if (m==3)
        y=a+b;
     else
        y=recursive(m-1, a+b, a);
     end
    
end

 for i=3:n
     f(i)=recursive(i, 1, 0);
 end

end


function f=fibo_5(n)
    
 f=[0,1];

 for i=3:n
    f(i)=sum(f(i-2:i-1));
 end

end


function f=fibo_6(n)
    
  f=fibonacci(0:n-1);
 
end


function f=fibo_7(n)
    
 f=[0,1];

 for i=3:n
     
     if (i>3)
        f(i)=sum(f)-sum(f(1:i-3));
     else
         f(i)=sum(f);
     end
     
 end

end


function f=fibo_8(n)
    
  f = '0-1-1';
  
  if n>3
   
      for i=4:n     
         logical = f=='-';
         strip = find(logical == 1);
         idx1 = strip(end);  idx2 = strip(end-1);
         a=str2num(f(idx1+1:end)); b=str2num(f(idx2+1:idx1-1));
         f(end+1)='-'; 
         new=num2str(a+b);
         f(end+2:end+2+length(new)-1)=new;
      end
     
  end 
 
end


function f= fibo_9(n)
   
    f=[0, 1];
  
    if n>3
        
        for i=3:n
            M = [1 1 ; 1 0]^(i-2);
            f(i) = M(1,1);
        end
        
    end
    
end


