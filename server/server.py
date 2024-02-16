from flask import Flask, jsonify
from flask_cors import CORS

# creates app instance
app = Flask(__name__)
CORS(app)


@app.route("/api/home", methods=['GET'])
def return_home():
    return jsonify({
        'message':"YO FAM!",
        'people':['Jack', 'Harry', 'Barry']
    })

if __name__ == "__main__":
    app.run(debug=True, port=8080) #remove debug=True once you put app to production
    
    