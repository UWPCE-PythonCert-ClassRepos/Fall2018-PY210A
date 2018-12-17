#!/usr/bin/env python3
import os
import sys
import math

# from textwrap import dedent

class Donor:
    """responsible for donor data encapsulation,
       This will hold all the information about a single donor.
     """
    def __init__(self, name, *args):
        self.name = name
        self.donations = []
        self.donations.extend(map(float, args))

    def donate(self, donation):
        self.donations.append(donation)


    def get_total_donation(self):
        return sum(self.donations)


    def get_num_donations(self):
        return len(self.donations)


    def get_avarage_donation(self):
        return sum(self.donations) / len(self.donations)


class DonorCollection:
    """responsible for donor collection data encapsulation,this will hold all of the donor objects,
       as well as methons to add a new donor, search for a given donor,etc.
    """
    def __init__(self):
        self.donors_info = {
            "Bill Gates": Donor("Bill Gates", 3500, 5500, 7500),
            "Paul Alen": Donor("Paul Alen", 3000, 3700, 3900),
            "Jeff Benzo": Donor("Jeff Benzo",3300, 5000, 7500),
            "Mark Zuckerberg": Donor("Mark Zuckerberg", 33565.37, 465.37, 545.37, 7506),
            "Warren Buffett": Donor("Warren Buffett", 3303.17, 334.17, 5080, 7500)
        }
    
    def add_donation(self, name, donation):
        if name in self.donors_info:
            self.donors_info[name].donate(donation)
        else:
            self.donors_info[name] = Donor(name,donation)
        return """

    Dear {},
        
        Thank you for your generous donation ${:,.2f}.

    Best regards,
    Your Youth and Seniors Foundation

            """.format(name, donation)


    def create_report(self):
        # create a report for donors contribution as a table formate.
        report = "{:<20}| {:<10} | {:<10} | {:<12}\n".format(
            "Donor Name", "Total Given", " Num Gifts", "Average Gift")
        report += "-" * 60 + "\n"
        # list comprehension here
        for name,donor in self.donors_info.items():
            report += "{:<21} ${:<15.2f} {:<10} ${:<12.2f}\n".format(
                name, donor.get_total_donation(), donor.get_num_donations(), donor.get_avarage_donation())
        return report

    def save_letter_todisk(self):
        """ Save generates thank you letter, 
        and writes each letter to disk as a text file. 
        """
        result = ""
        for name, donor in self.donors_info.items():
            with open(f"{name.replace(' ', '_')}.txt", "w") as output:
                output.write(
                    """
    Dear {},

        Thank you for your generous donation ${:,.2f}.

    Best regards,
    Your Youth and Seniors Foundation
                    """.format(name, donor.get_total_donation())
                )
            result += f"Created thank you file for {name}.\n"
        return result
    
    def list_donors(self):
        donors = ""
        for name in self.donors_info.keys():
            donors += f"- {name}\n"
        return donors


