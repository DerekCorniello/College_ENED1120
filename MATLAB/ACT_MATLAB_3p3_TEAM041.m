clear; clc

T = [7 9 -8 9 3 -8 -5 1 10 10 0 -7];
sumPos = 0;
numPos = 0;
for i = 1:length(T)
    if(i > 0)
        sumPos = sumPos + T(i);
        numPos = numPos + 1;
    end
end

fprintf(sumPos/numPos);

sumNeg = 0;
numNeg = 0;
for i = 1:length(T)
    if(i <= 0)
        sumNeg = sumNeg + T(i);
        numNeg = numNeg + 1;
    end
end

fprintf(sumNeg/numNeg);