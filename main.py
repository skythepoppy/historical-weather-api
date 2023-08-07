from flask import Flask, render_template

app = Flask(__name__)  # website object


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/api/v1/<station>/<date>")   # contains the link to about // route to about
def about(station, date):
    temperature = 23
    return {"station": station,
            "date" : date,
            "temperature" : temperature}      # flask searches root directory 'templates' for about.html

if __name__  ==  "__main__" :
    app.run(debug=True)

