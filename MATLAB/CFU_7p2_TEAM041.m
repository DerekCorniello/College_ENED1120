% CFU 7p2
% File: CFU_7p2_TEAM041.m
% Date: 22 February 2023
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

clear; clc

rng(3);

X = randi([-5,5],[3,4]);

Y = randi([-5,5],[3,4]);
q1=0;
q2=0;
q3=0;
q4=0;

for i = 1:3
    for j = 1:4
        if X(i, j) >= 0 %1 or 4 

            if Y(i, j) >= 0 %1
                Q(i, j) = 1;
                q1 = q1+1;
            else %4
                Q(i, j) = 4;
                q4 = q4+1;
            end
        else %2 or 3

            if Y(i, j) >= 0 %2
                Q(i, j) = 2;
                q2 = q2+1;
            else %3
                Q(i, j) = 3;
                q3 = q3+1;
            end
        end

    end
end

disp(Q);
fprintf("Points in Q1: %i \nPoints in Q2: %i \nPoints in Q3: %i \nPoints in Q4: %i \n", q1, q2, q3, q4);
