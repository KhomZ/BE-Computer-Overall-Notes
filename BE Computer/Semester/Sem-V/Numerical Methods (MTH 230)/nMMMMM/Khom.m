%Title:- To determine function value of Discrete using Langrange's 
%Interpolation Method
%Developed By:- Khom Raj Thapa Magar
%Date :- 13th Feb, 2020
%----------------Three Credential Statements----------------
close all;
clear variables;
clc;
%----------------Input Section-----------------------------
x = input('Enter the x-value of data set x[]=');
y = input('Enter the y-value of data set y[]=');
while(length(x) ~= length(y))
disp('The no. of record in x & y must match');
x = input('Enter the x-value of data set x[]=');
y = input('Enter the y-value of data set y[]=');
end
out = [x;y];
disp(out);
X = input('Enter the value of x at which y is to be determined x=');
%----------------Calculation Section-----------------------------
n = length(x);
Y = 0;
for i=1:n
    temp = 1;
    for j=1:n
        if(i~=j)
            temp = temp*(X-x(j))/(x(i)-x(j));
        end
        end
        Y = Y+ y(i)*temp;
end
disp('---------------------------------------------------------------');

%---------------------Output Section-----------------------------
msg = strcat('The functional value at x= ',num2str(X),' is : ',num2str(Y));
disp(msg);
%---------------------------------------------------------------

