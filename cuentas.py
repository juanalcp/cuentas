import pandas as pd

df = pd.read_excel('input/test.xlsx')

def get_column(value):
    return df.iloc[:,value].iloc[4:]

documento = df.iloc[4:,1:]

fechas = get_column(1);
conceptos = get_column(3);
movimientos = get_column(4);
importes = get_column(5);
disponibles = get_column(7)
observaciones = get_column(9)

cafes = documento.loc[conceptos.str.contains("Dolce milano")]
pataPuerca = documento.loc[conceptos.str.contains("Patapuerca")]


diferenciaMensual = "Has ahorrado: " + str(disponibles.iloc[0] - disponibles.iloc[-1])

print(conceptos)

print(cafes, pataPuerca)