years_str = input("Years: ")
years_int = int(years_str)
current_int = 307357870
birth_int = (years_int * (365*60*60*24)) / 7
death_int = (years_int * (365*60*60*24)) / 13
immigrant_int = (years_int * (365*60*60*24))/ 35
new_population = current_int + birth_int + immigrant_int - death_int


print("New population after", years_int, " years is ", int(new_population))
