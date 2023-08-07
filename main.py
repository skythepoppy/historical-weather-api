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
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])   # dataframe (df)
    temperature = df.loc[df['    DATE']==date]['   TG'].squeeze()/10
    temperature = 23
    return {"station": station,
            "date" : date,
            "temperature" : temperature}      # flask searches root directory 'templates' for about.html


@app.route("/api/v1/<station>")
def all_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])   # dataframe (df)
    result = df.to_dict(orient="records")   # converts dataframe into dictionary
    return result


@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)  # dataframe (df)
    df['    DATE'] = df['    DATE'].astype(str)     # convert data column as a string
    result = df[df['    DATE'].str.startswith(str(year))].to_dict(orient="records")
    return result


if __name__  ==  "__main__" :
    app.run(debug=True, port = 5001)    # port allows you to run multiple apps on flask

