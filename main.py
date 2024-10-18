
# vulnerable_python310_project/main.py

from flask import Flask
import requests
import yaml

app = Flask(__name__)

@app.route('/')
def home():
    # Simulate unsafe loading of YAML
    data = yaml.load('foo: {bar: baz}', Loader=yaml.FullLoader)  # Potential vulnerability in older PyYAML
    return "Hello, Flask with vulnerable dependencies!"

if __name__ == '__main__':
    app.run(debug=True)
