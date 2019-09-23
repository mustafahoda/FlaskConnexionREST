from flask import Flask, render_template
import connexion

# Create the application instancre
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for the '/'
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)