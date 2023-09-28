#This project simulates how file handling can be used to gather data from an IoT sensor and print it on
# a txt file for analysis

'''import time
from random import randint


    def get_sensor_data():
    temperature = randint(10,30)
    humidity = randint(40,60)
    return temperature,humidity

status = True
while status:
    temperature,humidity = get_sensor_data()
    sensor_data = f"The temp is {temperature}deg and humidity of {humidity}%"
    print(sensor_data)
    #Append the data on to a file
    with open(r"C:\\Users\\user\\Desktop\\Elewa Tech\\File_Handling\\sensor_data_file.txt","a") as data_file:
        data_file.write(sensor_data + "\n")
 
    time.sleep(1)
'''
import time
from random import randint

def getSensorData():
    temp = randint(20,50)
    humid = randint(80,100)
    return temp,humid

status = True
while status:
    temp,humid = getSensorData()
    sensor_data = f"Temperature is {temp} & Humidity is {humid}"
    
