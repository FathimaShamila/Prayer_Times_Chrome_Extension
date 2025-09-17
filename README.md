# Prayer_Times_Chrome_Extension
A lightweight Chrome extension that displays daily prayer times based on your location.
Built with HTML,CSS,JavaScript and Python(Flask) backend for dynamic calculation of prayer times.

## Features
Shows daily prayer times (Fjr,Dhuhr,Asr,Maghrib,Isha) based on your location.
Clean,responsive and user-friendly interface
Easy to install as a Chrome Extension

## Installation & Live Setup

### 1.Clone the repository

  ```
git clone https://github.com/FathimaShamila/Prayer_Times_Chrome_Extension.git
cd prayer-times-extension
```

### 2.Set up Python environment

Optional but recommended for Flask backend.

```
python -m venv venv
source venv/bin/activate #For Mac/Linux
venv\Scripts\activate   #For Windows
pip install -r reqiurements.txt
```

### 3.Configure location and timezone



### 4.Run the Flask backend

python app.py
- By default,Flask will run on https://127.0.1:5000/.
- Open this in your browser to test that prayer times are calculated correctly.

### 5.Load the extension in Chrome

1. Open Chrome -> chrome://extensions/
2. Enable Developer mode(top-right)
3. Click Load unpacked
4. Select the folder containing extension files.
   Now the extension's logo should appear in the Chrome toolbar, showing live prayer times based on your location.


### Usage

- Automatically detects your location or uses default coordinates.
- Displays prayer times clearly.
- Updates daily according to the respective timezone.


### Customization

- Location: Change the latitude,longitude or timezone in the backend.
- Styling: Modify style.css for colors,fonts or layout.
- Icons: Replace icons in the assets folder.

### Tech Stack
- **Frontend**: HTML,CSS ,JavaScript,Jinja templates
- **Backend**: Python Flask
- **Browser**: Google Chrome 



