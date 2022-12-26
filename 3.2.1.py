import csv


class Csv_cutter_by_years:
    def __init__(self, file_name):
        self.file_name = file_name
        self.headers = []
        self.info = {}

    def separate_csv(self):
        for year in self.info:
            with open(f'csv_files/new_csv_{year}.csv', 'w', newline='', encoding="utf-8-sig") as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for row in self.info[year]:
                    filewriter.writerow(row)

    def read_file(self):
        flag = True
        with open(self.file_name, encoding="utf-8-sig") as File:
            reader_obj = csv.reader(File)
            for current_row in reader_obj:
                if flag:
                    self.headers = current_row
                    flag = False
                else:
                    if current_row[-1][:4] in self.info.keys():
                        self.info[current_row[-1][:4]].append(current_row)
                    else:
                        self.info[current_row[-1][:4]] = [self.headers, current_row]


name = input("Введите название файла для парсинга по годам: ")
cutter = Csv_cutter_by_years(name)
cutter.read_file()
cutter.separate_csv()
