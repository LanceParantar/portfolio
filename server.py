from flask import Flask, render_template,request, redirect
import csv
app = Flask(__name__)

@app.route("/")
def base():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_form(data):
    with open("database.csv",newline='', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter =',',quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        if data['email']:
            write_to_form(data)
            return redirect('/thankyou.html')    
        else:
            return render_template('/contact.html')
    else:
        return "oops"

