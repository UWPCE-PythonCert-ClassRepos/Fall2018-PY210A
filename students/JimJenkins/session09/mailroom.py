#!/usr/bin/env python3

class Donor:
    def __init__(self, name):
        self.name = name
        self.donations = []

    def add_donation(self, donation):
        self.donations.append(donation)

    @property
    def num_donations(self):
        return len(self.donations)


#@lastdonation
#@sumdonations


class donor_collection():
