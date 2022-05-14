from flask import redirect, render_template


class CalcController():
  def sub(num1, num2):
    return f'Sub = {int(num1) - int(num2)}'

class Index():
  def index():
    return render_template('index.html')
  