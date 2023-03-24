% Exam 5 Question 16
% File: E5_P16_corniedj.m
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
% Calculate sums in a matrix

clear; clc

N = input("Please Enter the order of the matrix (integer at or above 2): ");

while(N < 2 || mod(N, 1) ~= 0)
    N = input("Please Enter the order of the matrix (integer at or above 2): ");
end

X = randi([1 100],N);

for i = 1:N

    if mod(i,2) ~= 0

        sum = 0;

        for j = 1:N

            sum = sum + X(j,i);

        end

        fprintf("The sum of Column %i is %i.\n", i, sum);

    end

end

sumUnder = 0;

for i = 1:N

    for j = 1:N
        
        if i - j > 0

            sumUnder = sumUnder + X(i,j);

        end

    end

end

fprintf("The sum under the diagonal is %i.\n", sumUnder);

