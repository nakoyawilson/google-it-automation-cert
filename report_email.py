#!/usr/bin/env python3
import os
from datetime import date
import reports
import emails

def process_data(data):
    directory_path = data
    fruits_info = os.listdir(directory_path)
    additional_info = []
    for text_file in fruits_info:
        if text_file.endswith(".txt"):
            with open(os.path.join(directory_path, text_file)) as d:
                lines = d.read().strip().splitlines()
                name, weight, description = lines
                entry = ["name: " + name, "weight: " + weight]
                additional_info.append(entry)
    additional_info.sort()
    pdf_body = []
    for item in additional_info:
        pdf_body.append(item[0])
        pdf_body.append(item[1])
        pdf_body.append("")
    pdf_body = '<br/>'.join(pdf_body)
    return pdf_body

def main(argv):
  data = "/Users/nakoya/Documents/Python/google-it-automation-cert/supplier-data/descriptions/"
  today = date.today()
  formatted_date = today.strftime("%B %d, %Y")
  pdf_title = "Process Update on {}".format((formatted_date))
  filename = "/tmp/processed.pdf"
  pdf_body = process_data(data)
  reports.generate_report(filename,pdf_title,pdf_body)
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  email_body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  message = emails.generate_email(sender, receiver, subject, email_body, "/tmp/processed.pdf")
  emails.send_email(message)

if __name__ == "__main__":
  main(sys.argv)