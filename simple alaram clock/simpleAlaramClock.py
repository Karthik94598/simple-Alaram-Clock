import datetime

# Get user input
setHr = int(input("Enter hour in 12hrs time mode: "))
setMin = int(input("Enter minute: "))
setAmPm = input("Enter AM or PM: ").upper().strip()
setDate = int(input("Enter Date: "))
setMon = int(input("Enter Month number: "))
setYear = int(input("Enter Year: "))

# Validate user input
if 1 <= setHr <= 12 and 0 <= setMin < 60 and setAmPm in ["AM", "PM"]:
    if setAmPm == "PM" and setHr != 12:
        setHr += 12
    elif setAmPm == "AM" and setHr == 12:
        setHr = 0
else:
    print("Invalid data, please enter correct data again.")
    exit()

# Continuously check the time
while True:
    currentTime = datetime.datetime.now()
    currentHr = int(currentTime.strftime("%H"))
    currentMin = int(currentTime.strftime("%M"))
    currentDate = int(currentTime.strftime("%d"))
    currentMon = int(currentTime.strftime("%m"))
    currentYear = int(currentTime.strftime("%Y"))

    if currentDate == setDate and currentMon == setMon and currentYear == setYear \
        and currentHr == setHr and currentMin == setMin:
        print("Reminder: Hello bro, It's time to start...!")
        break
