project = {
    "Technology": "JFS",
    "Employee": [
        {"name": "Omkar", "Email": "omkar@email.com"},
        {"name": "Naresh", "Email": "naresh@email.com"},
        {"name": "Sachin", "Email": "sachin@email.com"}
    ]
}

print("Employee Emails -->")
for i in project['Employee']:
    print(i['Email'])
