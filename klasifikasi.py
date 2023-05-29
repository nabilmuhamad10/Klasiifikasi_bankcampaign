import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('bankmarketing.sav', 'rb'))

st.title('Prediksi Bank Marketing Campaign')
c1, c2 = st.columns(2)

with c1:
   age = st.number_input('Umur Klien')
   default = st.number_input('Kredit gagal dibayar')
   loan = st.number_input('Pinjaman Klien')
   month = st.number_input('Bulan kontak terakhir')
   duration = st.number_input('Durasi panggilan')
   pdays = st.number_input('Jumlah hari terakhir dihubungi')
   poutcome = st.number_input('Hasil kampanye sebelumnya')
   nr_employed = st.number_input('Jumlah Karyawan')

with c2:
   marital = st.number_input('Status hubungan Klien')
   housing = st.number_input('Pinjaman Perumahan')
   contact = st.number_input('Jenis komunikasi dengan Klien')
   day_of_week = st.number_input('Hari kontak terakhir')
   campaign = st.number_input('Jumlah kontak saat Kampanye')
   previous = st.number_input('Jumlah kontak sebelum kampanye')
   euribor3m = st.number_input('Suku Bbunga 3 bulan')

prediksi = ''
if st.button('Hasil Prediksi'):
    prediksi = model.predict([[age, marital, default, housing, loan, contact, month, day_of_week, duration, campaign, pdays, previous, poutcome, euribor3m, nr_employed]])

    if (prediksi [0] == 1):
        prediksi = ('Klien Berlangganan Deposit Berjangka')
    else:
        prediksi = ('Klien Tidak Berlangganan Deposit Berjangka')
st.success(prediksi)