"""
So this code runs on "generated emails" from chatgpt, but there will be another variation of the same code but the data will be authentic because  we want to make sure 
that i or you can also use this script in a real world setting, this is useful but the real problem here is that we have to actually set an example of what might be a potential 
fake email, so we could in the next variation include a meter like option which shows the likelyhood of an email being "fake" or labelling it as a phishing email..
"""





import re

emails = [
    "j4n3_doe-1991@xmpl.co",
    "super.user+99@mail-service123.com",
    "info@a-very-long-domain-name-example.biz",
    "t3ch_guru#45@dev-portal.net",
    "m!chael.o'connor@weird-email.org",
    "alice_bob2024@corporate-email.co.uk",
    "cust0mer123-service@shop4all.us",
    "random_guy99@strang3r-mail.info",
    "feedback@xyz123-company.io",
    "vip-member!2021@exclusive.co",
    "c0ntact_us@sup3rsite.onl",
    "lucky#7.win@lottery-email.xyz",
    "daily-updates+news@newsletter.co",
    "first-last_789@example-data.net",
    "us3r-01@new-platform.app",
    "team.lead99@global-company.com",
    "hello.world-2022@smpldomain.tech",
    "secure+account!login@safe-mail.gov",
    "qwerty.09876@keyboard-fanatic.edu",
    "trial-user_x001@beta-test-platform.dev",
    "email.with.many.parts@a.b.c.d.com",
    "complex.address_12345@my-email.place",
    "special+characters-in@domain-x.co.uk",
    "webmaster!site@home.site-builder.io",
    "f@ncy-email+extra.tag@mydomain.special",
    "john.doe@gmail.com",
    "sarah.connor2024@yahoo.com",
    "fake-email@notarealdomain.fake",
    "test_user_123@randomdomain.biz",
    "unusual_email!99@fakemail.xyz",
    "invalid-email@fake.fake",
    "admin_account#42@website.com",
    "newsletter-subscribe_2021@updates.co",
    "no-reply@realtalk.fake",
    "legit.email_2023@yahoo.com",
    "backup.contact_2025@gmail.com",
    "email.test999@testing.com",
    "trash-email_123@throwaway.fake",
    "spammer@spamdomain.notreal",
    "catch_me_if_you_can@fakeplace.io",
    "mister.fake.email@notreal.biz",
    "scam_email999@shady.business",
    "real.person.name@gmail.com",
    "official-contact@bigcorp.com",
    "user.name+alias_001@yahoo.com"
    "mikenaim.75@gmail.com"
]

# Function to validate emails and filter fake ones in an organized way
def validate_and_filter_emails():
    valid_pattern = r"^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$"
    fake_domains = ["fake.com", "yahoo.com", "fakemail.xyz", "notarealdomain.fake", "throwaway.fake", "spamdomain.notreal", "fakeplace.io", "notreal.biz", "shady.business"]
    
    valid_emails = []
    fake_emails = []

    # Process the emails
    for email in emails:
        if re.match(valid_pattern, email):  # Validate basic email format
            domain = email.split('@')[-1]
            if domain in fake_domains:  # Check if the domain is considered fake
                fake_emails.append(email)
            else:
                valid_emails.append(email)
    
    # Organize the output
    print("\nValid Emails:")
    for email in valid_emails:
        print(f"- {email}")
    
    print("\nFake Emails:")
    for email in fake_emails:
        print(f"- {email}")

# Function to check emails with numbers in the username part
def emails_with_numbers():
    pattern = r"^[\w\.-]*\d+[\w\.-]*@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$"
    return [email for email in emails if re.match(pattern, email)]

# Function to check for domain-specific emails (e.g., Gmail, Yahoo)
def domain_specific():
    pattern = r"^[\w\.-]+@(gmail\.com|yahoo\.com)$"
    return [email for email in emails if re.match(pattern, email)]

# Function to check for fake emails (example: emails with fake.com or yahoo.com)
def fake_emails_checker():
    pattern = r"^[\w\.-]+@(fake\.com|yahoo\.com)$"
    return [email for email in emails if re.match(pattern, email)]

def show_options():
    print("\nAvailable Functions:")
    print("1. Check emails with numbers in the username")
    print("2. Check basic email validation and filter fake emails")
    print("3. Check domain-specific emails (e.g., Gmail, Yahoo)")
    print("4. Check for fake emails (fake.com, yahoo.com)")
    print("5. Exit")

does_user_want_to_check_the_mail_list = input('Type "check" or "yes" if you want to see the entire email list: \n')
check = "check"
yes = ["yes", "Yes", "YeS", "yES", "YES"]

if does_user_want_to_check_the_mail_list == check or yes:
    print(emails)
    # Now ask if the user wants to see the function options
    show_more_options = input("Would you like to see the available functions? (yes/no): \n")
    
    if show_more_options.lower() in yes:
        show_options()
        choice = input("Select an option: ")
        if choice == "1":
            print(emails_with_numbers())
        elif choice == "2":
            validate_and_filter_emails()
        elif choice == "3":
            print(domain_specific())
        elif choice == "4":
            print(fake_emails_checker())
        elif choice == "5":
            print("Exiting... Goodbye!")
        else:
            print("Invalid choice, please try again.")
    else:
        print("Returning to the main menu.")
else:
    print("Incorrect input. Please type 'yes' or 'check'.")
