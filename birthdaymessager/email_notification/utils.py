import json
import requests


# def get_patient_emails():
#   load = {'access_token' : access_token}
#   thistime = requests.get('https://drchrono.com/api/patients', params=load)
#   res = thistime.json()
#   storage = []
#   count = 0

#   for n in res['results']:
#     count += 1
#     if n['date_of_birth'] != None:
#       if n['date_of_birth'].find('-03-') == -1:
#         count -= 1
#       else:
#         storage.append(n)

#   emails = []
#   for patient in storage:
#     emails.append(patient['email'])

#   return emails



def bday_email():
  # emails = get_patient_emails()
  # for e in emails:
  a = EmailMessage('Happy Birthday from DrChrono!', 'We hope you have a great birthday!', to=[matrharr@gmail.com])
  a.send()
