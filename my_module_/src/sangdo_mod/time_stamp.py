import datetime as dt

# Return a time stamp string like 20240518_210437 (date_time of now)
def get_time_stamp():
    now = dt.datetime.now()
    filename_time_stamp = (
        f"{now.year}{now.month:0>2}{now.day:0>2}_"            
        f"{now.hour:0>2}{now.minute:0>2}{now.second:0>2}")
    return filename_time_stamp


if __name__ == "__main__":
    fs = get_time_stamp()
    print(fs)
