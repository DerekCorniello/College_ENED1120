clear; clc

answer = "Y";
dataSum = 0;
n = 0;

while strcmpi(answer, "Y")
    dataPoint = input("Enter a datapoint: ");
    dataSum =+ dataPoint;
    n =+ 1;
    answer = input("Do you have another datapoint? (y/n) ", "s");
end

avg = dataSum/n;
fprintf("The average of your data points is %0.2f.\n", avg);