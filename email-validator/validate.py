import smtplib
import dns.resolver
from email_validator import validate_email, EmailNotValidError

def generate_emails(name, domain):
    """Generate possible email combinations."""
    name_parts = name.lower().split()
    email_combinations = [
        f"{name_parts[0]}@{domain}",
        f"{name_parts[0]}.{name_parts[1]}@{domain}",
        f"{name_parts[0]}{name_parts[1][0]}@{domain}",
        f"{name_parts[0][0]}{name_parts[1]}@{domain}",
        f"{name_parts[0][0]}.{name_parts[1]}@{domain}",
        f"{name_parts[0]}_{name_parts[1]}@{domain}",
        f"{name_parts[0]}-{name_parts[1]}@{domain}",
        f"{name_parts[0]}{name_parts[1]}@{domain}"
    ]
    return email_combinations

def verify_email(email):
    """Verify if the email exists using SMTP."""
    print(f"Verifying {email}...")
    try:
        # Validate email format
        valid = validate_email(email)
        email = valid.email
        
        # Get domain for MX record lookup
        domain = email.split('@')[1]
        
        # Get MX record
        records = dns.resolver.resolve(domain, 'MX')
        mx_record = str(records[0].exchange)
        
        # SMTP lib setup
        server = smtplib.SMTP(timeout=10)  # Set a timeout for the SMTP connection
        server.set_debuglevel(0)

        # SMTP Conversation
        server.connect(mx_record)
        server.helo(server.local_hostname)
        server.mail('me@mydomain.com')
        code, message = server.rcpt(email)
        server.quit()

        # Check if the email is valid
        if code == 250:
            print(f"{email} is valid")
            return True
        else:
            print(f"{email} is invalid")
            return False
    except (smtplib.SMTPServerDisconnected, smtplib.SMTPConnectError, smtplib.SMTPHeloError,
            smtplib.SMTPSenderRefused, smtplib.SMTPDataError, smtplib.SMTPRecipientsRefused,
            dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, EmailNotValidError, TimeoutError) as e:
        print(f"Error verifying {email}: {e}")
        return False

def main():
    name = input("Enter the person's name: ")
    domain = input("Enter the company domain: ")

    email_combinations = generate_emails(name, domain)
    valid_emails = []

    for email in email_combinations:
        if verify_email(email):
            valid_emails.append(email)

    if valid_emails:
        print("Valid email addresses found:")
        for email in valid_emails:
            print(email)
    else:
        print("No valid email addresses found.")

if __name__ == "__main__":
    main()
