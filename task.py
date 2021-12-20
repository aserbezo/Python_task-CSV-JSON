import os.path
import json
import csv
from datetime import datetime


# function to check if datetime is format ISO 8601 , converted and pass it to function convert_time_local.
def check_time_format(format_check):
    try:
        time = datetime.strptime(format_check, "%Y-%m-%dT%H:%M:%S%z")
    except:
        time = format_check
    return time


# function to convert datetime and change only current time and timezone.
def convert_time_local(date_input):
    time = check_time_format(date_input)
    old_date = str(time)
    old_date = old_date.split()
    curr_time = datetime.now()
    curr_time = str(curr_time.astimezone())
    new_time = curr_time.split()
    timezone = new_time[1]
    timezone = timezone[-6:]
    curr_time = new_time[1].split(".")
    curr_time = curr_time[0]
    result = old_date[0] + " " + curr_time + timezone
    return result


# function to convert celsius to fahrenheit and vice verse.
def convert_temperatures(temp_check):
    temperatures = temp_check
    if "c" in temperatures:
        numbers = ""
        for i in temperatures:
            if i.isdigit():
                numbers += i
        numbers = int(numbers)
        # celsius to fahrenheit formula
        cover = ((9 / 5) * numbers + 32)
        result = f"{int(cover)}F"
        return result
    else:
        number = ""
        for i in temperatures:
            if i.isdigit():
                number += i
        number = int(number)
        # fahrenheit to celsius formula
        cover_f = (number - 32) * 5 / 9
        result = f"{round(cover_f)}C"
        return result


# function to check if the input file name has a file extension .csv or .json .
def check_input_file(inputfilename):
    if ".json" in inputfilename:
        file = True

    elif ".csv" in inputfilename:
        file = True

    else:
        file = False
        # print("Please choose .csv or .json file extension for input file!")
    return file


# function to check if the file name exist.
def file_existence(file_name):
    if os.path.isfile(file_name):
        file = True
    else:
        file = False
        # print(f"Sorry , there is no file associated with name {filename}")
    return file


# function to check if the output file name has a file extension .csv or .json .
def check_output_name(outputfilename):
    if ".json" in outputfilename:
        file = True
    elif ".csv" in outputfilename:
        file = True
    else:
        file = False
    # print("Please choose .csv or .json file extension for output file!")
    return file


print("At beginning you can select between sample.csv and sample.json file")
inputFilename = input("Please enter the name of input file: ")
outputFilename = input("Please enter the name of output file: ")

# we use two help variables to save valid results
input_file = ""
output_file = ""

# after input the file name and output file name we call first the function "check_input_file" and "check_output_file" ,
# to verify in the file extension .csv or .json are valid.
if check_input_file(inputFilename):
    # if is valid we check the existence of the file with function "file_existence".
    if file_existence(inputFilename):
        input_file = inputFilename
    else:
        print(f"Sorry , there is no file associated with name {inputFilename}")
else:
    print("Please choose .csv or .json file extension for input file!")
if check_output_name(outputFilename):
    output_file = outputFilename
else:
    print("Please choose .csv or .json file extension for output file!")

# if the input and output file name is valid we're starting to convert  from csv or json and vice verse.
# first we check if the input file is with csv or json extension then we check the output file extension
if ".json" in input_file:
    filename = input_file
    # if the output file is with json extension
    if ".json" in output_file:
        with open(filename) as f:
            data = json.load(f)
            my_dict = []
            data_dict = {}
            for key in data:
                if key["city"] not in my_dict:
                    data_dict = {"city": key['city'], "date": "", "temp": ""}
                    date = key["date"]
                    # calling function convert_time_local convert datetime
                    date_convert = convert_time_local(date)
                    data_dict["date"] = date_convert
                    temp = str(key['temp'])
                    temp = temp.lower()
                    # calling function convert_temperatures
                    temp_convert = convert_temperatures(temp)
                    data_dict['temp'] = temp_convert
                    my_dict.append(data_dict)
            f = open(output_file, "a")
            json.dump(my_dict, f, indent=4)
            f.close()
    # if the output file is with csv extension
    elif ".csv" in output_file:
        with open(filename) as f:
            data = json.load(f)
            for key in data:
                my_lists = []
                my_lists.append(key["city"])
                convert_time = convert_time_local(key["date"])
                my_lists.append(convert_time)
                convert_temp = str(key["temp"]).lower()
                convert_temp = convert_temperatures(convert_temp)
                my_lists.append(convert_temp)
                f = open(output_file, "a")
                writer = csv.writer(f)
                writer.writerow(my_lists)
                f.close()
elif ".csv" in input_file:
    filename = input_file
    # if the output file is with json extension
    if ".json" in output_file:
        with open(filename) as f:
            reader = csv.reader(f)
            my_list = []
            data_dict = {}
            for row in reader:
                data_dict = {"city": row[0], "date": "", "temp": ""}
                current_time = row[1].strip()
                current_time = convert_time_local(current_time)
                data_dict["date"] = current_time
                temp = row[2].lower()
                temp = convert_temperatures(temp)
                data_dict["temp"] = temp
                my_list.append(data_dict)

                f = open(output_file, "w")
                json.dump(my_list, f, indent=4)
                f.close()
    # if the output file is with csv extension
    elif ".csv" in output_file:
        with open(filename) as f:
            reader = csv.reader(f)
            for row in reader:
                my_lists = []
                my_lists.append(row[0])
                name = row[1].strip()
                my_lists.append(convert_time_local(name))
                temp = row[2].lower()
                my_lists.append(convert_temperatures(temp))
                f = open(output_file, "a")
                writer = csv.writer(f)
                writer.writerow(my_lists)
                f.close()
