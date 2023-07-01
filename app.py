from flask import Flask, request, render_template
import languagemodels as lm

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send-message", methods=["POST"])
def send_message():
    message = request.form.get("input-message")
    
    response = lm.do(str(message))

    return response

if __name__ == "__main__":
    app.run(debug=True)

