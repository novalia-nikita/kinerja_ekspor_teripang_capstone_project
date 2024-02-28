import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import base64
# import seaborn as sns
# import plotly.express as px
# import plotly.graph_objects as go
# from graphviz import Digraph


st.set_page_config(layout='wide')

df1 = pd.read_csv("produksi_id.csv")
df2 = pd.read_csv("export_id.csv")
df3 = pd.read_csv("importers_id.csv")
df4 = pd.read_csv("importers_global.csv")
df5 = pd.read_csv("habitat_id.csv")
# df6 = pd.read_csv("exporters_global.csv")

# st.dataframe(df6)


# # Menampilkan judul
# st.title('ANALISIS KINERJA EKSPOR KOMODITAS TERIPANG DI INDONESIA')

# Menampilkan judul konten di tengah
st.markdown("<h1 style='text-align: center;'>ANALISIS KINERJA EKSPOR KOMODITAS TERIPANG DI INDONESIA</h1>", unsafe_allow_html=True)

# Image
from PIL import Image

image1 = Image.open("teripang.jpg")

# # Mengonversi path relatif ke path absolut
# gambar_path_absolut = os.path.abspath(image)

# Menampilkan gambar di tengah
st.image(image1, caption="Teripang di habitatnya. Sumber: www.seafdec.org.ph", use_column_width=True, output_format='auto')


# Tabbing
tab1, tab2, tab3, tab4 = st.tabs(['TENTANG TERIPANG (Holothuria sp.)','PRODUKSI TERIPANG DI INDONESIA', 'KINERJA EKSPOR TERIPANG DI INDONESIA', 'KESIMPULAN DAN REKOMENDASI'])

with tab1:
    # st.header("Header")
    # st.subheader("Subheader")
    # Paragraf yang ingin ditampilkan
    paragraf1 = """
    Indonesia sebagai negara kepulauan yang sebagian besar wilayahnya terdiri dari 70% lautan.
    Wilayah lautan ini kaya akan berbagai sumber daya alam, baik yang bersifat hayati maupun non-hayati.
    Salah satu sumber daya hayati laut di Indonesia adalah teripang.
    Teripang memiliki ciri khas tubuh lunak, berbentuk silindris seperti mentimun, dan berotot melingkar dari mulut hingga anus.
    Hewan ini dikenal sebagai timun laut atau "beche-de-mer" di perdagangan internasional.
    Hewan ini menjadi komoditi ekspor non-migas yang penting bagi Indonesia, menghasilkan devisa negara dari berbagai negara tujuan ekspor.
    """

    # Menampilkan paragraf di Streamlit
    st.markdown(f'<p style="font-family: Arial; font-size: 16px;">{paragraf1}</p>', unsafe_allow_html=True)



    # Menampilkan Manfaat Teripang dalam berbagai bidang
    image2 = Image.open("manfaat_teripang.jpg")

    with st.expander("Manfaat teripang dalam berbagai bidang"):
        st.image(image2)

with tab2:
    # #helper function
    # def format_big_number(num):
    #     if num <= 1e6:
    #         return f"{num:,.0f}"
    #     else:
    #         return f"{num}"

    st.header("Produksi Teripang di Indonesia")

    # Fungsi untuk menghitung rata-rata harga_per_kg
    def hitung_rata_rata_harga(df1_filtered, tahun):
        return df1_filtered[df1_filtered['tahun'] == tahun]['harga_per_kg'].mean()

    # Fungsi untuk memformat tahun
    def format_tahun(tahun):
        return str(int(tahun))

    # Filter data berdasarkan tahun (2019 - 2022)
    df1_filtered = df1[(df1['tahun'] >= 2019) & (df1['tahun'] <= 2022)]

    # Persiapkan data untuk chart
    data1_chart = pd.DataFrame({
        'tahun': [2019, 2020, 2021, 2022],
        'rata-rata harga per kg (Rp)': [0, 0, 0, 0]
        })

    # Hitung rata-rata harga_per_kg untuk setiap tahun
    for i, row in data1_chart.iterrows():
        tahun = row['tahun']
        data1_chart.at[i, 'rata-rata harga per kg (Rp)'] = hitung_rata_rata_harga(df1_filtered, tahun).astype(int)


    # Memformat kolom tahun
    data1_chart['tahun'] = data1_chart['tahun'].apply(format_tahun)

    # Memformat kolom harga_per_kg
    # data1_chart['rata-rata harga per kg (Rp)'] = data1_chart['rata-rata harga per kg (Rp)'].apply(format_big_number)

    # Buat chart Altair
    price1_chart = alt.Chart(data1_chart).mark_line().encode(
        x='tahun',
        y='rata-rata harga per kg (Rp)'
    ).properties(
        width=500,
        height=400,
        title='Rata-rata Harga per kg Teripang (2019-2022)'
    )

    # Tampilkan chart menggunakan Streamlit
    # st.altair_chart(price1_chart, use_container_width=True)


    # Fungsi untuk menghitung jumlah produksi teripang setiap tahunnya
    def hitung_volume_produksi(df1_filtered, tahun):
        return df1_filtered[df1_filtered['tahun'] == tahun]['volume_produksi'].sum()


    # Persiapkan data untuk chart
    data2_chart = pd.DataFrame({
        'tahun': [2019, 2020, 2021, 2022],
        'jumlah volume produksi(kg)': [0, 0, 0, 0]
    })

    # Hitung volume produksi untuk setiap tahun
    for i, row in data2_chart.iterrows():
        tahun = row['tahun']
        data2_chart.at[i, 'jumlah volume produksi(kg)'] = hitung_volume_produksi(df1_filtered, tahun)

    # Memformat kolom tahun
    data2_chart['tahun'] = data2_chart['tahun'].apply(format_tahun)

    # Buat chart Altair
    volume1_chart = alt.Chart(data2_chart).mark_line().encode(
        x='tahun',
        y='jumlah volume produksi(kg)'
    ).properties(
        width=500,
        height=400,
        title='Volume Produksi Teripang (2019-2022)'
    )

    # Tampilkan chart menggunakan Streamlit
    # st.altair_chart(volume1_chart, use_container_width=True)

    # Tampilkan chart secara sejajar
    # Buat container untuk menampung kedua chart
    container1 = st.container()

    # Tampilkan chart secara sejajar
    col1, col2 = container1.columns(2)
    col1.altair_chart(price1_chart)
    col2.altair_chart(volume1_chart)


    # Paragraf Penjelasan Produksi Teripang pada Tahun 2019-2020 yang ingin ditampilkan
    paragraf2 = """
    Berdasarkan data KKP tahun 2019 hingga 2022, harga rata-rata teripang berkisar antara Rp.100.000-Rp.150.000/kg dan meningkat setiap tahunnya, sedangkan volume produksi mengalami penurunan.
    Tingginya harga teripang mendorong penangkapan berlebihan yang berakibat pada minimnya pengelolaan sumber daya teripang.
    Meskipun berhasil dalam upaya pembenihan teripang, tidak cukup untuk mengatasi hal ini karena jangka waktu pembenihan hingga pemanenan teripang membutuhkan waktu selama 11 bulan.
    Oleh karena itu, pengelolaan yang lebih baik diperlukan untuk melestarikan dan memastikan keberlanjutan sumber daya teripang.
    Produksi teripang yang berasal dari penangkapan di laut, selain menyebabkan ketidakstabilan produksi, juga menghasilkan hasil tangkapan teripang yang bervariasi dalam jenis dan ukuran.
    Pemerintah melakukan peraturan pembatasan melalui Kementerian Perdagangan dan Kementerian Lingkungan Hidup dan Kehutanan.
    Aturan ini membatasi pendistribusian teripang di pasar internasional berdasarkan jenis dan volume.


    Sumber:
    1. Produksi Perikanan Tangkap Laut - Statistik-KKP
    2. Aspek Biologi dan Budidaya Teripang Pasir - Tim BRSDMKP
    """

    # Menampilkan paragraf2 di Streamlit
    with st.expander("Penjelasan Produksi Teripang:"):
        st.markdown(f'<p style="font-family: Arial; font-size: 16px;">{paragraf2}', unsafe_allow_html=True)



    # Menghitung jumlah total volume produksi untuk setiap provinsi dari tahun 2019 sampai 2022
    df1_total_volume2 = df1.groupby('provinsi')['volume_produksi'].sum().reset_index()

    # Membuat horizontal bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(df1_total_volume2['provinsi'], df1_total_volume2['volume_produksi'], color='skyblue')
    ax.set_xlabel('Jumlah Volume Produksi Teripang (juta kg)')
    ax.set_ylabel('Provinsi')
    ax.set_title('Provinsi Penghasil Teripang di Indonesia (2019-2022)')

    # Menampilkan plot menggunakan Streamlit
    st.pyplot(fig)



    # Menghitung jumlah total jenis teripang untuk setiap provinsi
    df5_total_jenis = df5.groupby('provinsi')['jumlah_jenis_teripang'].sum().reset_index()

    # Membuat horizontal bar chart
    fig2, ax = plt.subplots(figsize=(10, 6))
    ax.barh(df5_total_jenis['provinsi'], df5_total_jenis['jumlah_jenis_teripang'], color='skyblue')
    ax.set_xlabel('Jumlah Jenis Teripang')
    ax.set_ylabel('Provinsi')
    ax.set_title('Sebaran dan Habitat Teripang di Indonesia')

    # Menampilkan plot menggunakan Streamlit
    st.pyplot(fig2)


    # Paragraf Penjelasan Provinsi penghasil teripang pada Tahun 2019-2022 yang ingin ditampilkan
    paragraf3 = """
    Sebaran dan habitat teripang banyak di perairan Jawa Tengah, Jawa Timur, Nusa Tenggara Barat, Sulawesi, Kalimantan Timur, Maluku, Papua, dan Papua Barat, sisanya ada di 7 provinsi lainnya. 
    Data Kementerian Kelautan dan Perikanan (KKP) dari tahun 2019 hingga 2022 menunjukkan bahwa Jawa Timur, Maluku, Sulawesi Selatan, Kalimantan Timur, dan Sulawesi Tenggara menjadi lima provinsi penyumbang produksi teripang nasional. Sisanya tersebar di 16 provinsi lainnya di Indonesia.
    Dari data tersebut, dapat disimpulkan bahwa teripang lebih banyak tumbuh di Indonesia bagian tengah dan timur. Meskipun produksi teripang tersebar di seluruh wilayah Indonesia, sebagian besar pengiriman ekspor hanya dilakukan dari beberapa daerah saja.
    Hal ini menunjukkan potensi pengembangan budidaya teripang di seluruh Indonesia, dengan fokus pada peningkatan kualitas dan akses pasar ekspor untuk meningkatkan nilai ekonomi bagi para pembudidaya.


    Sumber:
    1. Produksi Perikanan Tangkap Laut - Statistik-KKP
    2. Teripang Indonesia: Jenis, Sebaran, dan Status Nilai Ekonomi - Setyastuti, dkk.
    """

    # Menampilkan paragraf3 di Streamlit
    with st.expander("Penjelasan provinsi penghasil teripang (2019-2022):"):
         st.markdown(f'<p style="font-family: Arial; font-size: 16px;">{paragraf3}', unsafe_allow_html=True)


with tab3:
    st.header("Kinerja Ekspor Teripang di Indonesia")

    # Menampilkan Ekspor Teripang di Indonesia (2014-2022)    
    # Menghitung jumlah fob_value untuk setiap tahun dari 2014 sampai 2022
    df2_total_fob = df2.groupby('year')['fob_value'].sum().reset_index()

    # Membuat line chart menggunakan Altair
    fob1_value_chart = alt.Chart(df2_total_fob).mark_line().encode(
        y=alt.Y('fob_value:Q', title='Nilai Ekspor Teripang di Indonesia (USD)'),
        x=alt.X('year:N', title='Tahun'),
        tooltip=['year:N', alt.Tooltip('fob_value:Q', title='Nilai Ekspor Teripang di Indonesia (USD)')],
    ).properties(
        width=500,
        height=400,
        title='Nilai Ekspor Teripang di Indonesia (2014-2022)'
    )

    # # Menampilkan plot menggunakan Streamlit
    # st.altair_chart(fob1_value_chart)


    # Menghitung jumlah net_weight untuk setiap tahun dari 2014 sampai 2022
    df2_total_net_weight = df2.groupby('year')['net_weight'].sum().reset_index()

    # Membuat line chart menggunakan Altair
    net_weight1_chart = alt.Chart(df2_total_net_weight).mark_line().encode(
        y=alt.Y('net_weight:Q', title='Volume Ekspor Teripang di Indonesia (kg)'),
        x=alt.X('year:N', title='Tahun'),
        tooltip=['year:N', alt.Tooltip('net_weight:Q', title='Volume Ekspor Teripang di Indonesia (kg)')],
    ).properties(
        width=500,
        height=400,
        title='Volume Ekspor Teripang di Indonesia (2014-2022)'
    )

    # # Menampilkan plot menggunakan Streamlit
    # st.altair_chart(net_weight1_chart)

    # Tampilkan chart secara sejajar
    # Buat container untuk menampung kedua chart
    container2 = st.container()

    # Tampilkan chart secara sejajar
    col3, col4 = container2.columns(2)
    col3.altair_chart(fob1_value_chart)
    col4.altair_chart(net_weight1_chart)



    # Menampilkan Grafik Laju Pertumbuhan Nilai Ekspor dan Volume Ekspor Teripang di Indonesia Tahun 2014-2022
    ## Laju Pertumbuhan Nilai Ekspor Teripang di Indonesia Tahun 2014-2022
    # Mengurutkan data berdasarkan tahun
    df2_sort_year1 = df2.sort_values('year')

    # Membuat kolom laju_pertumbuhan
    df2_sort_year1['laju_pertumbuhan_nilai'] = df2_sort_year1['fob_value'].pct_change() * 100

    # Filter data tahun 2015-2022
    filtered_df2 = df2_sort_year1[df2_sort_year1['year'].between(2015, 2022)]

    # # Menampilkan data
    # st.dataframe(filtered_df2)

    # Membuat grafik dengan Altair
    laju_pertumbuhan1_chart = alt.Chart(filtered_df2).mark_line().encode(
        y=alt.Y('laju_pertumbuhan_nilai:Q',title='Laju Pertumbuhan Nilai Ekspor Teripang di Indonesia (%)'),
        x=alt.X('year:N', title='Tahun'),
        tooltip=['year:N', alt.Tooltip('laju_pertumbuhan_nilai:Q', title='Laju Pertumbuhan Nilai Ekspor di Indonesia (%)')],
    ).properties(
        width=500,
        height=400,
        title='Laju Pertumbuhan Nilai Ekspor Teripang (2015-2022)'
    )

    # # Menampilkan grafik di Streamlit
    # st.altair_chart(laju_pertumbuhan1_chart, use_container_width=True)


    ## Laju Pertumbuhan Volume Ekspor Teripang di Indonesia Tahun 2014-2022
    # Mengurutkan data berdasarkan tahun
    df2_sort_year1 = df2.sort_values('year')

    # Membuat kolom laju_pertumbuhan
    df2_sort_year1['laju_pertumbuhan_volume'] = df2_sort_year1['net_weight'].pct_change() * 100

    # Filter data tahun 2015-2022
    filtered_df2 = df2_sort_year1[df2_sort_year1['year'].between(2015, 2022)]

    # # Menampilkan data
    # st.dataframe(filtered_df2)

    # Membuat grafik dengan Altair
    laju_pertumbuhan2_chart = alt.Chart(filtered_df2).mark_line().encode(
        x=alt.X('year:N', title='Tahun'),
        y=alt.Y('laju_pertumbuhan_volume:Q',title='Laju Pertumbuhan Volume Ekspor Teripang di Indonesia (%)'),
        tooltip=['year:N', alt.Tooltip('laju_pertumbuhan_volume:Q', title='Laju Pertumbuhan Volume Ekspor di Indonesia (%)')],
    ).properties(
        width=500,
        height=400,
        title='Laju Pertumbuhan Volume Ekspor Teripang (2015-2022)'
    )

    # # Menampilkan grafik di Streamlit
    # st.altair_chart(laju_pertumbuhan2_chart, use_container_width=True)

    # Tampilkan chart secara sejajar
    # Buat container untuk menampung kedua chart
    container3 = st.container()

    # Tampilkan chart secara sejajar
    col5, col6 = container3.columns(2)
    col5.altair_chart(laju_pertumbuhan1_chart)
    col6.altair_chart(laju_pertumbuhan2_chart)


    # Paragraf Penjelasan Laju Pertumbuhan Nilai Ekspor dan Volume Ekspor Teripang di Indonesia pada Tahun 2015-2022 yang ingin ditampilkan
    paragraf4 = """
    Menurut Data Ekspor Impor Nasional dari BPS tahun 2014 hingga 2022, ekspor komoditas teripang mengalami fluktuatif cenderung meningkat.
    Hasil analisis perkembangan ekspor teripang dari tahun 2014 hingga 2022 sebagaimana terlihat pada Grafik Laju Pertumbuhan Nilai Ekspor dan Volume Ekspor Teripang di Indonesia menunjukkan kenaikan yang sangat besar hingga 274% untuk nilai ekspor dan 392% untuk volume ekspor.
    Meskipun volume ekspor teripang turun hingga -14% pada tahun 2017, nilai ekspor teripang mengalami kenaikan signifikan sebesar 395%.
    Hal ini menunjukkan bahwa harga teripang mengalami kenaikan yang sangat tinggi di pasar internasional.
    Meskipun nilai ekspor teripang sempat naik pada tahun 2017, namun mengalami penurunan pada tahun 2019 hingga 2021. Hal ini terjadi karena adanya Pandemi COVID-19 pada tahun 2020 hingga 2022. Namun, terjadi kenaikan kembali pada tahun 2022. Kenaikan ekspor pada tahun 2022 menunjukkan bahwa pemulihan ekonomi setelah status Pandemi COVID-19 dicabut.


    Sumber:
    Data Ekspor Impor Nasional - BPS
    """

    # Menampilkan paragraf4 di Streamlit
    with st.expander("Penjelasan nilai ekspor dan volume ekspor teripang (2014-2022):"):
        st.markdown(f'<p style="font-family: Arial; font-size: 16px;">{paragraf4}', unsafe_allow_html=True)



    # Menghitung jumlah total nilai ekspor untuk setiap negara tujuan ekspor teripang dari Indonesia (2014-2022)
    df3_total_value1 = df3.groupby('importers')['fob_value'].sum().reset_index()

    # Membuat horizontal bar chart
    fig3, ax = plt.subplots(figsize=(10, 6))
    ax.barh(df3_total_value1['importers'], df3_total_value1['fob_value'], color='skyblue')
    ax.set_xlabel('Jumlah Nilai Ekspor Teripang (puluh juta USD)')
    ax.set_ylabel('Negara-Negara Tujuan Ekspor Teripang')
    ax.set_title('Negara-Negara Tujuan Ekspor Teripang dari Indonesia')

    # Menampilkan plot menggunakan Streamlit
    st.pyplot(fig3)



    # Menghilangkan data "world" dari DataFrame
    df4_filtered = df4[df4['importers'] != 'World']

    # Mengelompokkan data berdasarkan negara tujuan ekspor dan menghitung nilai ekspor total
    total_exports = df4_filtered.groupby('importers')['fob_value'].sum().sort_values(ascending=False)

    # Mengambil 10 negara tujuan ekspor terbanyak
    top_10_countries = total_exports.head(10)

    # Membuat grafik horizontal bar chart
    fig4, ax = plt.subplots(figsize=(10, 8))
    top_10_countries.plot(kind='barh', color='skyblue')
    plt.xlabel('Jumlah Nilai Ekspor Teripang (ratus juta USD)')
    plt.ylabel('Negara Tujuan Ekspor Teripang')
    plt.title('Negara-Negara Tujuan Ekspor Teripang di Dunia')

    # Menampilkan grafik menggunakan Streamlit
    st.pyplot(fig4)



    # Paragraf Penjelasan Kinerja Ekspor Teripang yang ingin ditampilkan
    paragraf5 = """
    Lima negara tujuan ekspor teripang dari Indonesia adalah China, Korea, Hongkong, Vietnam, dan Malaysia, sedangkan 5 negara tujuan ekspor teripang secara global adalah China, Hongkong, Korea, Amerika, dan Taiwan.
    Hal ini menunjukkan negara-negara tujuan ekspor teripang terbanyak secara global mengimpor teripang dari Indonesia.
    Total nilai ekspor teripang di Indonesia pada tahun 2018 hingga 2022 adalah sebesar USD 25.057.594, sedangkan total nilai ekspor teripang di dunia pada tahun 2018 hingga 2022 adalah sebesar USD 428.609.000.
    Pangsa pasar relatif Indonesia dalam ekspor teripang sepanjang tahun 2018 hingga 2022 adalah sebesar 5,8%.
    Meskipun pangsa pasar relatif sebesar 5,8% masih tergolong kecil dibandingkan total nilai ekspor teripang dunia, kontribusi teripang Indonesia masih tetap signifikan.



    Sumber:
    1. Data Ekspor Impor Nasional - BPS
    2. List of Importing Markets for A Product Exported by Indonesia: 160561 Sea Cucumbers, Prepared or Preserved (excl. Smoked) - ITC
    3. List of Importers for The Selected Product: 160561 Sea Cucumbers, Prepared or Preserved (excl. Smoked) - ITC
    """

    # Menampilkan paragraf4 di Streamlit
    with st.expander("Penjelasan kinerja ekspor teripang:"):
        st.markdown(f'<p style="font-family: Arial; font-size: 16px;">{paragraf5}', unsafe_allow_html=True)

with tab4:
    st.header("Kesimpulan dan Rekomendasi")
    # Paragraf Kesimpulan yang ingin ditampilkan
    paragraf6 = """
    Indonesia memiliki potensi ekspor teripang yang besar.
    Hal ini ditunjukkan dengan besarnya laju pertumbuhan nilai ekspor yang sangat besar hingga 274% untuk nilai ekspor dan laju pertumbuhan volume ekspor hingga 392% sepanjang tahun 2014-2022.
    Namun, dalam pangsa pasar relatif, Indonesia hanya menyumbang 5,8% dari total nilai ekspor teripang dunia.
    Harga rata-rata teripang meningkat setiap tahunnya, sedangkan volume produksi teripang mengalami penurunan.
    Produksi teripang yang hanya berasal dari penangkapan di laut menyebabkan ketidakstabilan produksi.
    Oleh karena itu, pengelolaan yang lebih baik diperlukan untuk melestarikan dan memastikan keberlanjutan sumber daya teripang.
    """

    # Menampilkan paragraf4 di Streamlit
    st.markdown(f'<p style="font-family: Arial; font-size: 16px;">{paragraf6}</p>', unsafe_allow_html=True)



# Buat daftar pustaka
pustaka = [
    "1. Badan Pusat Statistik (BPS). 2023. Data ekspor impor nasional. https://www.bps.go.id/id/exim, 19 Februari 2024, pk. 12:32.",
    "2. International Trade Center (ITC). 2023. List of importing markets for a product exported by Indonesia: 160561 sea cucumbers, prepared or preserved (excl. smoked). https://www.trademap.org/Country_SelProductCountry_TS.aspx?nvpm=1%7c360%7c%7c%7c%7c160561%7c%7c%7c6%7c1%7c1%7c2%7c2%7c1%7c2%7c1%7c%7c1, 19 Februari 2024, pk. 16:25.",
    "3. International Trade Center (ITC). 2023. List of importers for the selected product: 160561 sea cucumbers, prepared or preserved (excl. smoked). https://www.trademap.org/Country_SelProduct_TS.aspx?nvpm=1%7c%7c%7c%7c%7c160561%7c%7c%7c6%7c1%7c1%7c1%7c2%7c1%7c2%7c1%7c%7c1, 22 Februari 2024, pk. 22:57.",
    "4. Setyastuti, A., I. Wirawati, S. Permadi, & I.B. Vimono. 2019. Teripang Indonesia: jenis, sebaran, dan status nilai ekonomi. PT. Media Sains Nasional, Jakarta: 75 hlm.",
    "5. Statistik – Kementerian Kelautan dan Perikanan (KKP). 2023. Produksi perikanan tangkap laut. https://statistik.kkp.go.id/home.php?m=prod_ikan_laut_kab#panel-footer, 8 Februari 2024, pk. 00:41.",
    "6. Tim Badan Riset Sumber Daya Manusia Kelautan dan Perikanan (BRSDMKP). Aspek biologi dan budidaya teripang pasir. AMAFRAD Press Badan Riset dan Sumber Daya Manusia Kelautan dan Perikanan, Jakarta: 159 hlm."
]

# Tampilkan daftar pustaka di dalam spoiler
with st.expander("Daftar Pustaka"):
    for item in pustaka:
        st.markdown(item)



# Alamat email dan website Anda
email_address = "novalia.nikita@gmail.com"
website_address = "https://github.com/novalia-nikita"

# Path ke gambar logo Gmail dan website
logo_gmail_path = "gmail_logo.jpg"
logo_website_path = "github_logo.jpg"

# Membaca gambar dan mengonversi ke format base64
logo_gmail_base64 = base64.b64encode(open(logo_gmail_path, "rb").read()).decode()
logo_website_base64 = base64.b64encode(open(logo_website_path, "rb").read()).decode()

# # Menampilkan gambar di dalam expander dengan HTML
# with st.expander("Kontak penulis:", expanded=True):
#     st.write(
#         f'''
#         <div style="display: flex; align-items: center;">
#             <a href="mailto:{email_address}" target="_blank">
#                 <img src="data:image/jpg;base64,{logo_gmail_base64}" alt="Gmail Logo" style="width:35px;height:35px;margin-right:3mm;">
#             </a>
#             <a href="{website_address}" target="_blank">
#                 <img src="data:image/jpg;base64,{logo_website_base64}" alt="Website Logo" style="width:35px;height:35px;">
#             </a>
#         </div>
#         ''',
#         unsafe_allow_html=True
#     )

# Menampilkan gambar dan teks dengan st.write dan CSS
with st.expander("Kontak penulis:", expanded=True):
    # Menampilkan logo Gmail dengan link dan teks di sampingnya
    st.write(
        f'<div style="display: flex; align-items: center;">'
        f'<a href="mailto:{email_address}" target="_blank">'
        f'<img src="data:image/jpg;base64,{logo_gmail_base64}" alt="Gmail Logo" style="width:35px;height:35px;"></a>'
        f'<p style="text-align:left; margin-left:3mm;">{email_address}</p>'
        f'</div>',
        unsafe_allow_html=True
    )

    # Menampilkan logo website dengan link dan teks di sampingnya
    st.write(
        f'<div style="display: flex; align-items: center;">'
        f'<a href="{website_address}" target="_blank">'
        f'<img src="data:image/jpg;base64,{logo_website_base64}" alt="Website Logo" style="width:35px;height:35px;"></a>'
        f'<p style="text-align:left; margin-left:3mm;">GitHub</p>'
        f'</div>',
        unsafe_allow_html=True
    )