clear; clc

N = input("How many values are in the sequence: ");
J = [0 1];
for k = 3:N+1
    J(k) = J(k-1) + 2*J(k-2);
end

plot(0:N, J, 'k*');
title("Jacobsthal Number")
xlabel('n')
ylabel('Jn')