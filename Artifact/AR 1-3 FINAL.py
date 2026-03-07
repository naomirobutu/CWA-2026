import serial
import time

# connect to Arduino
ser = serial.Serial("COM4", 115200)
time.sleep(2)


def check_wildfire_risk(temp, moisture, light):

    risk = temp * 2 - (moisture / 10) + (light / 50)

    if risk > 40:
        status = "HIGH FIRE RISK"
    elif risk > 30:
        status = "MEDIUM FIRE RISK"
    else:
        status = "LOW FIRE RISK"

    return risk, status


while True:

    try:
        line = ser.readline().decode(errors='ignore').strip()

        if line == "":
            continue

        data = line.split(",")

        if len(data) < 4:
            continue

        moisture = int(data[0])
        temp = int(data[1])
        light = int(data[2])
        sound = int(data[3])

        risk, status = check_wildfire_risk(temp, moisture, light)

        print("Temp:", temp,
              "Moisture:", moisture,
              "Light:", light,
              "Risk:", risk,
              "Status:", status)

        # adaptive warning system 
        if risk > 40:
            print("⚠️ Wildfire danger is HIGH!")
            print("siren activated!")
        elif risk > 30:
            print("⚠️ wrarning: Medium wildfire risk. monitor conditions.")
        else:
            print ("✅enviormental conditions are safe.")
            

        # simulation 1: temperature increase
        temp_sim = temp + 5
        risk_temp, status_temp = check_wildfire_risk(temp_sim, moisture, light)

        # simulation 2: moisture decrease
        moisture_sim = moisture - 40
        risk_moist, status_moist = check_wildfire_risk(temp, moisture_sim, light)

        print("Original:", temp, moisture, risk, status)
        print("Temp +5:", temp_sim, moisture, risk_temp, status_temp)
        print("Moisture -40:", temp, moisture_sim, risk_moist, status_moist)
        print("-----------------------------------")

        time.sleep(1)

    except:
        print("Invalid data received")