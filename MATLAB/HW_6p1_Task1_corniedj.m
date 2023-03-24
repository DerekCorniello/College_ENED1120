% HW 6 Task 1
% File: HW_6p1_Task1_corniedj.m
% Date: 16 February 2023
% By: Derek Corniello corniedj 
%
% Section: 003
% Team: 041
%
% ELECTRONIC SIGNATURE 
% Derek Corniello
%
% The electronic signature above indicates the script
% submitted for evaluation is my individual work, and I
% have a general understanding of all aspects of its
% development and execution.
%
% A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
% Stress test module for different materials
Stress = importdata('Stress.txt'); 
Strain = importdata('Strain.txt'); 

plot(Strain, Stress, 'x')
xlabel("Strain")
ylabel("Stress")
title("Stress-Strain Relationship")
hold on

E = [];
for n = 1:100
    E = [E, abs((Stress(n+1) - Stress(n))/(Strain(n+1) - Strain(n)))];
end

sum1 = 0;
for n = 1:length(E)
    sum1 = sum1 + E(n);
end
sum1 = sum1/length(E);

k = [];
H = [];
for n = 101:256
    A = log((Strain(n+1))/(Strain(n)));
    B = log((Stress(n+1))/(Stress(n)));
    k = [k, abs(B/A)];

    C = Stress(n);
    D = Strain(n)^k(n-100);
    H = [H, C/D];
end

sum2 = 0;
for n = 1:length(H)
    sum2 = sum2 + H(n);
end
sum2 = sum2/length(H);

sum3 = 0;
for n = 1:length(k)
    sum3 = sum3 + k(n);
end
sum3 = sum3/length(k);

fprintf("The estimated Young's Modulus, E, is:  %.2f MPa\n", sum1)
fprintf("The estimated Strength Coefficient, H, is:  %.2f MPa\n", sum2)
fprintf("The estimated Strain Hardening Exponent, k, is:  %.2f\n", sum3)