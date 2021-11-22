from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    url='https://goquotes-api.herokuapp.com/api/v1/random?count=1'
    res=requests.get(url)
    data=res.json()
    quote=data['quotes'][0]['text']
    author=data['quotes'][0]['author']


    return render_template('index.html',quote=quote,author=author)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port='5000')

