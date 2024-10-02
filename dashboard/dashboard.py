import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Dashboard Title
    st.title("Bike Sharing Dashboard")

    # Load the data
    all_df = pd.read_csv('all_data.csv')

    # 1. Visualisasi Pengaruh Cuaca Terhadap Jumlah Pengguna Sepeda
    st.header("Pengaruh Cuaca Terhadap Jumlah Pengguna Sepeda")
    weather_data = all_df.groupby('weathersit_y')['cnt_y'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='weathersit_y', y='cnt_y', data=weather_data, palette='coolwarm', ax=ax)
    ax.set_title('Pengaruh Kondisi Cuaca Terhadap Jumlah Pengguna Sepeda')
    ax.set_xlabel('Kondisi Cuaca (1 = Cerah, 4 = Cuaca Buruk)')
    ax.set_ylabel('Jumlah Pengguna Sepeda')
    st.pyplot(fig)

    # 2. Perbedaan Pola Penggunaan Sepeda pada Hari Kerja vs Hari Libur
    st.header("Perbedaan Penggunaan Sepeda pada Hari Kerja vs Hari Libur")
    workingday_data = all_df.groupby('workingday_y')['cnt_y'].mean().reset_index()
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(x='workingday_y', y='cnt_y', data=workingday_data, palette='Set2', ax=ax2)
    ax2.set_title('Perbedaan Penggunaan Sepeda pada Hari Kerja vs Hari Libur')
    ax2.set_xlabel('Hari Kerja (0 = Libur, 1 = Hari Kerja)')
    ax2.set_ylabel('Rata-rata Jumlah Pengguna Sepeda')
    st.pyplot(fig2)
    st.sidebar.header("Filter Data")
    workingday_filter = st.sidebar.selectbox("Pilih Hari Kerja/Libur", options=[0, 1], index=0)
    filtered_data = all_df[all_df['workingday_y'] == workingday_filter]
    st.write(f"Menampilkan data untuk {'Hari Libur' if workingday_filter == 0 else 'Hari Kerja'}")
    st.dataframe(filtered_data[['dteday', 'cnt_y', 'weathersit_y', 'workingday_y']])

if __name__ == "__main__":
    main()
