from math import ceil, log, floor
import sys

def nominal_interest(interest):
    return interest / 100 / 12


def payments(principal, monthly_payment, nominal_interest):

    return ceil(log(monthly_payment / (monthly_payment - nominal_interest * principal),
                    1 + nominal_interest))


def differentiated_payment(principal, nominal_interest, number_of_payments, current_period):

    return ceil(principal / number_of_payments \
           + nominal_interest * (principal - principal * (current_period - 1) / number_of_payments))


def monthly_payment(principal, number_of_payments, nominal_interest):

    return ceil(principal * formula(nominal_interest, number_of_payments))


def formula(nominal_interest, number_of_payments):
    return (nominal_interest * (1 + nominal_interest) ** number_of_payments)\
           / ((1 + nominal_interest) ** number_of_payments - 1)


def principal(monthly_payment, number_of_payments, nominal_interest):
    return floor(monthly_payment / formula(nominal_interest, number_of_payments))


def input_principal():
    return int(input('Enter the credit principal:'))


def input_monthly_payment():
    return float(input('Enter monthly payment:'))


def input_interest():
    return float(input('Enter credit interest:'))


def input_number_of_payments():
    return float(input('Enter count of periods:'))


def get_parameters(parameter_string):
    name_key = '--'
    value_key = '='
    parameter_name = parameter_string[parameter_string.find(name_key) + len(name_key)
                                      :parameter_string.find(value_key)]
    parameter_value = parameter_string[parameter_string.find(value_key) + len(value_key):]

    return parameter_name, parameter_value


def period_string(payments):

    period_string = str()

    if payments >= 12:
        years = payments // 12
        years_noun = 'year' if years == 1 else 'years'
        period_string += f'{str(years)} {years_noun}'

        months = payments % 12
    else:
        years = 0
        months = payments

    if months != 0:
        if years != 0:
            period_string += ' and '

        months_noun = 'month' if months == 1 else 'months'
        period_string += f'{str(months)} {months_noun}'

    return f'You need {period_string} to repay this credit!'


def overpayment(calculation_type, principal=0, periods=0, payment=0, total_payment=0):
    if calculation_type == 'annuity':
        param_overpayment = periods * payment - principal
    elif calculation_type == 'diff':
        param_overpayment = total_payment - principal
    return int(param_overpayment)

param_principal, param_interest, param_periods, param_payment, param_current_period = 0, 0, 0, 0, 0
param_total_payment = 0
param_calculation_type = str()

parameters = sys.argv
# parameters = ['--0=0', '--type=diff', '--principal=1000000', '--periods=10', '--interest=10'] # OK Example 1
# parameters = ['--0=0', '--type=annuity', '--principal=1000000', '--periods=60', '--interest=10'] # OK Example 2
# parameters = ['--0=0', '--type=diff', '--principal=1000000', '--payment=104000'] # OK Example 3
# parameters = ['--0=0', '--type=diff', '--principal=500000 ', '--periods=8', '--interest=7.8'] # OK Example 4
# parameters = ['--0=0', '--type=annuity', '--payment=8722', '--periods=120', '--interest=5.6'] # OK Example 5
# parameters = ['--0=0', '--type=annuity', '--principal=500000', '--payment=23000', '--interest=7.8']  # OK Example 6




for parameter in parameters[1:]:
    parameter_name, parameter_value = get_parameters(parameter)
    if parameter_name == 'principal':
        param_principal = float(parameter_value)
    elif parameter_name == 'interest':
        param_interest = float(parameter_value)
    elif parameter_name == 'periods':
        param_periods = int(parameter_value)
    elif parameter_name == 'payment':
        param_payment = float(parameter_value)
    elif parameter_name == 'current_period':
        param_current_period = int(parameter_value)
    elif parameter_name == 'type':
        param_calculation_type = parameter_value

# Check parameters
if param_principal < 0 or param_interest < 0 \
        or param_periods < 0 or param_payment < 0 \
        or param_current_period < 0:
    print('Incorrect parameters.')

if param_principal != 0 \
        and param_payment != 0 \
        and param_interest != 0 \
        and param_calculation_type == 'annuity':
    param_periods = payments(param_principal,
                             param_payment,
                             nominal_interest(param_interest))
    print(period_string(param_periods))

    print(f'Overpayment = {overpayment(param_calculation_type, param_principal, param_periods, param_payment)}')

elif param_periods != 0 \
        and param_payment != 0 \
        and param_interest != 0 \
        and param_calculation_type == 'annuity':
    param_principal = principal(param_payment, param_periods, nominal_interest(param_interest))

    print(f'Your credit principal = {param_principal}!')
    print(f'Overpayment = {overpayment(param_calculation_type, param_principal, param_periods, param_payment)}')

elif param_periods != 0 \
        and param_interest != 0 \
        and param_calculation_type == 'diff':
    for current_period in range(1, param_periods + 1):
        current_payment = differentiated_payment(param_principal, nominal_interest(param_interest),
                               param_periods, current_period)
        print(f'Month {current_period}: paid out {current_payment}')
        param_total_payment += current_payment
    print(f'Overpayment = {overpayment(param_calculation_type, principal=param_principal, total_payment=param_total_payment)}')

elif param_periods != 0 \
        and param_principal != 0 \
        and param_interest != 0 \
        and param_calculation_type == 'annuity':
    param_payment = monthly_payment(param_principal, param_periods, nominal_interest(param_interest))
    print(f'Your annuity payment = {param_payment}!')
    print(f'Overpayment = {overpayment(param_calculation_type, principal=param_principal, periods=param_periods, payment=param_payment)}')


else:
    print('Incorrect parameters.')
