from flask import Flask, render_template, g, request
import http.client
import sys

conn = http.client.HTTPSConnection("informacion-vehiculos-de-mexico.p.rapidapi.com")

headers = {
    'Authorization': "undefined",
    'X-RapidAPI-Key': "4a19ca0119mshf54c0d0660f3a27p170b06jsn5bb8da911720",
    'X-RapidAPI-Host': "informacion-vehiculos-de-mexico.p.rapidapi.com"
    }

app = Flask(__name__)

plateVin = ''

print(sys.version)

#ruta de home
@app.route('/')
def home():
    #return '<h1>hello World!</h1>'
    return render_template('home.html')

@app.route('/', methods=['POST'])
def home_post():
    auxText = request.form['plate']
    plateVin = auxText.upper()
    conn.request("GET", "/api/repuve3/private/"+plateVin+"/", headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    return data.decode("utf-8")

if __name__ == "__main__":
    app.run(debug=True)