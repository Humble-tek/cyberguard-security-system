print("========================================")
print("           CYBERGUARD v1.0")
print("     PERSONAL SECURITY MONITORING SYSTEM")
print("========================================")
print()
print("Welcome, SOC Analyst!")
print()
print("Your mission is to monitor account")
print("information and identify potential threats.")
print()
print("Starting security assessment...")
print()
print()

#COLLECT USER INFO

username = input("Enter username: ")
email = input("Enter email address: ")
password = str(input("Enter password: "))
age = int(input("Enter age: "))
ip_address = str(input("Enter IP address: "))
failed_attempts = int(input("Enter number of failed login attempts: "))
account_status = bool(input("Is the account Active or Inactive? "))

#PASSWORD STRENTGH
password_length = len(password)
if password_length < 8:
    password_strength = "WEAK"
elif 8 == password_length <= 11:
    password_strength = "MODERATE"
else:
    password_strength = "STRONG"

#THREAT DETECTION
# Float calculation: percentage of the 5-attempt brute-force limit
attempt_percentage = failed_attempts / 5 * 100
attempt_percentage = float(attempt_percentage)

# Login attempt analysis
if failed_attempts == 0:
    login_message = "No failed login attempts detected."
    threat_level = "LOW"
elif failed_attempts <= 4:
    login_message = "Low security alert: some failed login attempts."
    threat_level = "MEDIUM"
else:
    login_message = "Critical warning: Possible brute-force attack!"
    threat_level = "HIGH"

# Account status analysis
if account_status == False:
    status_message = "Account access is currently disabled."
elif failed_attempts < 5:
    status_message = "No critical login threat detected."
else:
    status_message = "Account is active and under suspicious activity."

# Account status text for the report
if account_status:
    status_text = "ACTIVE"
else:
    status_text = "INACTIVE"

# Recommendation depends on the threat level and account status
if threat_level == "HIGH":
    recommendation = "Investigate the login activity and secure the account immediately."
elif threat_level == "MEDIUM":
    recommendation = "Monitor the account and consider resetting the password."
else:
    recommendation = "No action required. Continue routine monitoring."

if account_status == False:
    recommendation = recommendation + "The account is disabled. Verify why before re-enabling it."

if password_strength == "WEAK":
    recommendation = recommendation + "Use a longer password (at least 12 characters)."


#REPORT
print()
print("========================================")
print("          CYBERGUARD SECURITY REPORT")
print("========================================")
print()
print("USER INFORMATION")
print("----------------------------------------")
print(f"Username:  {username}")
print(f"Email:  {email}")
print(f"Age:  {age}")
print(f"IP Address:  {ip_address}")
print(f"Account Status: {status_text}")
print()
print("SECURITY ANALYSIS")
print("----------------------------------------")
print(f"Password Assessment:  {password_strength}")
print(f"Failed Login Attempts:  {failed_attempts}")
print(f"Brute-force limit used:  {attempt_percentage}")
print()
print("THREAT DETECTION")
print("----------------------------------------")
print(f"[LOGIN]  {login_message}")
print(f"[ACCOUNT]  {status_message}")
print()
print("FINAL SECURITY STATUS")
print("----------------------------------------")
print(f"THREAT LEVEL:  {threat_level}")
print()
print("RECOMMENDATION:")





