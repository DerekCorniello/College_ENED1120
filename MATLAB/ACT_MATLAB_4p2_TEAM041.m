clear; clc

pic = imread("Arm_Fracture.jpg", "jpg");
[nrows, ncols] = size(pic);
threshold = -1;

while(threshold > 255 || threshold < 0)
    threshold =  input("Enter the threshold value between 0 and 255: ");
end

newpic = zeros(size(pic));

for row = 1:nrows
    for col = 1:ncols
        if pic(row, col) > threshold
            newpic(row, col) = 255;
        else
            newpic(row, col) = 0;
        end
    end
end

pic = uint8(pic);
newpic = uint8(newpic);

figure(1); imshow(pic);
figure(2); imshow(newpic);