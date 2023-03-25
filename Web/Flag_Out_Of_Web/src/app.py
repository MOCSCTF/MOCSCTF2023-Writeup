from flask import *

app = Flask(__name__)

@app.route("/")
def home():
        output = request.args.get('name')        
        if output:
                output = render_template_string('Hello ' + output + "!")
        else:
                output = render_template_string('Please give me a name.')
        return output
        

if __name__ == "__main__":
    app.run(debug=True)
