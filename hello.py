from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/v1/will", methods=["GET"])
@app.route("/will", methods=["GET"])
def will():
    '''(None) -> (Dict)

    This method returns a simple message saying "Hello World"

    '''
    return jsonify(message="Hello World", status_code=200)

@app.route("/v1/health", methods=["GET"])
@app.route("/health", methods=["GET"])
def health():
    '''(None) -> (Dict)

    This method provides an arbitrary health check status.
     
    '''

    # Arbitrary health check
    return jsonify(message="UP", status_code=200) 

@app.route("/v1/ready", methods=["GET"])
@app.route("/ready", methods=["GET"])
def ready():
    '''(None) -> (Dict)

    This method returns a simple message saying "It works!"
     
    '''
    return jsonify(message="It works!", status_code=200)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)