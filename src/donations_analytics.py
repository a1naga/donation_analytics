from recipient import RecipientData
from validate_record import ValidateRecord
import csv


class DonationAnalytics:
    '''This class processes each donation record, identifies repeat donors,
    calculates total contribution, percentile value for a [recipient, zip, year] combination.
    The running count, total, percentile values are written to output file'''

    def __init__(self,percentile,outfile):
        self.donor_dict = {}
        self.recipient_dict = {}
        self.outfile = open(outfile, "w")
        self.datawriter = csv.writer(self.outfile, delimiter="|")
        self.percentile = percentile
        self.validator = ValidateRecord()

    def process_data(self,record):

        if not self.validator.validate(record):
            return
        # Extract the year from transaction date
        year = record.trans_date[4:8]
        # Extract the first 5 digits of zip code
        zip_code = record.zip_code[:5]
        # Donor name and zipcode make the unique donor
        unique_donor = (record.donor_name,zip_code)
        if unique_donor in self.donor_dict:
            if self.donor_dict[unique_donor] <= year:
                recipient_key = (record.cmte_id, zip_code, year)
                if recipient_key in self.recipient_dict:
                    self.recipient_dict[recipient_key].add_donation(float(record.trans_amt))
                else:
                    recipient_value = RecipientData(self.percentile)
                    self.recipient_dict[recipient_key] = recipient_value
                    recipient_value.add_donation(float(record.trans_amt))
                recipient_value = self.recipient_dict[recipient_key]
                data_row = [record.cmte_id, zip_code, year,
                            recipient_value.find_percentile(),
                            recipient_value.get_total_donation(),
                            recipient_value.get_num_cont()]
                self.datawriter.writerow(data_row)
            else:
                self.donor_dict[unique_donor] = year
        else:
            self.donor_dict[unique_donor] = year

    def close_outfile(self):
        self.outfile.close()
