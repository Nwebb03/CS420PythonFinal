%Save mickey into MATLAB
image = imread('Mickey.png');

%Reshape to an array
img_1d = reshape(image, 1, []);

%Write 1d array to input.txt
dlmwrite('input.txt', img_1d, 'delimiter', ' ');

%Close
exit;