import streamlit as st
import pandas as pd
import sqlite3
st.title("System Monitorowania alertów")


def pobierz_dane():
    pol = sqlite3.connect('SQL_SIEM.db')
    d = pd.read_sql_query("SELECT * FROM alerty", pol)
    pol.close()
    return d


dane = pobierz_dane()

if not dane.empty:
    st.subheader("Ostatnie alerty:")
    st.dataframe(dane)
    st.subheader("Najczęściej występujące adresy ip:")
    wykres_dane = dane['ip_nr'].value_counts()
    st.bar_chart(wykres_dane)
else:
    st.success("Brak ataków w bazie. System jest bezpieczny! ")    
