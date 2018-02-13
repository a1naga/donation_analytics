from datetime import datetime


class ValidateRecord:
    'This is a utility class to validate the record fields'

    def validate(self, record):

        if len(record.cmte_id) == 0 or len(record.donor_name) == 0 or len(record.trans_amt) == 0 or len(
                record.trans_date) == 0 or len(
                record.zip_code) < 5:
            return False
        if len(record.cmte_id) > 9:
            return False
        fullname = record.donor_name.split(',')
        for name in fullname:
            name = name.strip()
            if not name.isalpha():
                return False
        try:
            datetime.strptime(record.trans_date, "%m%d%Y")
            float(record.trans_amt)
        except ValueError:
            return False
        return True


