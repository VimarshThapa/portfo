from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/<string:filename>')
def about(filename=None):
    return render_template(filename+".html")


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"{email}, {subject}, {message}")


def write_to_csv(data):
    with open('database.csv', newline="",mode='a') as database2:
        email = data['email']
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/form-submited', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return render_template("thankyou.html")
    else:
        return "<center><h2>Something went Wrong!!</h2></center>"
