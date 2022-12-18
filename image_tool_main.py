import cv2
import math as m
from fractions import Fraction

'''
    User note(s):   opencv used BGR color space
                    1: remove index 1, returns remaining
                    :1 returns up to index 1
                    start:stop@:step by
'''

point_list = []  # For storing pixel tuple (int x, int y)
global_list = []
AA = cv2.LINE_AA    # Anti-Aliased line
line_thickness = 5
line_color = (255, 0, 0)
font = cv2.FONT_HERSHEY_SIMPLEX
marker_typ = cv2.MARKER_CROSS

# Read and show image
image = cv2.imread("images/vette_profile.jpg")
cv2.imshow("Display Window", image)  # Display image input
image_height, image_width, image_channels = image.shape

# Using diagonal as a constant - As it is the maximum length a line can be within image
image_diagonal = m.sqrt(pow(image_height, 2) + pow(image_width, 2))
image_diagonal_int = int(image_diagonal)


def click_event(event, x, y, flag, userdata):
    if event == cv2.EVENT_LBUTTONUP:

        point_list.append((x, y))   # Append tuple to empty point list
        global_list.append((x, y))  # Append tuple to global point list
        
        # print(point_list)

        for point_x, point_y in zip(point_list[0:1], point_list[1:2]):  # zip joins tuples (a, b)

            var_x = [x[0] for x in point_list]  # Gets first value in each array of provided list
            var_y = [x[1] for x in point_list]  # Gets second value in each array of provided list

            midpoint_x = int((var_x[0] + var_x[1])/2)   # Return midpoint-x and convert to integer
            midpoint_y = int((var_y[0] + var_y[1])/2)   # Return midpoint-y and convert to integer

            distance = m.sqrt(m.pow((var_x[0] - var_x[1]), 2) + m.pow((var_y[0] - var_y[1]), 2))
            distance_int = int(distance)    # Result of distance formula

            get_float = round(distance_int/image_diagonal_int, 2)   # divide line dist by max allowed dist
            get_int = int(get_float * 100)  # Move decimal place and convert to int
            convert_fraction = str(get_int)    # +"/100"
            # convert_fraction = Fraction(get_float).limit_denominator(100)

            create_line = cv2.line(image, point_x, point_y, (255, 0, 0), line_thickness, AA, 0)
            create_marker_x = cv2.drawMarker(image, point_x, (0, 255, 128), marker_typ, 20, 2, AA)
            create_marker_y = cv2.drawMarker(image, point_y, (0, 255, 128), marker_typ, 20, 2, AA)

            create_text = cv2.putText(image, str(convert_fraction), (midpoint_x, midpoint_y),
                                      font, 0.6, (125, 128, 255), 2)

            point_list.clear()  # Clear point list

        cv2.imshow("Display Window", image)

    if event == cv2.EVENT_RBUTTONUP:

        print("test")


cv2.setMouseCallback("Display Window", click_event)  # Call function for mouse event
cv2.waitKey(0)  # Wait for a keystroke in the window



