import os
import re

def extract_emails(input_file, output_file):
    print("Current Working Directory:", os.getcwd())  # Debugging
    try:
        with open(input_file, 'r') as file:
            content = file.read()

        email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        emails = re.findall(email_pattern, content)
        unique_emails = sorted(set(emails))

        with open(output_file, 'w') as file:
            for email in unique_emails:
                file.write(email + '\n')

        print(f"✅ Extracted {len(unique_emails)} email(s).")

    except FileNotFoundError:
        print(f"❌ The input file '{input_file}' was not found.")
    except Exception as e:
        print(f"❌ Error: {e}")

# Use the correct full path if needed
input_file = r"sample_text.txt"
output_file = r"extracted_emails.txt"
extract_emails(input_file, output_file)
