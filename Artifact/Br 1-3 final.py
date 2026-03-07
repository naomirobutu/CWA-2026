import serial
import csv

ser= serial.Serial("COM4", 115200)



filename= "Br1-3-Naomi-Data.csv"



for x in range(1,100):
    #print(line)
    line=ser.readline(). decode("utf-8", errors= "ignore").strip ()
    
    print(line)
    parts= line.split(",")
    
        
    if len(parts) >= 4:
    
        moisture= parts[0]
        temp= parts[1]
        light= parts[2]
        sound= parts [3]
    
        print("my moisture is:", moisture,"my temperature is:",temp)
        print("my light is:", light, "my sound is :", sound)
    

    
        with open(filename, "a", newline= "") as f:
            writer = csv.writer(f)
            writer.writerow ([moisture,temp,light,sound])
    
    
    
    
