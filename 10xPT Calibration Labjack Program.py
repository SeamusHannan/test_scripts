from labjack import ljm 
import csv
import os

def get_data(handle):
    pt=ljm.eReadName(handle, "AIN0")
    return [pt]


def log_data(part_number,serial_number,position,mV,datasheet):
    filewriter = csv.writer(datasheet)
    row = [part_number,serial_number,position,mV]
    filewriter.writerow(row)

def create_csv(new_file_name):
    with open(f"{new_file_name}.csv", 'a+', newline='') as datasheet:
        filewriter = csv.writer(datasheet)
        heading = "Part Number","Serial Number","Position","mV Reading"
        filewriter.writerow(heading)
        return [datasheet]
       
def main():
    part_number = input("Part Number: ")
    serial_number = input("Serial Number: ")
    position = input("Position on Calibration Station: ")
    new_file_name = f"{part_number}_{serial_number}"
    handle = ljm.openS("T7", "ANY", "ANY")
    mV = get_data(handle)
    create_csv(new_file_name)
    log_data(part_number,serial_number,position,mV,new_file_name)

if __name__ == "__main__":
    main()