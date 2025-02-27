import pandas as pd
import altair as alt

df = pd.read_excel('NomeDoArquivo.xls')

charte = alt.Chart(df).mark_point(filled=True, size=100).encode(
    x= 'Eixo X',
    y= 'Eixo Y',
    color='Cores',
    tooltip=['Informacoes ao passar o mouse por cima']
).properties(
    width=800,
    height=800).interactive()

charte.save('scatter.html')