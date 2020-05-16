# 2017BTECS00080_2017BTECS00082
DIP Assignment:- Detect lines present in the Image.


To detect Lines present in the image...

Note:- To run this code on your device, you need library of OpenCV thats it...!!

you can see a image of sudoku.png..
and two extra images result1.png for edge detction and result2.png for line detection created because of this first image.

here is the explanation of code...
everything is same as simple image processing that is...

imread() to read an image...
imshow() to display image.. 
etc..

except the new features explained below...

OpenCV implements two kind of Hough Line Transforms

Difference:-
1. The Standard Hough Transform:-
	It gives you as result a vector of couples (\theta, r_{\theta})
	In OpenCV it is implemented with the function HoughLines

2. The Probabilistic Hough Line Transform:-
	A more efficient implementation of the Hough Line Transform. It gives as output the extremes of the detected lines (x_{0}, y_{0}, x_{1}, y_{1})
	In OpenCV it is implemented with the function HoughLinesP



1) The Standard Hough Transform  (HoughLines method):-

	lines = cv.HoughLines(image, rho, theta, threshold) 
	image : source image.
	lines : Output vector of lines. Each line is represented by a 2 or 3 element vector (ρ,θ) or (ρ,θ,votes) . 
	       ρ is the distance from the coordinate origin (0,0) (top-left corner of the image). θ is the line rotation angle in 	radians . votes is the value of accumulator.
	rho : Distance resolution of the accumulator in pixels.
	theta : Angle resolution of the accumulator in radians.
	threshold : Accumulator threshold parameter. Only those lines are returned that get enough votes ( greater then threshold ).



2) The Probabilistic Hough Line Transform  (HoughLinesP method):-

	lines=cv.HoughLinesP(image, rho, theta, threshold[, lines[, minLineLength[, maxLineGap]]])
	rho : Distance resolution of the accumulator in pixels.
	theta: Angle resolution of the accumulator in radians.
	threshold:Accumulator threshold parameter. Only those lines are returned that get enough votes ( greater then threshold ).
	minLineLength : Minimum length of line. Line segments shorter than this are rejected.
	maxLineGap  : Maximum allowed gap between line segments to treat them as a single line.



					thank you...!!
