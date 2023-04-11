import streamlit as st
import pandas as pd

from PIL import Image
imagen = Image.open('rot_alimento.jpg')

lista_alimento = ['Bacon Frito', 'Costela de porco', 'Camarão', 'Mortandela', 
                  'Maça Vermelha', 'Abacaxi', 'Alface', 'Brocolis', 'Cebola',
                  'Pão Frances', 'Pão Integral', 'Cerveja']
lista_porcao = [30, 100, 100, 15, 130, 80, 20, 80, 70, 50, 100, 350]
medida = ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'ml']
lista_calorias = [235, 483, 310, 41, 85, 50, 4, 23, 32, 135, 261, 147]

dicionario_alimentos = {'Alimento':lista_alimento,
                        'Porção':lista_porcao,
                        'Medida':medida,
                        'Calorias': lista_calorias}

df = pd.DataFrame(dicionario_alimentos)

st.set_page_config(layout='centered', page_title='Informações Caloricas dos Alimentos')

st.header('CONSULTAR INFORMAÇÕES DE CALORIAS DE ALIMENTOS')

st.subheader('Calorias de cada alimento', help='Selecione um alimento para suas informações')
selecionar_alimento = st.selectbox(label='Alimentos', options=lista_alimento, index=0, help='Selecione um alimento para ver suas informações de calorias')
if selecionar_alimento:
   st.table(df.loc[df['Alimento']==selecionar_alimento])

st.subheader('Calculadora de calorias', help='Calcule as calorias de um alimento com base na sua tabela energetica')
with st.expander('Abrir calculadora de calorias do alimento', True):

   st.image(image=imagen, width=200, caption='Exemplo de Rotulo Nutricional\nGordura=0, Carboidratos=35g e Proteina=3,2g, Calorias = 152.80 a cada 50g de arroz')
   st.info('Para cada grama(g) de gordura o alimento tem 9 calorias')
   gordura = st.number_input('Gordura', min_value=0.00, value=0.00)
   st.info('Para cada grama(g) de carboidrato o alimento tem 4 calorias')
   carboidratos = st.number_input('Carboidratos', min_value=0.00, value=0.00)
   st.info('Para cada grama(g) de proteina o alimento tem 4 calorias')
   proteinas = st.number_input('Proteina', min_value=0.00, value=0.00)

   total_caloria = (gordura*9)+(carboidratos*4)+(proteinas*4)
   text_caloria = f'Gordura: {gordura} * 9 = {gordura*9}\nCarboidrato: {carboidratos} * 4 = {carboidratos*4}\nProteina: {proteinas} * 4 = {proteinas*4}'

   if gordura != 0 or carboidratos != 0 or proteinas != 0:
      st.text_area(label='Descrição do Calculo', placeholder='Calorias', value=text_caloria)
      st.success(f'Calorias totais do alimento: {total_caloria:.2f}')

st.subheader('Tabela Nutricional de alimentos', help='Veja as calorias de alimentos comuns no dia a dia')
with st.expander('Visualisar  Tabela'):
   st.subheader('Clique na coluna que desejar para ordenar os dados')
   st.dataframe(df, width=5000)


