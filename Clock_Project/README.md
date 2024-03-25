# Read Me
# Digital Clock

This is a simple Python script to create a digital clock using OpenCV (cv2). The script draws a clock face with hour bars, minute dots, and clock hands to represent the current time. It continuously updates the time and displays it on the screen.

## Dependencies
- Python 3.x
- OpenCV (cv2)
- NumPy

## Installation
1. Make sure you have Python installed. You can download it from [python.org](https://www.python.org/).
2. Install OpenCV and NumPy using pip:
    ```
    pip install opencv-python numpy
    ```

## Usage
1. Clone the repository:
    ```
    git clone https://github.com/Kaptan-Usama/OpenCV_Projects.git
    ```
2. Navigate to the project directory:
    ```
    cd OpenCV_Projects/Clock_Project
    ```
3. Run the script:
    ```
    python main.py
    ```
4. Press 'q' to quit the application.

## Script Explanation
- The script defines a set of colors and fonts for drawing.
- It contains functions to draw the clock structure, including hour bars, minute dots, and clock hands.
- The `draw_structure()` function draws the clock face.
- The `draw_hands()` function draws the clock hands according to the current time.
- Inside the `if __name__ == '__main__':` block, the script continuously updates the clock and displays it on the screen until the 'q' key is pressed.

Feel free to modify the script according to your needs. Enjoy your digital clock!
