import json
from datetime import datetime, time

def load_attendance_data():
    try:
        with open('attendance3.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

def save_attendance_data(data):
    with open('attendance3.json', 'w') as file:
        json.dump(data, file)

def update_attendance(subject):
    data = load_attendance_data()
    current_time = datetime.now()
    date_str = current_time.strftime("%Y-%m-%d")
    time_str = current_time.strftime("%H:%M:%S")
    day_str = current_time.strftime("%A")
    
    if subject in data:
        data[subject]['count'] += 1
        data[subject]['attendance'].append({'date': date_str, 'time': time_str, 'day': day_str})
    else:
        data[subject] = {'count': 1, 'attendance': [{'date': date_str, 'time': time_str, 'day': day_str}]}
    
    save_attendance_data(data)

def is_within_time_limit():
    now = datetime.now().time()
    start_time = time(20, 24)  # Customizable start time
    end_time = time(21, 20)    # Customizable end time
    return start_time <= now <= end_time

def main():
    while True:
        if not is_within_time_limit():
            print("Attendance registration time is over.")
            break
        password = input("Enter password (or 'q' to quit): ")
        if password == 'q':
            break
        else:
            update_attendance(password)

if __name__ == "__main__":
      main() 
