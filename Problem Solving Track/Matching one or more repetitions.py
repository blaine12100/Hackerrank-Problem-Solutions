Regex_Pattern = r"^\d{1,}[A-Z]+[a-z]+$"  # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
