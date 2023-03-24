% HW 5 Task 1
% File: HW_5p2_Task1_corniedj.m
% Date: 16 February 2023
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
% Plays a game with the driver and the follower

clear; clc

p1score = 0;
p2score = 0;
p1die = 0;
p2die = 0;
p1 = input("Input Player 1's name: ", 's');
p2 = input("Input Player 2's name: ", 's');

numGames = input("The number of games to play is: ");

while(p1die == p2die)
    p1die = randi([1, 6], 1);
    p2die = randi([1, 6], 1);
end

if (p1die > p2die)
    fprintf("The driver is %s and the follower is %s.\n", p1, p2);

    for k = 1:numGames
        p1die = randi([1, 6], 1);
        if (p1die == p2die)
            p2score = p2score + 1;
            fprintf("The winner of round %i is %s.\n", k, p2)
        else
            p1score = p1score + 1;
            fprintf("The winner of round %i is %s.\n", k, p1)
        end
    end

else
    fprintf("The driver is %s and the follower is %s.\n", p2, p1);

    for k = 1:numGames
        p2die = randi([1, 6], 1);
        if (p1die == p2die)
            p1score = p1score + 1;
            fprintf("The winner of round %i is %s.\n", k, p1)
        else
            p2score = p2score + 1;
            fprintf("The winner of round %i is %s.\n", k, p2)
        end
    end
end

if (p1score > p2score)
    fprintf("The winner of the game is %s.\n", p1);
elseif (p1score < p2score)
    fprintf("The winner of the game is %s.\n", p2);
else
    fprintf("The game was a tie!\n");
end

fprintf("The points for %s is %i.\n", p1, p1score)
fprintf("The points for %s is %i.\n", p2, p2score)