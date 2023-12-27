%Read the file
file1 = fileread('c_output.txt');
file2 = fileread('Prolog_output.txt');
file3 = fileread('Haskell_output.txt');



%Convert output array to unsigned int
output_array1 = uint8(str2num(file1));
output_array2 = uint8(str2num(file2));
output_array3 = uint8(str2num(file3));
%Save the array as a matrix
resized_matrix1 = reshape(output_array1, 256, 256);
resized_matrix2 = reshape(output_array2, 256, 256);
resized_matrix3 = reshape(output_array3, 256, 256);




%Show the images
subplot(2,2,1), imshow('Mickey.png'), title('Original Image')
subplot(2,2,2), imshow(resized_matrix1), title('Black and White From C')
subplot(2,2,3), imshow(resized_matrix2), title('Rotated With Prolog')
subplot(2,2,4), imshow(resized_matrix3), title('Color Flipped With Haskell')


%Pause for 10 seconds to show the image
pause(15);

exit;





