import os 
import math



class DonorCollection():
    
    def __init__(self, donor_list, name=None):
        self.name = name
        self.data_collection = donor_list
        self.title = ("Donor Name", "Total given", "Num Gifts", "Average Gift")
        self.DIR_NAME = "D_letter"

    def exist_list(self):
        return [person_name for person_name in self.data_collection]

    
    def find_donor(self):
        
        for x in self.data_collection.keys():
            print (x, "test")
            if (x == self.name):
                return True
        return False

    def create_report(self):
        report_donor = []
        print(self.data_collection, " report")

        for key, values in self.data_collection.items():    
            name = "{}".format(key)
            total_cost = sum(values)
            n_time = len(values)
            average = total_cost/n_time
            report_donor.append([name, round(total_cost, 2), n_time, round(average, 2)])

        report_donor = sorted(report_donor, key=self._sort, reverse=False)

        print("{:20}|  {:<10s}|  {:<10s}|  {: <10s} ".format(*self.title))
        print("".join(["-"] * 62))
        for x in range (len(report_donor)):
            print("{:20} $ {:10.2f} {:>12d} $ {:>12.2f}".format(*report_donor[x]))

        return report_donor

    @staticmethod
    def _sort(row_report):
        #each row record look like
        dl_name = row_report[0].split(' ')[1]
        if (len(dl_name) > 1):
            return dl_name
        else:
            return row_report[0].split(' ')[2]

    def ck_dir(self):
        if not os.path.isdir(self.DIR_NAME):
            os.mkdir(self.DIR_NAME)
            return False
        return True

    def ss_letterall(self):
    #     """
    #     This method write letter to disk as txt file

    #     params:  none
    #     will check and generate directory
    #     will write all txt file in the directory
    #     """

        #writes each letter to disk as txt file
        #open ("./thankyou.txt", "w")
        # tempfile.gettempdir() 

        for key, values in self.data_collection.items():  
            d = Donor(key)
            letter = d.generate_letter(values)
            filename = key + ".txt"
            self.ck_dir()    
            try:
                print(filename) 
                filename = os.path.join(self.DIR_NAME, filename)
                open(filename, 'w').write(letter)
            except FileNotFoundError:
                print("couldn't open missing.txt")
            finally:
                pass
    

    def add_donor(self, Donor):
        if self.find_donor() is True:
            self.data_collection[Donor.name].append(Donor.donations[0])    
        else:
            self.data_collection[Donor.name] = Donor.donations



class Donor(DonorCollection):

    def __init__(self, name, donations=None):  
        """
        Create Donor object
        param name: the full name of the donor
        param donations: the donations 
        """

        self.name = name
        if donations is None:
            self.donations = []
        else:
            self.donations = [donations]
        print("name is {}".format(self.name))
        print("donations is", self.donations)

    # @property #outside look like attribute
    def add_donations(self, amount):
        """
        Add donation amount of user input
        """
        donate_amount = self._ck_dollar(amount)
        self.donations.append(donate_amount)
    
    @property #outside look like attribute
    def num_donations(self):
        """
        measure 
        param donations: iterable donations
        """
        return len(self.donations)


    @staticmethod
    def _ck_dollar(d_amount):
        """
        This method is check if user input correct float number.
        Check if user not a nubmber or infinity number
        Check if user enter negative amount

        params amount:  input amount of dollar value
        returns amount dollar value
        """

        amount_flt = round(float(d_amount), 2)

        if math.isnan(amount_flt) or math.isinf(amount_flt):
            raise ValueError("Is not a number or infinite number")

        if amount_flt <= 0.00:
            raise ValueError("Can't be negative number")
            
        return amount_flt

    
    def validate_name(self):
        """
        This method is validate user name input

        params:  input user name
        returns true or false if name is correct input
        """

        if (self.name == " " or self.name.isdigit()):
            return False

        str_name = self.name.rstrip()
        # #parse first and last name into string
        try:
            str_name = str_name.split(' ') 
            if (str_name[1] == ' '):    
                return False
        except IndexError:
            print ("Need to have first and last name within space between")
            return False

        #Validate user not to enter digit  
        for char in str_name:  
            for i in char:
                if (i.isnumeric() == True):
                    print("Must be Character")
                    return False
        return True
    

    def generate_letter(self, donations):
        print(self.name, "namne letter")
        print(self.donations, "donateioadsf")

        return """
            Dear {},
            Thank you  for your very kind donation of ${:.2f}
            It will be put to very good use.

                            Sincerely,
                            - The Team   
	        """.format(self.name, donations[-1])



