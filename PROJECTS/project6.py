min_number = float('inf')
min_state = ""
max_number = 0
max_state = ""
empty = ""

HEART_DISEASE =  1
MOTOR_DEATHS =  5
TEEN_BIRTH_RATE = 7
ADULT_SMOKING = 11
ADULT_OBESITY =  13




def check_data():
   try:
       filename = input("Enter filename containing csv data: ")
       dataFile = open(filename, "r")
       return filename
   except FileNotFoundError:
       print("Cannot find file {}".format(filename))
       return False

def print_above_line():
   print ("%-33s%-21s%6s%6s%-15s%6s" %("Indicator", "Min", empty, empty, "Max", empty))
   print ("-"*87)

def find_min(file_name, min_number, min_state, position):
   value = min_number
   with open (file_name, "r") as data:
       for line in data.readlines():
           try:
               value = float(line.split(",")[position].replace("%", ""))
               state = str(line.split(",")[0])
           except ValueError:
               value = value
           if value < min_number:
               min_number = value
               min_state = state
               formatted_number = str(round(min_number, 1))
       return (formatted_number, min_state)
  
def find_max(file_name, max_number, max_state, position):
   value = 0
   with open (file_name, "r") as data:
       for line in data.readlines():
           try:
               value = float(line.split(",")[position].replace("%", ""))
               state = str(line.split(",")[0])
           except ValueError:
               value = value
           if value > max_number:
               max_number = value
               max_state = state
               formatted_number = str(round(max_number, 1))
       return (formatted_number, max_state)

def fetch_indicator(file_name, position):
   with open (file_name, "r") as data:
       for line in data.readlines():
           indicator = str(line.split(",")[position])
           return indicator
  
def fetch_numbers(file_name, min_number, min_state, max_number, max_state, numbercode):
   position = numbercode
   indicator = (fetch_indicator(file_name, position) + ":")
   min_number, min_state = find_min(file_name, min_number, min_state, position)
   max_number, max_state = find_max(file_name, max_number, max_state, position)
   print ("%-33s%-21s%6s%6s%-15s%6s" %(indicator, min_state, min_number, empty, max_state, max_number))

def print_below_line(file_name):
   Heart_disease = fetch_numbers(file_name, min_number, min_state, max_number, max_state, HEART_DISEASE)
   Motor_vehicle = fetch_numbers(file_name, min_number, min_state, max_number, max_state, MOTOR_DEATHS)
   Teen_birth = fetch_numbers(file_name, min_number, min_state, max_number, max_state, TEEN_BIRTH_RATE)
   Adult_smoking = fetch_numbers(file_name, min_number, min_state, max_number, max_state, ADULT_SMOKING)
   Adult_obesity = fetch_numbers(file_name, min_number, min_state, max_number, max_state, ADULT_OBESITY)
  
def main():
   file_name = check_data()
   print_above_line()
   if file_name != False:
       print_below_line(file_name)


















main()