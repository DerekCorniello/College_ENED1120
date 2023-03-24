% File: HW4p2_Task2_corniedj.m
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
% Generates a confidence interval based on user input

clear; clc

sampSize = input("Enter Sample Size: ");

if(sampSize > 0)
    sigmaKnown = input("Is the population standard deviation known? ", "s");
    if (sigmaKnown == "Yes")
        popStdDev = input("Enter the population standard deviation: ");
        alpha = input("Enter alpha: ");
        z = input("Enter z: ");

        E = z * (popStdDev / sqrt(sampSize));
    elseif (sigmaKnown == "No")
        isNormal = input("Is the distribution approximately normal? ","s");
        if(isNormal == "Yes")
            if(sampSize < 30)
                s = input("Enter the sample standard deviaiton: ");
                alpha = input("Enter alpha: ");
                t = input("Enter t with degree of freedom n-1: ");

                E = t*(s/sqrt(sampSize));
            else
                popStdDev = input("Enter the population standard deviation ");
                alpha = input("Enter alpha: ");
                z = input("Enter z: ");

                E = z * (popStdDev / sqrt(sampSize));
            end
        elseif(isNormal == "No")
            fprintf("Outside the scope of this project.");
        else
            fprintf("Please enter a valid answer for shape of distribution.");
        end
         
    else
        fprintf("Please enter a 'Yes' or 'No'.");
    end
    
    mean = input("Enter the mean: ");
    xL = mean - E;
    xR = mean + E;
    fprintf("Your confidence interval is (%.2f,%.2f).", xL, xR);
else
    fprintf("Please enter a valid sample size. ")
end

fprintf("\n");