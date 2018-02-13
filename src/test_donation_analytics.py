from donations_analytics import DonationAnalytics
from recipient_record import RecipientRecord


class TestDonationAnalytics:
    'This class is to test the process data method of DonationAnalytics class'

    def setup_class(self):

        self.donation_anaytics = DonationAnalytics(30,"/tmp/repeat_donors.txt")

    def test_process_data(self):

        record1 = RecipientRecord("C00384516","SABOURIN, JAMES","02895","01262016","230")
        record2 = RecipientRecord("C00384517", "SABOURIN, JOE", "02892", "01152017", "330")
        record3 = RecipientRecord("C00384516", "SABOURIN, JAMES", "02895", "01202017", "430")
        record4 = RecipientRecord("C00384517", "SABOURIN, JAMES", "02895", "01312017", "130")

        self.donation_anaytics.process_data(record1)
        self.donation_anaytics.process_data(record2)
        self.donation_anaytics.process_data(record3)
        self.donation_anaytics.process_data(record4)
        self.donation_anaytics.close_outfile()

        with open("/tmp/repeat_donors.txt") as fp:

            line1 = fp.readline()
            print("line1 :", line1)
            data = line1.split("|")
            assert data[0] == "C00384516"
            assert data[1] == "02895"
            assert data[2] == "2017"
            assert data[3] == "430"
            assert data[4] == "430"
            assert data[5] == "1\n"

            line2 = fp.readline()
            data = line2.split("|")
            assert data[0] == "C00384517"
            assert data[1] == "02895"
            assert data[2] == "2017"
            assert data[3] == "130"
            assert data[4] == "130"
            assert data[5] == "1\n"



