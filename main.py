from ssl import DER_cert_to_PEM_cert
from flask import Flask,jsonify,request,render_template
from firebase_admin import credentials, firestore, initialize_app, auth
app = Flask(__name__)

cred = credentials.Certificate('api\key.json')
default_app = initialize_app(cred)
db = firestore.client()

@app.route('/ping')
def getPing():
    return 'Hello world!'

@app.route('/usuario' , methods=['GET'])
def getUsers():
    users = dict()
    for user in auth.list_users().iterate_all():
        users[f'{user.email}'] = user.uid
    return jsonify(users), 200

if __name__ == '__main__':
    app.run(debug= True, port= 4000)



