"""from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey"""


from flask import Flask, request, render_template,jsonify,redirect,url_for
app = Flask(__name__)



@app.route('/')
def home():
	return render_template('about.html')

@app.route('/sign_in')
def sign_in():
	return render_template('sign_in.html')


@app.route('/login', methods=['GET','POST'])
def my_form_post():
    if request.method=="POST":
        username = request.form['username']
        password = request.form ['password']
        if username=="disha@gmail.com" and password=="1234567":
            return redirect(url_for('patient_info'))

    
    return redirect(url_for('sign_in'))

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=="GET":
	    return render_template('signup.html')
    if request.method=="POST":
        username = request.form['email']
        password = request.form ['password']
        #add this to database
        return redirect(url_for('sign_in'))
    return redirect(url_for('sign_in'))


@app.route('/patient_info',methods=['GET','POST'])
def patient_info():
    if request.method=="GET":
	    return render_template('patient_info.html')
    if request.method=="POST":
         text1 = request.form['text1']
         #take all the request parameters and put in database and return to confitm page
         return redirect(url_for('confirm'))


@app.route('/confirm')
def confirm():
	return render_template('confirm.html')


"""serviceUsername = "be1739fb-a7e4-4484-bfe6-b257393eb16b-bluemix"
servicePassword = "49c0c343d225623956157d94b25d574586f26d1211e8e589646b4713d5de4801"
serviceURL = "https://be1739fb-a7e4-4484-bfe6-b257393eb16b-bluemix.cloudantnosqldb.appdomain.cloud"

client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()

databaseName = "remote_doctor"
myDatabaseDemo = client.create_database(remote_doctor)

if myDatabaseDemo.exists():
    print("'{0}' successfully created.\n".format(remote_doctor))

"""



if __name__ == '__main__':
    app.run(debug=True)
