donation_list = [('John Roberts', [100, 200, 300]),
                ('Clarence Thomas', [200, 400, 600]),
                ('Ruth Bader-Ginsberg', [700, 100, 2000]),
                ('Elena Kagen', [1800, 2300, 7000]),
                ('Sonia Sotomayor', [500, 190, 212, 55]),
                ('Neil Gorsuch', [100, 3000]),
                ('Brett Kavanaugh',[400, 4500]),
                ('Samuel Alito', [1000, 1000, 1000]),
                ('Stephen Breyer', [200, 300, 10000])]

print(donation_list)

# ("{} | {} | {} | {}".format('Donor Name:', 'Total Given:', 'Num Gifts:', 'Average Gift:'))

i = 0
print(donation_list[i][0])
#print(sum(donation_list[i][0]))

print(sum(donation_list[i][1]))

user = donation_list[i][1]

def average(a):
    return sum(a) / len(a)

def count(a):
    return len(a)

print('sum: ', sum(user))
print('average: ', average(user))
print('count: ', count(user))
