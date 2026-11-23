from datetime import datetime

first_name = input("Enter student first name: ").strip()
last_name = input("Enter student last name: ").strip()
section = input("Enter section: ").strip()
event_name = input("Enter event name: ").strip()
event_year = int(input("Enter event year: ").strip())
event_month = int(input("Enter event month: ").strip())
event_day = int(input("Enter event day: ").strip())

full_name = f"{first_name} {last_name}".title()
name_code = full_name.upper()
formatted_section = section.upper()
formatted_event = event_name.title()

event_date_obj = datetime(event_year, event_month, event_day)
formatted_date = event_date_obj.strftime("%B %d, %Y").replace(" 0", " ")

print("\nStudent Event Registration Summary")
print(f"Name: {full_name}")
print(f"Name Code: {name_code}")
print(f"Section: {formatted_section}")
print(f"Event: {formatted_event}")
print(f"Event Date: {formatted_date}")
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Date/Time Feature Used: datetime")
print("Registration record created successfully.")
