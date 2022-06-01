import csv
import json

# Convert From CSV to JSON


def csv_to_json():
    csv_file_name = input("Input your csv file name: ") 
    if ".csv" not in csv_file_name:
        csv_file_name += ".csv" 
    json_file_name = input("Input your json file name: ")
    if ".json" not in json_file_name:
        json_file_name += ".json"
    with open(csv_file_name, "r") as mycsvfile:
        heading = next(mycsvfile)
        heading = heading.rstrip("\n")
        split_head = heading.split(",")
        reader = csv.reader(mycsvfile)
        data = []
        count = 0
        for row in reader:
          inner = dict()
          for i in row:
            inner[split_head[count]] = i
            count +=1
          data.append(inner)
          count = 0

    with open(json_file_name, "w") as myjsonfile:
        json.dump(data, myjsonfile, indent=4)
    myjsonfile.close()

def json_to_csv():
    json_file_name = input("Input your json file name: ")
    if ".json" not in json_file_name:
        json_file_name += ".json"
    csv_file_name = input("Input your csv file name: ")
    if ".csv" not in csv_file_name:
        csv_file_name += ".csv"

    with open(json_file_name, "r") as a:

        data = json.load(a)
        names = data


    with open(csv_file_name, "w") as csvfile:
        field = names[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=field, lineterminator='\n')
        writer.writeheader()
        for words in names:
            writer.writerow(words)    
    csvfile.close()  

def run_program():
    while True:
        which_do_you_want = input("Do you want to convert from csv to json or json to csv? \nFor csv to json input 'csvtojson' for json to csv input 'jsontocsv': ")
        which_do_you_want.lower()
        if which_do_you_want == "csvtojson":
            csv_to_json()
            break
        elif which_do_you_want == "jsontocsv":
            json_to_csv()
            break
        else:
            print("wrong input, input a correct selection 'csvtojson' or 'jsontocsv'")
            

run_program()
    

