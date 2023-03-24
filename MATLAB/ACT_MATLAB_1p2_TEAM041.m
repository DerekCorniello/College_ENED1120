% Activity 1 Task 2: Sequential and Conditional
% File: ACT_MATLAB_1p2_TEAM041.m
% Date: 1 January 2023
% By: Derek Corniello, Tyler Collaros,
%     Aidan Halpin, Aidan Oliver
%
% Section: 003
% Team: 041
%
% ELECTRONIC SIGNATURE 
% Derek Corniello, Tyler Collaros,
% Aidan Halpin, Aidan Oliver
%
% The electronic signature above indicates the script
% submitted for evaluation is my individual work, and I
% have a general understanding of all aspects of its
% development and execution.
%
% A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
% Determine if the roots of a second order polynomial are
% real and distinct, repeated, or complex.

clear; clc
a = input("Enter a: ");
b = input("Enter b: ");
c = input("Enter c: ");

D = b^2 - (4*a*c);

fprintf("D = " + D)
fprintf("\n")

if(D > 0)
    fprintf("Real Roots.")
elseif (D < 0)
    fprintf("Complex Roots.")
else
    fprintf("Repeated")
end
fprintf("\n")