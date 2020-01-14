# class Bmi:
#     height = float(input('Please enter your height input meters(decimals): '))
#     weight = int(input('Please enter your weight input kg: '))se
def bmi_calc(weight, height):
    if(height>0 and weight>0):
        bmi = int(weight / (height * height))
    elif height==0:
        return "Divide by zero"
    elif height<0 or weight<=0:
        return "Ivalid value"
    return bmi


def bmi_toweight(bmi):
    if bmi <= 18.5:
        print('Your BMI is', bmi, 'which means you are underweight.')
        return "underweight"

    elif bmi > 18.5 and bmi < 25:
        print('Your BMI is', bmi, 'which means you are normal.')
        return "normal"

    elif bmi > 25 and bmi < 30:
        print('your BMI is', bmi, 'overweight.')
        return "overweight"
    elif bmi > 30:
        print('Your BMI is', bmi, 'which means you are obese.')
        return "obese"
    else:
        print('There is an error with your input')
        print('Please check you have entered whole numbers\n'
              'and decimals were asked.')
        return None



