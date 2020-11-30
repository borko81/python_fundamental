import re

places = input()

pattern_for_location = re.compile(r'([=|\/])(?P<location>[A-Z][A-Za-z]{2,})(\1)')

result = []

for p in pattern_for_location.finditer(places):
    result.append(p.group('location'))

destinations = ", ".join(result)
travel_points = len([i for l in [list(i) for i in result] for i in l])
print(f"Destinations: {destinations}")
print(f"Travel Points: {travel_points}")

"""
You will be given a string representing some places on the map. You have to filter only the valid ones. A valid location is:
    • Surrounded by "=" or "/" on both sides (the first and the last symbols must match)
    • After the first "=" or "/" there should be only letters (the first must be upper-case)
    • The letters must be at least 3
Example: In the string "=Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=" only the first two locations are valid.
After you have matched all the valid locations, you have to calculate travel points. They are calculated by summing the lengths of all the valid destinations that you have found on the map. At the end, on the first line print the following: "Destinations: {destinations joined by ', '}". On the second line print "Travel Points: {travel_points}".
"""

# INPUT
# =Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=
