'''
starting_term = float(input("Please enter the starting term of the geometric series you want to find the sum of: "))
common_ratio = float(input("Enter its common ratio: "))
number_of_terms = int(input("Enter the number of terms in this sequence: "))
'''

def geometric_series_sum():
    a = starting_term
    r = common_ratio
    n = number_of_terms
    print(sum([a * r ** i for i in range(n)]))


def arithmetic_series_sum(common_difference):
    a = starting_term
    d = common_difference
    m = number_of_terms
    print(sum([a + d * i for i in range(m)]))


def harmonic_mean(num1, num2):
    print((2 * num1 * num2) / (num1 + num2))


#geometric_series_sum()

def feet_at_which_oxygen_becomes_toxic(oxygen_percentage):
    if 100 < oxygen_percentage:
        print(" Oxygen percentage cannot be greater than 100")
    else:
        oxygen_part = oxygen_percentage/100
        atmospheres = 1.6/oxygen_part
        end_result = (atmospheres-1)*10*3.28
        print(" Oxygen toxicity comes at " + str(end_result))

feet_at_which_oxygen_becomes_toxic(101)




