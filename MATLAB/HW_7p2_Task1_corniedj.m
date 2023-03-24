% HW 7.2 Matlab
% File: HW_7p2_Task1_corniedj.m
% Date: 24 February 2023
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
% Generate matrices with magic numbers

clear; clc

n = input("Please Enter n (integer at or above 2): ");
while(n < 2 || mod(n, 1) ~= 0)
    n = input("Please Enter n (integer at or above 2): ");
end

m = input("Please Enter m (integer at or above 1): ");
while(m < 1 || mod(m, 1) ~= 0)
    m = input("Please Enter m (integer at or above 1): ");
end

magicNum = (n*((n^2) + 1))/2;
goodArrays = 0;
goodRows = 0;
goodCols = 0;
goodSemis = 0;

for k = 1:m

%     This will do the same thing, but with a lot more processing
%     acceptableMatrix = false;
%     X = randi([1 n*n],n,n);
%    
%     while(~acceptableMatrix)
%         if length(unique(X)) ~= numel(X)
%             X = randi([1 n*n],n,n);
%         else
%             acceptableMatrix = true;
%         end
%     end

isGoodSemi = false;

P = randperm(n^2);
X = reshape(P, [n, n]);

badNum = 0;

    for j = 1:n

        rowSum = 0;

        for i = 1:n 
            rowSum = rowSum + X(i, j);
        end

        if (rowSum ~= magicNum)
            badNum = badNum + 1;
        else
            goodRows = goodRows + 1;
        end
       
        colSum = 0;

        for i = 1:n 
            colSum = colSum + X(j, i);
        end

        if (colSum ~= magicNum)
            badNum = badNum + 1;
        else
            goodCols = goodCols + 1;
        end

    end

    if badNum == 0
       isGoodSemi = true; 
    end

    diagSum1 = 0;

    for i=1:n
        diagSum1 = diagSum1 + X(i, i);  
    end

    if (diagSum1 ~= magicNum)
        badNum = badNum + 1;
    end

    diagSum2 = 0;

    for i=1:n
        diagSum2 = diagSum2 + X(i, n-i+1);
    end

    if (diagSum2 ~= magicNum)
        badNum = badNum + 1;
    end

    if (badNum == 0)
        goodArrays = goodArrays + 1;

    elseif (isGoodSemi)
        goodSemis = goodSemis + 1;
    end

end

fprintf("The number of magic arrays is: %i.\n", goodArrays);
fprintf("The number of semimagic arrays is: %i.\n", goodSemis);
fprintf("The number of magic rows is: %i.\n", goodRows);
fprintf("The number of magic columns is: %i.\n", goodCols);