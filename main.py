email = input("Enter your Email : ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_name = (f"Your user name is '{username}'\ and your domain is '{domain_name}'")
print(format_name)