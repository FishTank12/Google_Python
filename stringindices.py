#This is the first part of the excercise

'''
this excercise is seperated into two parts and they ask in the following:
1.
  given the string device_id ="a1b2c3d4e5"
  we need to extract the first character,
  extract the last character using a negative index
  Extract the substring "b2c"

  2. We need to create a string variable named ip_address that contains the value 
  "192.168.0.1" we must indice to extract the following:

  the first octet("192")
  the last octet("1")

'''
typeme = "a1b2c3d4e5" #we created a variable that holds the string so we dont repeat it for every other variable will assign it to.
device_id = typeme[1] #Completed first task: "Extract the first character"
print("answer:\n"+ device_id)
device_Negative_id = typeme[-9] #Completed the second task: "Extract the last character using a negative index"
print("answer:\n" + device_Negative_id)
device_sub_id = typeme[2:5] #Completed the third task: "Extract substring b2c"
print( "answer\n:"+device_sub_id)

print("Here is the other Excercise:")

typetheIP = "192.168.0.1" #we are doing the same technique in the last task
first_Octet = typetheIP[0:3]
print(first_Octet)
last_Octet = typetheIP[-11]
print(last_Octet)
