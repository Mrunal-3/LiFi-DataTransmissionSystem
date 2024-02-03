import cv2
import numpy as np

def find_largest_square_contour(captured_image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(captured_image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and improve contour detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use Canny edge detector to find edges
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours in the edges image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours to find squares
    squares = []
    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        if len(approx) == 4 and cv2.isContourConvex(approx):
            squares.append(approx)

    # Find the largest square contour
    largest_square = max(squares, key=cv2.contourArea, default=None)

    return largest_square

def highlight_square(frame, square_contour):
    # Draw a rectangle around the detected square
    if square_contour is not None:
        cv2.drawContours(frame, [square_contour], -1, (0, 255, 0), 2)

    return frame

def decode_and_display():
    capture = cv2.VideoCapture(0)

    # Initialize camera window
    cv2.namedWindow("Camera Output")

    while True:
        # Capture frame from the camera
        ret, frame = capture.read()

        # Find and highlight the square
        square_contour = find_largest_square_contour(frame)
        frame_with_highlight = highlight_square(frame.copy(), square_contour)

        # Display the camera output with highlighted square
        cv2.imshow("Camera Output", frame_with_highlight)

        # Check for key press
        key = cv2.waitKey(1) & 0xFF

        # 'q' key to exit the loop
        if key == ord('q'):
            break

    # Release the camera and close all windows
    capture.release()
    cv2.destroyAllWindows()

if _name_ == "_main_":
    decode_and_display()