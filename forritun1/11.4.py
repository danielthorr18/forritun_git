def get_emails():
    empty_list = []
    while True:
        netfang = input("Email address: ")
        if netfang != 'q':
            empty_list.append(netfang)
        else:
            return empty_list

def get_names_and_domains(listinn_minn):
    new_list = []
    for email in listinn_minn:
        split_list = email.split('@')
        new_list.append(tuple(split_list))
    return new_list


# Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)