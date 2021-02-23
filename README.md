# Password Checker
Check your passwords to see if it has been compromised or involved in any data breaches

## How to use
To run this script, python3 must be installed on the computer.

Download the script to your local pc, navigate to the folder where it was saved, and run the command below replacing the PASSWORD variables with however many passwords you would like to check seperated by spaces.
```
python3 checkmypass.py PASSWORD1 PASSWORD2
```
Script will return the password and how many times it has been involved in a data breach.

## Implementation
This script utilizes SHA1 encoding and validates the encrypted password with the pwnedpasswords api to verify the amount of times your password has been pwned.
