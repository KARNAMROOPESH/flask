from flask import Flask , jsonify , request

web = Flask(__name__)
tasks = [
    {'id': 1, 'title': u'do hw',
        'description': u'the subjects are math , social , science', 'status': False},
    {'id': 2, 'title': u'clean room',
        'description': u'the rooms to be cleaned are the none next to the hall and kitchen', 'status': False}
]


@web.route("/")
def print():
    return "HELLO"

@web.route("/get-data")
def get_task():
    return jsonify({ 
        "data":tasks
    })

@web.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json :
        return jsonify({
            "status":"error",
            "message":"Please provide the data"
        },400)
    task = {
        'id':tasks[-1]['id']+1 ,
        'title':request.json['title'],
        'description':request.json.get("descrition" , ""),
        'status':False
    }
    tasks.append(task)
    return jsonify({
        'status':"sucess",
        'message':"Task added sucessfully"
    })

if __name__ == "__main__":
    web.run(debug=True)
