from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)  # website object

# stations data frame
stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID","STANAME                                 "]]

@app.route("/")
def home():
    return render_template('home.html', data=stations.to_html())


@app.route("/api/v1/<station>/<date>")   # contains the link to about // route to about
def content(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6)+".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE']==date]['   TG'].squeeze()/10
    temperature = 23
    return {"station": station,
            "date" : date,
            "temperature" : temperature}      # flask searches root directory 'templates' for about.html

if __name__  ==  "__main__" :
    app.run(debug=True, port = 5001)    # port allows you to run multiple apps on flask

