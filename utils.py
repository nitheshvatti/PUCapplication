import uuid
from datetime import datetime
from dateutil.relativedelta import relativedelta


def generate_uuid():
    standard_uuid = uuid.uuid4()
    uuid_string = str(standard_uuid).replace('-', '')
    short_uuid = uuid_string[:10]
    return short_uuid


def calculate_expiry_date(certificate_type):
    if certificate_type == "12 months":
        no_of_months = 12
    else:
        no_of_months = 6
    current_date = datetime.now().date()
    expiry_date = current_date + relativedelta(months=no_of_months) - relativedelta(days=1)
    return expiry_date
