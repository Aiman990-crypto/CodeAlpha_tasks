import os
import re

def extract_emails(input_file, output_file):
    print("Current Working Directory:", os.getcwd())  # Debugging
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        email_pattern = r'(?i)\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}\b'
        emails = re.findall(email_pattern, content)
        unique_emails = sorted(set(emails))

        with open(output_file, 'w', encoding='utf-8') as file:
            for email in unique_emails:
                file.write(email + '\n')

        print(f"✅ Extracted {len(unique_emails)} email(s).")
        for email in unique_emails:
            print(email)

    except FileNotFoundError:
        print(f"❌ The input file '{input_file}' was not found.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    input_file = r"sample_text.txt"
    output_file = r"extracted_emails.txt"
    extract_emails(input_file, output_file)
