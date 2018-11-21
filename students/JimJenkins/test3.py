key_list = ['name', 'donation_amount']


donor_list = ['John Roberts',
              'Clarence Thomas',
              'Ruth Bader-Ginsberg',
              'Elena Kagen',
              'Sonia Sotomayor',
              'Neil Gorsuch',
              'Brett Kavanaugh',
              'Samuel Alito',
              'Stephen Breyer']


donation_amounts = ([100, 200, 300],
                    [200, 400, 600],
                    [700, 100, 2000],
                    [1800, 2300, 7000],
                    [500, 190, 212, 55],
                    [100, 3000],
                    [400, 4500],
                    [1000, 1000, 1000],
                    [200, 300, 10000])


donation_list = dict(zip(donor_list, donation_amounts))
print(donation_list)



a = 'Elena Kagen'
b = 200

donor = str(a)

donation = int(b)

if donor in donation_list:
    
    print('donor: ', donor)
    print('donation: ${:,.2f}'.format(donation))

    print(donation_list.get(donor))

    print('New: ', donation_list.get(donor))