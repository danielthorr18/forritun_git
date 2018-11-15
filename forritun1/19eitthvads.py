# Implement the class Sales which has a private member variable which contains sales data. 
# Implement the member functions needed for the following program to run:
# def main():
#     data = read_data_from_file("sales.txt")
#     sales = Sales(data)
#     average_sales = sales.get_average()
#     print("Average sales: {:.2f}".format(average_sales))
#     sales.add_sale(78.5)
#     average_sales = sales.get_average()
#     print("Average sales: {:.2f}".format(average_sales))
# main()
# In addition to the member functions in the Sales class, you need to implement the 
#  function read_data_from_file () which reads data from the file sales.txt into a list and returns that list.
# No text file is given but you should create one yourself and test your code using it.
# Example :
# Given the following contents of the input file sales.txt
# 128.4
# 298.2
# 10.9
# 835.6
# 45.7
# 99.9
# 101.5
# 78.3
# the program writes out:
# Average sales: 199.81
# Average sales: 186.33
 

# You should submit both the main program and the code for the class


def read_data_from_file(file_):
        try:
            file_ = open(file_, 'r')
            data = []
            for line in file_:
                data.append(float(line))
            file_.close()
            return data
        except FileNotFoundError:
            print("Documents not found.")
            return []

class Sales:
    def __init__(self, data=[]):
        self.__data = data

    def get_average(self):
        the_sum = sum(self.__data)
        the_len = len(self.__data)
        return the_sum/the_len
    
    def add_sale(self, new_number):
        self.__data.append(new_number)




# The main program starts here
def main():
    data = read_data_from_file("sales.txt")
    sales = Sales(data)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))
    sales.add_sale(78.5)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))

main()