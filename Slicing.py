# Exercise 2: Slicing Strings

employee_id = "emp92345"

# Extract the first three characters
first_three = employee_id[:3]
print("First three characters:", first_three)

# Extract the last three characters
last_three = employee_id[-3:]
print("Last three characters:", last_three)

# Extract the substring from index 3 to 5 (inclusive)
substring_3_to_5 = employee_id[3:6]
print("Substring from index 3 to 5:", substring_3_to_5)

# Given the URL
url = "https://www.example.com/page"

# Extract "https"
protocol = url[:5]
print("Protocol:", protocol)

# Extract "www.example.com"
domain = url[8:24]
print("Domain:", domain)

# Extract "page"
page = url[25:]
print("Page:", page)
