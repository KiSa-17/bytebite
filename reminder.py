import schedule
import time
from database import getmed, log

def send_reminder(pid,medication):
    print("Reminder: Take {medication['name']} ({medication['dosage']}) now!")
    confirmation = input("Did you take {medication['name']}? (yes/no): ").strip()
    if confirmation == 'yes':
        log(pid,medication['id'], "taken")
    else:
        log(pid,medication['id'], "missed")
        print("ALERT! {medication['name']} missed. Notifying caregiver...")

def schedule_reminders(pid):
    meds = getmed()
    for med in meds:
        schedule.every(int(med['frequency'])).hours.do(send_reminder, medication=med,pid=pid)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    pid=input("enter patient id")
    schedule_reminders(pid)
