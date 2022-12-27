import exifread
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog

class MetadataExtractor(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    # Create a button to select a photo file
    self.btn = QtWidgets.QPushButton('Select Photo', self)
    self.btn.clicked.connect(self.showDialog)

    # Set the layout
    layout = QtWidgets.QVBoxLayout(self)
    layout.addWidget(self.btn)
    self.setLayout(layout)

  def showDialog(self):
    # Show a file dialog to select a photo file
    options = QFileDialog.Options()
    options |= QFileDialog.ReadOnly
    fileName, _ = QFileDialog.getOpenFileName(self, 'Select Photo', '', 'Images (*.jpg *.jpeg)', options=options)
    if fileName:
      # If a file was selected, extract the metadata from it
      with open(fileName, 'rb') as f:
        metadata = exifread.process_file(f)

      # Print the latitude and longitude values
      latitude = metadata.get('GPS GPSLatitude')
      longitude = metadata.get('GPS GPSLongitude')
      print(f'Latitude: {latitude}')
      print(f'Longitude: {longitude}')

if __name__ == '__main__':
  app = QtWidgets.QApplication([])
  ex = MetadataExtractor()
  ex.show()
  app.exec_()
