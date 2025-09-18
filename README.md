# Prayer_Times_Chrome_Extension
A lightweight Chrome extension that displays daily prayer times based on your location.
Built with HTML,CSS,JavaScript and Python(Flask) backend for dynamic calculation of prayer times.

## Features
Shows daily prayer times (Fajr,Dhuhr,Asr,Maghrib,Isha) based on your location.
Clean,responsive and user-friendly interface
Easy to install as a Chrome Extension

## Installation & Live Setup

### 1. Clone the repository

  ```
git clone https://github.com/FathimaShamila/Prayer_Times_Chrome_Extension.git
cd prayer-times-extension
```

### 2. Set up Python environment

Optional but recommended for Flask backend.

```
python -m venv venv
source venv/bin/activate #For Mac/Linux
venv\Scripts\activate   #For Windows
pip install -r requirements.txt
```

### 3. Configure location and timezone
- By default, the backend uses Chicago(America/Chicago) for demonstration.
- latitude,longitude and timezone can be updated in app.py
- Alternatively,let the frontend use browser geolocation for automatic detection.


### 4. Run the Flask backend

```
python app.py
```
- Flask will run on https://127.0.1:5001/ (index.html will be displayed)
- Open this in your browser to test that prayer times are calculated correctly.
- JSON output with prayer times will be displayed.

### 5. Load the extension in Chrome

-  Open Chrome -> chrome://extensions/
- Enable **Developer mode**(top-right)
- Click **Load unpacked**
- Select the folder containing extension files.
   Now the extension's logo should appear in the Chrome toolbar, showing live prayer times based on your location.


### Usage

- Automatically detects your location or uses default coordinates.
- Displays prayer times clearly.
- Updates daily according to the respective timezone.


### Customization

- Location: Change the latitude,longitude or timezone in app.py.
- Styling: Modify style.css for colors,fonts or layout.
- Icons: Replace icons in the icons/ folder.

### Tech Stack
- **Frontend**: HTML,CSS ,JavaScript
- **Backend**: Python(Flask)
- **Browser**: Google Chrome 



