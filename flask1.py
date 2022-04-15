from flask import Flask,render_template,request
import spacy
nlp = spacy.load("en_core_web_sm")
app = Flask(__name__)

text = ""
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/add", methods = ['POST', 'GET'])
def add():
    text = request.form.get("Field1")
    doc = nlp(text)
    # for ent in doc.ents:
    #     print(ent.text, ent.start_char, ent.end_char, ent.label_)
    return render_template('output.html',doc = doc)

app.run()