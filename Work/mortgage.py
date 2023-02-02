# mortgage.py
#
# Exercise 1.7

principal = 500000
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment_start_month = 5*12
extra_payment_end_month = (5+4)*12 
extra_payment = 1000


while principal > 0:
    if extra_payment_start_month <= months < extra_payment_end_month:
        payment = 2684.11 + extra_payment
    elif months == extra_payment_end_month:
        payment = 2684.11

    payment = min(payment,principal* (1+rate/12))
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    months = months + 1
    print(months,round(total_paid,2),round(principal,2))

#print('Total paid', total_paid)
#print('Number of months',months)
print(f'${total_paid:0.2f} Total paid in {months} months')