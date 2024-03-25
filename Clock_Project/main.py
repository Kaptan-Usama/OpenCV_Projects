import cv2
import numpy as np
import datetime
import math

colors = {
    'red': (0, 0, 255),
    'green': (0, 255, 0),
    'blue': (255, 0, 0),
    'yellow': (0, 255, 255),
    'purple': (255, 0, 255),
    'cyan': (255, 255, 0),
    'white': (255, 255, 255),
    'black': (0, 0, 0)
}

fonts = [
    cv2.FONT_HERSHEY_SIMPLEX,
    cv2.FONT_HERSHEY_COMPLEX,
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
    cv2.FONT_HERSHEY_DUPLEX,
    cv2.FONT_HERSHEY_PLAIN,
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
    cv2.FONT_ITALIC,
    cv2.FONT_HERSHEY_TRIPLEX
]

# Function to draw a clock, hours bars and minutes dots
def draw_structure(canvas, center, radius):
    for i in range(0, 60):
        angle = math.radians(i * 6) - math.pi / 2
        x = int(center[0] + radius * math.cos(angle))
        y = int(center[1] + radius * math.sin(angle))
        if i % 5 == 0:
            if i == 0:
                cv2.putText(canvas, '12', (x - 10, y + 10), cv2.FONT_HERSHEY_DUPLEX, 1, colors['black'], 1)
            elif i == 5:
                cv2.putText(canvas, 'One', (x - 10, y + 10), cv2.FONT_HERSHEY_DUPLEX, 1, colors['black'], 1)
            elif i == 10:
                cv2.putText(canvas, 'Two', (x - 10, y + 10), cv2.FONT_HERSHEY_DUPLEX, 1, colors['black'], 1)
            elif i == 15:
                cv2.putText(canvas, 'Three', (x - 10, y + 10), cv2.FONT_HERSHEY_DUPLEX, 1, colors['black'], 1)
            elif i == 20:
                cv2.putText(canvas, 'Four', (x - 10, y + 10), cv2.FONT_HERSHEY_DUPLEX, 1, colors['black'], 1)
            elif i == 25:
                cv2.putText(canvas, 'Five', (x - 10, y + 10), cv2.FONT_HERSHEY_DUPLEX, 1, colors['black'], 1)
            elif i == 30:
                cv2.putText(canvas, '6', (x - 10, y + 10), cv2.FONT_HERSHEY_DUPLEX, 1, colors['black'], 1)
            elif i == 35 or i == 55 or i == 40 or i == 50:
                cv2.circle(canvas, (x, y), 7, colors['black'], -1)
            elif i == 45:
                cv2.putText(canvas, '9', (x - 10, y + 10), cv2.FONT_HERSHEY_DUPLEX, 1, colors['black'], 1)
        # Draw Center Dot
        cv2.circle(canvas, center, 5, colors['black'], -1)
        # Draw Logo
        cv2.putText(canvas, 'Digital Clock', (center[0] - 50, center[1] + 50), fonts[3], .6, colors['black'], 1)

# Function to draw the clock hands
def draw_hands(canvas, center, radius):
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    
    # Draw Time
    time = now.strftime('%I:%M:%S %p')
    cv2.putText(canvas, time, (center[0] - 80, center[1] - 50), fonts[3], .8, colors['red'], 1)
    # lines around the time
    cv2.rectangle(canvas, (center[0] - 90, center[1] - 80), (center[0] + 90, center[1] - 40), colors['black'], 1)

    # Draw Hour Hand
    angle = math.radians((hour % 12) * 30 + minute / 2) - math.pi / 2
    x = int(center[0] + radius * 0.5 * math.cos(angle))
    y = int(center[1] + radius * 0.5 * math.sin(angle))
    cv2.line(canvas, center, (x, y), colors['black'], 3)

    # Draw Minute Hand
    angle = math.radians(minute * 6) - math.pi / 2
    x = int(center[0] + radius * 0.7 * math.cos(angle))
    y = int(center[1] + radius * 0.7 * math.sin(angle))
    cv2.line(canvas, center, (x, y), colors['black'], 2)

    # Draw Second Hand
    angle = math.radians(second * 6) - math.pi / 2
    x = int(center[0] + radius * 0.9 * math.cos(angle))
    y = int(center[1] + radius * 0.9 * math.sin(angle))
    cv2.line(canvas, center, (x, y), colors['red'], 1)

if __name__ == '__main__':
    center = (250, 250)
    radius = 200
    while True:
        canvas = np.ones((500, 600, 3), dtype='uint8') * 255
        draw_structure(canvas, center, radius)
        draw_hands(canvas, center, radius)
        cv2.imshow('Clock', canvas)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
