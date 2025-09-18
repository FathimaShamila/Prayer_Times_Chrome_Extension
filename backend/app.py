from flask import Flask, jsonify,request
from flask_cors import CORS
from datetime import datetime
import praytimes
from timezonefinder import TimezoneFinder
import pytz

app = Flask(__name__,static_url_path='',static_folder='static') 
CORS (app)
pt = praytimes.PrayTimes('ISNA')
tf = TimezoneFinder()

@app.route("/")
def home():
    return app.send_static_file("index.html")
@app.route("/prayer-times")
def prayer_times():
    try:
        #Get lat and lon from query parameters
        lat = 41.8781
        lon = -87.698
        timezone_str = "America/Chicago"

    #Get current time in that timezone
        tz = pytz.timezone(timezone_str)
        now = datetime.now(tz)

    # Get timezone offset in hours
        offset_hours = now.utcoffset().total_seconds() / 3600

    # Calculate prayer times

        times = pt.getTimes(now.date(), (lat,lon), offset_hours)

        # Sorting the prayertimes by order

        order = [ "fajr","sunrise", "dhuhr", "asr","maghrib","sunset","isha","midnight"]

        filtered_times = {prayer: times[prayer] for prayer in order if prayer in times}
        return jsonify({
            "date": now.strftime("%Y-%m-%d"),
            "timezone": timezone_str,
            "times": filtered_times
        })
    except Exception as e:
        print("Error:", e)  # logs to terminal
        return jsonify({"error": str(e)}), 500 

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5001, debug = True)



