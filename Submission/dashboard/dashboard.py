import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import random
from babel.numbers import format_currency
sns.set(style='dark')

# Fungsi untuk generate warna
def make_color(n):
  color = []
  for i in range(n):
    r = lambda: random.randint(0,255)
    ranhex= '#%02X%02X%02X' % (r(),r(),r())
    color.append(ranhex)
  return color

# Load data
hour_df = pd.read_csv("hour_data.csv")
day_df = pd.read_csv("day_data.csv")

with st.sidebar:
    st.image("https://raw.githubusercontent.com/IrfanArsyananda/Analisis-Data-dengan-Python/main/Submission/dashboard/bike-sharing-logo.jpg")
    st.header("Bike Sharing Club")
    st.text("Nama : Irfan Arsyananda")
    st.text("Link Dicoding ⬇️⬇️")
    st.link_button("Go to Profile", "https://www.dicoding.com/users/irfanarsyananda")
    
# Melengkapi Dashboard dengan Berbagai Visualisasi Data
st.title('Bike Sharing Statistics')

st.header('Rata-rata Jumlah Sewa Berdasarkan:')
tab1, tab2, tab3 = st.tabs(["Jam", "Cuaca", "Musim"])
 
with tab1:
    # Rata-rata jumlah sewa berdasarkan jam
    st.subheader("Jumlah Sewa Berdasarkan Jam")
    byhr = hour_df.groupby(by="hr").cnt.mean().reset_index()

    fig, ax = plt.subplots(figsize=(20, 10))
    
    sns.barplot(x="hr", y="cnt", data=byhr.sort_values(by="hr", ascending=True), palette=make_color(1))
    ax.set_ylabel("",  fontsize=30)
    ax.set_xlabel("Jam", fontsize=30)
    # ax.set_title("X", loc="center", fontsize=50)
    ax.tick_params(axis='y', labelsize=30)
    ax.tick_params(axis='x', labelsize=30)
    st.pyplot(fig)
 
with tab2:
    # Rata-rata jumlah sewa berdasarkan cuaca
    st.subheader("Jumlah Sewa Berdasarkan Cuaca")
    byweather_df = hour_df.groupby(by="weathersit").cnt.mean().reset_index()

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(x="weathersit", y="cnt", data=byweather_df.sort_values(by="cnt", ascending=False), palette=make_color(1))
    ax.set_ylabel("",  fontsize=30)
    ax.set_xlabel("Cuaca", fontsize=30)
    # ax.set_title("X", loc="center", fontsize=50)
    ax.tick_params(axis='y', labelsize=30)
    ax.tick_params(axis='x', labelsize=30)
    st.pyplot(fig)
 
with tab3:
    # Rata-rata jumlah sewa berdasarkan musim
    st.subheader("Jumlah Sewa Berdasarkan Musim")
    byseason_df = day_df.groupby(by="season").cnt.mean().reset_index()

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(x="season", y="cnt", data=byseason_df.sort_values(by="cnt", ascending=False), palette=make_color(1))
    ax.set_ylabel("",  fontsize=30)
    ax.set_xlabel("Musim", fontsize=30)
    # ax.set_title("X", loc="center", fontsize=50)
    ax.tick_params(axis='y', labelsize=30)
    ax.tick_params(axis='x', labelsize=30)
    st.pyplot(fig)
    

# Total jumlah sewa berdasarkan bulan
st.header("Total Jumlah Sewa Berdasarkan Bulan")
bymonth_df = day_df.groupby(by="mnth").cnt.sum().reset_index()
month_name_df = day_df["month"].unique()

fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(x=month_name_df, y=bymonth_df["cnt"], palette=make_color(1))
ax.set_ylabel("",  fontsize=30)
# ax.set_xlabel("Bulan", fontsize=30)
# ax.set_title("X", loc="center", fontsize=50)
plt.xticks(rotation=40)
ax.tick_params(axis='y', labelsize=30)
ax.tick_params(axis='x', labelsize=30)
st.pyplot(fig)

# Jumlah sewa berdasarkan hari kerja
st.header("Total Jumlah Sewa Berdasarkan Hari Kerja")
byworkingday_df = day_df.groupby(by="workingday").cnt.sum().reset_index()

labels = byworkingday_df["workingday"]
sizes = byworkingday_df["cnt"]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
ax1.axis('equal')
ax1.set_title("Hari kerja?", fontsize=20)
st.pyplot(fig1)

st.caption('Irfan Arsyananda © - Dicoding 2023')