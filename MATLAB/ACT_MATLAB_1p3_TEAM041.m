% Activity 1 Task 3: Sequential and Conditional
% File: ACT_MATLAB_1p3_TEAM041.m
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

x = input("Enter x: ");
y = input("Enter y: ");

if (x == 0 && y == 0)
    fprintf("Your point is the origin. \n")
elseif (x == 0)
    fprintf("Your point is on the y-axis. \n")
elseif (y == 0)
    fprintf("Your point is on the x-axis. \n")
elseif (x > 0)
    if (y > 0)
        fprintf("Your point is in the First Quadrant. \n")
    else
        fprintf("Your point is in the Fourth Quadrant. \n")
    end
else
    if (y > 0)
        fprintf("Your point is in the Second Quadrant. \n")
    else
        fprintf("Your point is in the Third Quadrant. \n")
    end
end