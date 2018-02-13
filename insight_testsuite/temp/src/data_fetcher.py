import sys
from donations_analytics import DonationAnalytics
from recipient_record import RecipientRecord


class FetchData:

    def __init__(self,itcont,percentile,outfile):
        self.itcont = itcont
        with open(percentile) as p_file:
            for line in p_file:
                self.percentile = float(line)
        self.donation_analytics = DonationAnalytics(self.percentile,outfile)

    def process_lines(self):
        with open(self.itcont, 'r') as data_file:
            for line in data_file:
                data = line.split("|")
                if len(data[15]) > 0:
                    continue
                cmte_id = data[0]
                donor_name = data[7]
                zip_code = data[10]
                trans_date = data[13]
                trans_amt = data[14]
                record = RecipientRecord(cmte_id, donor_name, zip_code, trans_date, trans_amt)
                self.donation_analytics.process_data(record)
        self.donation_analytics.close_outfile()


def main():
    print(sys.argv)
    print(len(sys.argv))
    if len(sys.argv) >= 4:
        read = FetchData(sys.argv[1],sys.argv[2],sys.argv[3])
        read.process_lines()
    else:
        print("Please give the required arguments to run the program")


if __name__ == "__main__":
    main()