import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QColor

def rgb_to_hsl(r, g, b):
    # Convert RGB values to [0, 1] range
    r = r / 255.0
    g = g / 255.0
    b = b / 255.0
    
    # Find the minimum and maximum values of R, G and B
    cmin = min(r, g, b)
    cmax = max(r, g, b)
    
    # Calculate the difference between the maximum and minimum values
    delta = cmax - cmin
    
    # Calculate hue
    if delta == 0:
        h = 0
    elif cmax == r:
        h = ((g - b) / delta) % 6
    elif cmax == g:
        h = (b - r) / delta + 2
    else:
        h = (r - g) / delta + 4
        
    # Convert hue to degrees
    h = round(h * 60)
    
    # Calculate lightness
    l = (cmax + cmin) / 2
    
    # Calculate saturation
    if delta == 0:
        s = 0
    else:
        s = delta / (1 - abs(2 * l - 1))
        
     # Return HSL values in degrees and percentages 
    return h, round(s * 100), round(l * 100)

class MyLabel(QLabel):
    
   def __init__(self):
        super().__init__()
        screen = app.desktop().screenGeometry()
        self.setGeometry(screen)
        pixmap = QPixmap("image.jpg")
        self.setPixmap(pixmap)
        self.setScaledContents(True)
       
   def mousePressEvent(self, event):
        x = event.x()
        y = event.y()
       
        # Get RGB value of clicked pixel 
        color = QColor(self.pixmap().toImage().pixel(x,y))
       
        # Convert RGB to HSV 
        hsv_color= color.toHsv()
       
        # Convert RGB to HSL 
        hsl_color= rgb_to_hsl(color.red(), color.green(), color.blue())
       
        # Update labels with color values 
        rgb_label.setText(f"R:{color.red():3d} G:{color.green():3d} B:{color.blue():3d}")
        hsv_label.setText(f"H:{hsv_color.hue():3d} S:{hsv_color.saturation():3d} V:{hsv_color.value():3d}")
        hsl_label.setText(f"H:{hsl_color[0]:3d} S:{hsl_color[1]:3d} L:{hsl_color[2]:3d}")

app= QApplication(sys.argv)

# Create a widget for layout 
widget= QWidget()

# Create a horizontal layout 
layout= QVBoxLayout()

# Create labels for displaying color values 
rgb_label= QLabel("R: , G: , B:")
hsv_label= QLabel("H: , S: , V:")
hsl_label= QLabel("H: , S: , L:")

# Add labels to layout 
layout.addWidget(rgb_label)
layout.addWidget(hsv_label)
layout.addWidget(hsl_label)

# Set layout to widget 
widget.setLayout(layout)

# Create a label for displaying image 
label= MyLabel()

# Show widget and label 
widget.show()
label.show()

sys.exit(app.exec_())