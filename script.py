from functions import read_data_from_excel
from functions import save_data_to_excel
from functions import filtration


data = read_data_from_excel(file_path=r'C:\projects\python-app\dane.xlsx')

correct_data = filtration(data=data)

save_data_to_excel(
    output_file_path=r'C:\projects\python-app\nowyplik.xlsx',
    correct_data=correct_data
    )