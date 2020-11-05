def format_strdate_to_cmpdate(strdate):
    list_strdate = strdate.split('/')
    list_strdate.reverse()
    return "".join(list_strdate)