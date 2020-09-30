clc;clear;
x=[0, 2.40482555769577, 3.83170597020751, 5.52007811028631,7.01558666981561, 8.65372791291101, 10];
y = besselj(1,x);
n=length(x)-1;
a=y;

b=zeros(1,n);
d=zeros(1,n);
h=zeros(1,n);

alpha=zeros(1,n);

c=zeros(1,n+1);
u=zeros(1,n+1);
z=zeros(1,n+1);
l=zeros(1,n+1);
l(1)=1;

for i=1:n
    h(i)=x(i+1)-x(i); %deltaX
end

for i=2:n
    a1=a(i+1)-a(i);
    a2=a(i)-a(i-1);
    alpha(i)= (3*a1) / h(i)  - (3*a2)/h(i-1);
end

for i=2:n
    x1=x(i+1)-x(i-1);
    l(i)=2*x1-h(i-1)*(u(i-1));
    u(i)=h(i)/l(i);
    z(i)=(alpha(i)-h(i-1)*z(i-1))/l(i);
end
l(7)=1;

for j = n:-1:1
    c(j)=z(j)-u(j)*c(j+1);
    a1=a(j+1)-a(j);
    c1=c(j+1)+2*c(j);
    b(j)=a1/h(j) - h(j)*c1/3;
    c2=c(j+1)-c(j);
    d(j)=c(2)/(3*h(j));
end

S=zeros(n,5);
for i=1:n
    S(i,1)=a(i);
    S(i,2)=b(i);
    S(i,3)=c(i);
    S(i,4)=d(i);
    S(i,5)=x(i);
end

plot(x,y,'o');
hold on
plot(0:.1:10,besselj(1,0:.1:10));
for i=1:n
    fplot(@(X) a(i) + b(i)*(X-x(i)) + c(i).*(X-x(i)).^2 + d(i).*(X-x(i)).^3,[x(i) x(i+1)],'--');
end
legend('Data Points','Bessel Function','Cubic 1','Cubic 2','Cubic 3','Cubic 4','Cubic 5')
hold off;