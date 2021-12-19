# QR Code Generator (Python)

I wanted to experiment if there was an easy way to generate a QR code using Python. Turns out there's a Python library - pyqrcode you can use to do that. You can then use the `pypng` library to render the code as a PNG or an SVG image. 

### Create a virtual environment (optional)
```virtualenv venv -p python3```

### Activate the virtual environment 
```source venv/bin/activate```

### Install Dependencies
```pip3 install -r requirements.txt```

### Generate the QR Code
```python3 generate-qr-code.py```