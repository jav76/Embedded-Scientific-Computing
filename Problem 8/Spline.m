clear;
clc;
close all;
x=[0, 2.40482555769577, 3.83170597020751, 5.52007811028631,7.01558666981561, 8.65372791291101, 10];
y = besselj(1,x);
delta=x(2:length(x)) - x(1:length(x)-1);
c=sym('C',[length(x)-1 4]);

for i=1:length(x)-1
    c(i,1)=y(i);
end

for i=1:length(x)-1
    eqn1(i)= y(i+1)==y(i)+c(i,2)*delta(i)+c(i,3)*delta(i)^2+c(i,4)*delta(i)^3;
end
