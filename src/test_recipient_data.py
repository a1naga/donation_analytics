from recipient import RecipientData

class TestRecipientData:
    'This test class is to test the methods of RecipientData class'

    def setup_class(self):
        self.test_recipient_data = RecipientData(20)

    def test_add_donation(self):
        self.test_recipient_data.add_donation(500)
        assert self.test_recipient_data.get_total_donation() == 500
        assert self.test_recipient_data.get_num_cont() == 1

        self.test_recipient_data.add_donation(220)
        assert self.test_recipient_data.get_total_donation() == 720
        assert self.test_recipient_data.get_num_cont() == 2

        self.test_recipient_data.add_donation(340.50)
        assert self.test_recipient_data.get_total_donation() == 1061
        assert self.test_recipient_data.get_num_cont() == 3

        self.test_recipient_data.add_donation(150)
        assert self.test_recipient_data.get_total_donation() == 1211
        assert self.test_recipient_data.get_num_cont() == 4

    def test_percentile(self):

        test_recipient_data = RecipientData(10)
        test_recipient_data.add_donation(200)
        assert test_recipient_data.find_percentile() == 200
        test_recipient_data.add_donation(100)
        test_recipient_data.add_donation(300)
        assert test_recipient_data.find_percentile() == 100

        test_recipient_data = RecipientData(30)
        test_recipient_data.add_donation(410)
        test_recipient_data.add_donation(120)
        assert test_recipient_data.find_percentile() == 120
        test_recipient_data.add_donation(340)
        assert test_recipient_data.find_percentile() == 120
        test_recipient_data.add_donation(160)
        assert test_recipient_data.find_percentile() == 160
        test_recipient_data.add_donation(510)
        assert test_recipient_data.find_percentile() == 160
        test_recipient_data.add_donation(75)
        assert test_recipient_data.find_percentile() == 120

        test_recipient_data = RecipientData(75)
        test_recipient_data.add_donation(190)
        test_recipient_data.add_donation(140)
        assert test_recipient_data.find_percentile() == 190
        test_recipient_data.add_donation(65)
        test_recipient_data.add_donation(30)
        test_recipient_data.add_donation(148)
        assert test_recipient_data.find_percentile() == 148



