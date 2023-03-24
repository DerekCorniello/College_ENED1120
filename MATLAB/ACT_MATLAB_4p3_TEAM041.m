clear; clc

pic = imread("Arm_Fracture.jpg", "jpg");
figure(1); imshow(pic);
[nrows, ncols] = size(pic);

srow = input("Enter the starting row: ");
scol = input("Enter the starting column: ");
erow = input("Enter the amount of rows: ");
ecol = input("Enter the amount of columns: ");

for row = srow:srow+erow
    for col = scol:scol+ecol
        croppic(row-srow+1, col-scol+1) = pic(row, col);
    end
end

croppic = uint8(croppic);
figure(2); imshow(croppic);
