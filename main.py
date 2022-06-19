from ssl import DER_cert_to_PEM_cert
from flask import Flask,jsonify,request,render_template
from firebase_admin import credentials, firestore, initialize_app, auth
app = Flask(__name__)

cred = credentials.Certificate('api\key.json')
default_app = initialize_app(cred)
db = firestore.client()

@app.route('/ping')
def getPing():
    return 'pong'

@app.route('/usuario' , methods=['GET'])
def getUsers():
    users = dict()
    for user in auth.list_users().iterate_all():
        users[f'{user.email}'] = user.uid
    return jsonify(users), 200

@app.route('/infoUser', methods=['GET'])
def getUsers():
    todo_id = request.args.get('uid')
    todo_ref = db.collection(u'usuario').document(todo_id).collection(u'infoUser')
    try:
        all_todos = [doc.to_dict() for doc in todo_ref.stream()]
        return jsonify(all_todos), 200
    except Exception:
        return render_template('data_error.html')

if __name__ == '__main__':
    app.run(debug= True, port= 4000)



