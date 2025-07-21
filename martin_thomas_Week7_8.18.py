import re

passwordarray = [
    "My-Secure-Password-for-123",
    "ShortPW!1",
    "Low-er-case-12-3",
    "UPPERCASEs1!@#",
    "A_m0re_C0mpl3x_Pa55_W0rd"
]

pattern1 = r'^(?=(?:[a-zA-Z0-9]*[-_., ]){4,}[a-zA-Z0-9]*$).{8,}'

pattern2 = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%<^>&*?]).{8,}'

for password in passwordarray:
    if re.match(pattern1, password):
        print(f"The Password '{password}' meets the first requirement.")
    else:
        print(f"The Password '{password}' does not meet the first requirement.")

    if re.match(pattern2, password):
        print(f"The Password '{password}' meets the second requirement.")
    else:
        print(f"The Password '{password}' does not meet the second requirement.")