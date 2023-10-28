import pandas as pd
import csv
import os


def le_dados_challenge(arquivo, index):
    if list(arquivo)[-1] == 'v':
        data_frame = pd.read_csv(arquivo)
    else:
        data_frame = pd.read_excel(arquivo)

    role = data_frame["Role in Company"][index]
    email = data_frame["Email"][index]
    first_name = data_frame["First Name"][index]
    last_name = data_frame["Last Name"][index]
    phone = str(data_frame["Phone Number"][index])
    company = data_frame["Company Name"][index]
    address = data_frame["Address"][index]

    return [first_name, last_name, company, role, address, email, phone]


def cria_csv(file_path):
    header = ['First Name', 'Last Name', 'Company Name', 'Role in Company', 'Address', 'Email', 'Phone Number']

    if os.path.exists(file_path):
        os.remove(file_path)

    with open((file_path), 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)


def escreve_csv(file_path, row):
    with open((file_path), 'a', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)
