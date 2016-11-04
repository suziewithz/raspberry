from motor.stepper_motor import StepperMotor
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/run")
def run_steps():
    stepper_motor = StepperMotor()
    stepper_motor.roll()
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
