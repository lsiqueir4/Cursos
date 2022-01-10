from flask import Flask
app = Flask(__name__)

@app.route("/<numero>", methods=['GET', 'POST'])
def hello(numero):
    return f"Hello World!{numero}"

if __name__=="__main__":
    app.run()