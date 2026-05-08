import streamlit as st

st.title('teste')

n1 = st.number_input('peso')
n2 = st.number_input('altura', value = 0.1)


imc = n1/(n2**2)


if st.button('calcular imc'):
    if imc:
        st.sucess(imc)
#-----------------------------------------------

# 3

# formulário

st.caption('CADASTRO SIMPLES')

NOME = st.text_input('Nome: ')
idade = st.number_input('idade: ')
email = st.text_input ('E-mail: ')
altura = st.number_input('Altura: ')


if st.button ('Cadastrar'):
    st.sucess('Pessoa cadastrada')


# 4

# Tabuada

numero = st.number_input('numero: ')


if st.button('calcular:'):
     for x in range (0,11):
         calculo = x * numero
         st.write(x, 'x', numero,'=',calculo)



   