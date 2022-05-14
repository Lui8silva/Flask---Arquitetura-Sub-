from flask import Flask
from controllers import Index, CalcController

app = Flask('app')

@app.route('/')
def index():
    return Index.index()

@app.route('/sub/<num1>/<num2>')
def sub(num1, num2):
  return CalcController.sub(num1, num2)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)