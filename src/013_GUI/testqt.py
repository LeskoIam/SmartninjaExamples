import sys
from PyQt4 import Qt
from PyQt4.QtGui import QApplication, QWidget

__author__ = 'mpolensek'
# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.

# Create an PyQT4 application object.
a = QApplication(sys.argv)

# The QWidget widget is the base class of all user interface objects in PyQt4.
w = QWidget()

# Set window size.
w.resize(320, 240)

w.setStyleSheet("QWidget {background-color: blue;}")

# Set window title
w.setWindowTitle("Hello World!")

# Show window
w.show()

sys.exit(a.exec_())
