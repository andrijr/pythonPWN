import pandas as pd


def generate_new_data():
    df = pd.read_csv('student_applications_data_n.csv', sep=';')
    df.to_csv(path_or_buf='new_students_data.csv')