
def height_feet_input():
  height_feet = float(input('What is the feet portion of your height?\n'))
  return(height_feet)

def height_inches_input():
  height_inches = float(input('What is the inches portion of your height?\n'))
  return height_inches

def weight_input():
  weight = float(input('What is your weight?\n'))
  return (weight)

def bmi_calc(height_feet, height_inches, weight):
  bmi = (weight*.45)/((((height_feet*12)+height_inches)*0.025)*(((height_feet*12)+height_inches)*0.025))
  category = "NULL"
  if(round(bmi, 1) < 18.5):
    print("You are underweight. BMI:", round(bmi, 1))
    category = "Underweight"
  elif(round(bmi, 1) >= 18.4 and round(bmi, 1) <= 24.9):
    print("You are normal weight. BMI:", round(bmi, 1))
    category = "Normal"
  elif(round(bmi, 1) >= 25.0 and round(bmi, 1) <= 29.9):
    print("You are overweight. BMI:", round(bmi, 1))
    category = "Overweight"
  elif(round(bmi, 1) >= 30.0):
    print("You are obese. BMI:", round(bmi, 1))
    category = "Obese"
  
  return (category)

def main():
  height_feet = height_feet_input()
  height_inches = height_inches_input()
  weight = weight_input()
  bmi_calc(height_feet, height_inches, weight)

if __name__ == "__main__":
  main()
  

