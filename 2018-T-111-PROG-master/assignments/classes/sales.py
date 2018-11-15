class Sales:
    def __init__(self, data):
        self.__sales_data = data

    def get_average(self):
        average = sum(self.__sales_data) / len(self.__sales_data)
        return average

    def add_sale(self, sale):
        self.__sales_data.append(sale)


def read_data_from_file(filename):
    content = open(filename, "r")
    data = []
    for line in content:
        data.append(float(line.strip()))
    content.close()
    return data

def main():
    data = read_data_from_file("sales.txt")
    sales = Sales(data)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))
    sales.add_sale(78.5)
    average_sales = sales.get_average()
    print("Average sales: {:.2f}".format(average_sales))

main()