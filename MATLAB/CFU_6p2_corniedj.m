% CFU MATLAB
% File: CFU_6p2_corniedj.m
% Date: 15 February 2023
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
% Describe the growth of a fish using the von Bertalanffy growth law

clear; clc

T = (0:.1:2);
Lmax = 100;
t = 0.5;

hold on
k1 = .25;
f1 = Lmax*(1-exp(-k1*(T+t)));
k2 = .5;
f2 = Lmax*(1-exp(-k2*(T+t)));

grid
plot(T, f1, 'bo-', T, f2, 'ro-');
title("Fish Growth Over Time:")
xlabel('Time in Years:')
ylabel('Length in cn:')
legend("Fish One", "Fish Two");
