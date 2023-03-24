% Exam 5 Question 15
% File: E5_P15_corniedj.m
% Date: 22 March 2023
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
% Prints Values using arrays and given values 

clear; clc

a = 1.24;
b = -1.25;
c = -1.81;
d = -1.91;

y = (1:100);
z = (1:100);
y(1) = 0;
z(1) = 0;
i = (1:100);

hold on

for n = 2:100

    y(n) = sin(a*z(n-1)) + (c*cos(a*y(n-1)));
    z(n) = sin(b*y(n-1)) + (d*cos(b*z(n-1)));

end

plot(i, y, 'bo-', i, z, 'ro-');
title("Function values")
xlabel('n')
ylabel('Function value')
legend("y(n)", "z(n)");

