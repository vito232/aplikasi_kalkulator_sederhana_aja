import streamlit as st

st.header('Aplikasi Penjumlahan bilangan numerik',divider='rainbow')

angka_pertama = st.number_input('masukkan angka pertama')
st.write('the first number is ', angka_pertama)

angka_kedua = st.number_input('masukkan angka kedua')
st.write('the second number is ', angka_kedua)

operasi_matematika = angka_pertama * angka_kedua
tambah = angka_pertama + angka_kedua
kurang  = angka_pertama - angka_kedua
bagi = angka_pertama / angka_kedua
st.write(f'{angka_pertama} x  {angka_kedua} = {operasi_matematika}')
st.write(f' {angka_pertama} +  {angka_kedua} = {tambah}')
st.write(f' {angka_pertama} -  {angka_kedua} = {kurang}')
st.write(f' {angka_pertama} /  {angka_kedua} = {bagi}')