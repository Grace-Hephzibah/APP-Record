from typing import Dict
import re
 # Create an alias called 'ContactDict'
ContactDict = Dict[str, str]
def check_if_valid(contacts: ContactDict) -> bool:
    for name, email in contacts.items():
        # Check if name and email are strings
        if (not isinstance(name, str)) or (not isinstance(email, str)):
            return False
        # Check for email xxx@yyy.zzz
        if not re.match(r"[a-zA-Z0-9\._\+-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$", email):
            return False
    return True
print(check_if_valid({'viji': 'viji@sample.com'}))
print(check_if_valid({'viji': 'viji@sample.com', 123: 'wrong@name.com'}))
