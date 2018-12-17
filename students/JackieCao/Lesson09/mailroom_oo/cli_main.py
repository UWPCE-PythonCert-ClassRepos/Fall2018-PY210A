
#!/usr/bin/env python
"""
Command line interface for mailroom
"""

import sys
import math

from donor_models import Donor, DonorDB, get_sample_data

db = DonorDB(get_sample_data())

def print_donor_report():
    print(db.generate_donor_report())

def send_thank_you():
    while True:
        name = input("Enter a donor's name"
                     "(or 'list' to see all donors or 'menu' to exit)> ").strip()
        if name == "list":
            print(db.list_donors())

        elif name == "menu":
            return
        else:
            break

