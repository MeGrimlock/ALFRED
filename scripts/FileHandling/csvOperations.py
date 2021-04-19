import csv


def saveFile(data, file_name):
    """Stores [data] into a new CSV file [file_name].csv"""
    with open(file_name, mode="w") as parsed_file:
        file_writer = csv.writer(parsed_file, delimiter=",")
        # Save column headers
        file_writer.writerow(data[1])
        # save Data
        for row in data[0]:
            file_writer.writerow(row)
    print("Done saivng file: \n", file_name)
    return "done"


def openEmailsCSV(my_file="ingComMaro2021.csv"):
    """
    Parameters:
        my_file: Filename of the CSV file to open

    Output:
        raw_emails: List of elements extracted from the file wit the following format
                [email[0], email[1] ... email[n]]

    """
    with open(my_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        raw_emails = []
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                # print "Encabezados:\n"+str(row)
            else:
                line_count += 1
                raw_emails.append(row)
    return raw_emails