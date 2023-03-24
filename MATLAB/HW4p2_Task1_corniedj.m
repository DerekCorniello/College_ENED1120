% File: HW4p2_Task1_corniedj.m
% Date: 3 February 2023
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
% utilizes user inputs and standardized values to classify 
% the quality of bolts in a manufacturing company.

clear; clc

totalBolts = input("Total Bolts: ");
mean = input("Mean Length of Bolts: ");
stdDev = input("Sample Standard Deviation: ");
randBolt = input("Enter the size of the random bolt: ");

zScore = ((randBolt - mean)/stdDev);

if (zScore <= 1 && zScore >= -1)
    fprintf("Superior Quality!")
elseif((zScore < -1 && zScore >= -2) || (zScore <= 2 && zScore > 1))
    fprintf("Premium Quality!")
elseif((zScore < -2 && zScore >= -3) || (zScore <= 3 && zScore > 2))
    fprintf("Bad Quality!")
else
    fprintf("Poor Quality!")
end
fprintf("\n")