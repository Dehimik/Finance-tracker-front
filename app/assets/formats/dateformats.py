from datetime import datetime

def format_date_dbY(date):
    #Format to '00 month 0000' type
    date = date.split("+")[0]
    date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d %b %Y")

def format_date_timeWithHMp(date):
    # Format to '00 month 00:00' type
    date = date.split("+")[0]
    date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
    return date_obj.strftime("%d %b %H:%M %p")