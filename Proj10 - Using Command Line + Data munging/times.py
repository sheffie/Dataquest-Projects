from read import load_data
import dateutil
data = load_data()

def get_hour(date):    
    time = dateutil.parser.parse(date, parserinfo=None)
    return time.hour

data["submission_hours"] = data["submission_time"].apply(get_hour)

hours = data["submission_hours"].value_counts()

print(hours)


