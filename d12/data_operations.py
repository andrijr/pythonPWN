from sklearn import preprocessing
import pandas as pd


def drop_unnecessary_columns(data_frame):
    data_frame = data_frame.drop(columns=[
        'Numer dokumentu',
        'Student',
        'Semestr rejestracji',
        'Brakujace przedmioty',
        'Stopień zaawansowania pracy',
        'Informacje o pracach dyplomowych',
        'Osoba przyjmująca',
        'Osoba przypisana'
    ])
    return data_frame


def parametrize_columns(data_frame):
    data_frame = data_frame[
        (data_frame['Status'] == 'Zamknięty - decyzja negatywna') |
        (data_frame['Status'] == 'Zamknięty - decyzja pozytywna')
        ]

    le = preprocessing.LabelEncoder()
    data_frame['Status'] = le.fit_transform(data_frame["Status"])
    return data_frame


def categorize_columns(data_frame):
    columns = [
        'Liczba brakujacych przedmiotow',
        'Brakujace ECTS',
        'ECTS uznane w bieżącym semstrze'
    ]
    # for column in columns:
    for i, column in enumerate(columns):
        if i == 0:
            data_frame['brakujace_przedmioty_cat'] = pd.cut(
                data_frame[column],
                bins=[0, 0.5, 5, max(data_frame[column])],
                include_lowest=True
            )
        if i == 1:
            data_frame['brakujace_ects_cat'] = pd.cut(
                data_frame[column],
                bins=[0, 0.5, max(data_frame[column])],
                include_lowest=True
            )
        if i == 2:
            data_frame['uznane_ects_cat'] = pd.cut(
                data_frame[column],
                bins=[0, 0.5, 36, max(data_frame[column])],
                include_lowest=True
            )
        return data_frame