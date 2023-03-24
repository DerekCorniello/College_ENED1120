clear; clc;
pH = input("Enter pH: ");

if (pH < 0 || pH > 14)
    fprintf("Invalid pH")
elseif (pH < 7)
    fprintf("Acidic")
elseif (pH > 7)
    fprintf("Basic")
else
    fprintf("Neutral")
end
fprintf("\n")