clear; clc

n = input("How many datapoints do you have? ");
dataSum = 0;

for k = 1:n
    dataPoint= input("Enter a data point: ");
    dataSum = dataPoint +  dataSum;
end

avg = dataSum/n;
fprintf("The average of your data points is %0.2f.\n", avg);