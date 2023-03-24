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

functionChoice = menu("What type of function do you want?", "Sine", "Cosine", "Exponential");

if (functionChoice == 1)
elseif (functionChoice == 2)
elseif (functionChoice == 3)
else
    fprintf("Please make a selection from the menu. \n")
    