from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_bmi():
    height_feet = height_feet_input(request.form['height_feet'])
    height_inches = height_inches_input(request.form['height_inches'])
    weight = weight_input(request.form['weight'])
    bmi_category, bmi = bmi_calc(height_feet, height_inches, weight)
    return f"You are {bmi_category}. BMI: {bmi}"

def height_feet_input(height_feet_str):
    height_feet = float(height_feet_str)
    return height_feet

def height_inches_input(height_inches_str):
    height_inches = float(height_inches_str)
    return height_inches

def weight_input(weight_str):
    weight = float(weight_str)
    return weight

def bmi_calc(height_feet, height_inches, weight):
    bmi = (weight*.45)/((((height_feet*12)+height_inches)*0.025)*(((height_feet*12)+height_inches)*0.025))
    category = "NULL"
    if(round(bmi, 1) < 18.5):
        print("You are underweight. BMI:", round(bmi, 1))
        category = "underweight"
    elif(round(bmi, 1) >= 18.4 and round(bmi, 1) <= 24.9):
        print("You are normal weight. BMI:", round(bmi, 1))
        category = "normal"
    elif(round(bmi, 1) >= 25.0 and round(bmi, 1) <= 29.9):
        print("You are overweight. BMI:", round(bmi, 1))
        category = "overweight"
    elif(round(bmi, 1) >= 30.0):
        print("You are obese. BMI:", round(bmi, 1))
        category = "obese"
    
    return (category, round(bmi, 1))

if __name__ == '__main__':
    app.run(debug=True)
