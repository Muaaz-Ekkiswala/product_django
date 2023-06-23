import datetime


def get_financial_year_details():
    date = datetime.datetime.now().date()
    financial_year_start_date = datetime.date(date.year, 4, 1)
    if date < financial_year_start_date:
        financial_year = "{}-{}".format(str(date.year - 1)[2:], str(date.year)[2:])
    else:
        financial_year = "{}-{}".format(str(date.year)[2:], str(date.year + 1)[2:])

    quarter = ['Q4', 'Q1', 'Q2', 'Q3'][((date.month - 1) // 3) % 4]

    return {
        'year': financial_year,
        'quarter': quarter
    }


print(get_financial_year_details())
