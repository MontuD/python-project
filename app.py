from flask import Flask, render_template,request,jsonify

app = Flask(__name__)



@app.route('/appGetMethod/<username>', methods=['GET', 'POST'])
def home(username):
    if request.method == 'POST':
        return f"Welcome, {username}!"
    return render_template('index.html')  # Render the form on GET request

# Route to accept JSON data via POST
@app.route('/api/data', methods=['POST'])
def api_data():
    data = request.get_json()  # Retrieve JSON data from the request body
    name = data.get('name')
    age = data.get('age')
    return jsonify(message=f"Received data for {name}, age {age}.")




if __name__ == '__main__':
    app.run(debug=True)