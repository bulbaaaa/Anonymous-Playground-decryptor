import string

str1 = "hEzAdCfHzA"
str2 = "hEzAdCfHzAhAiJzAeIaDjBcBhHgAzAfHfN"
str = str1 + str2
ssh = ""

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase

for i in range(0,len(str),2):
    letter1 = str[i]
    letter2 = str[i+1]
    index1 = lowercase.index(letter1) + 1
    index2 = uppercase.index(letter2) + 1
    sum_letter = index1 + index2
    result_letter = lowercase[(sum_letter - 1) % 26]
    ssh += result_letter

print(f"Creds SSH Login: {ssh[0:5]} Password: {ssh[5:]}")