#Simulating an IoT sensor
import time 
from random import randint
file = "test_data.txt"
def get_sensor_data():
    humidity = randint(20,60)
    temp = randint(60,100)
    return humidity,temp

status = True
while status:
    temp,humidity = get_sensor_data()
    sensor_data = f"Temperature data is {temp} and humidity of {humidity}"
    print(sensor_data)
    with open(file,"w") as mydata:
        mydata.write(sensor_data + "\n")
        mydata.flush()
    
    time.sleep(10)




#Reading the file
File_instance = open(file,"r")
for i in File_instance:
    print(i)
    