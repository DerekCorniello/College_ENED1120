% HW 5 Task 2
% File: HW_5p2_Task1_corniedj.m
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
% Calculate when the mass is on either arm.

clear; clc

d = input("Enter the value of the distance d: ");
m = input("Enter the value of the mass m: ");

m0 = 0;

for i = 1:40
    if (mod(i, 2) == 0)
        m0 = m0 + ((i + (i^2)*sin(i))/(2*(i^2)+1));
    else
        m0 = m0 + ((2*(i^2)+1)/(i^2+(sin(i))));
    end
end

m0 = m0 / 200;

fprintf("The value of mo is %.2f.\n",m0);

M = 0;

sumLess = 0;
sumGreater = 0;

for k = 0:100
    M = M + (m0 * ((k^2)/(k+1)));
    x = (d*((m-(2*M))/m));

    if (x < 0)
        sumLess = sumLess + 1;
    else
        sumGreater = sumGreater + 1;
    end
end

fprintf("The variable x is < 0 = %i. \n", sumLess)
fprintf("The variable x is > 0 = %i. \n", sumGreater)

