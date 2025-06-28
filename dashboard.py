import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Dashboard Penerimaan Universitas",
    page_icon="🎓",
    layout="wide"
)

st.title("Dashboard Analisis Penerimaan Mahasiswa Yale Univeristy")
st.markdown("Dashboard ini menganalisis data tren penerimaan tahunan berdasarkan dataset admisi mahasiswa Yale University.")


@st.cache_data
def load_data(file_path):
    """Memuat data dari file CSV dan melakukan prapemprosesan sederhana."""
    df = pd.read_csv(file_path)
    return df


try:
    df = load_data("YaleAdmits.csv")
except FileNotFoundError:
    st.error("File 'YaleAdmits.csv' tidak ditemukan. Pastikan file berada di direktori yang sama dengan aplikasi ini.")
    st.stop()


st.sidebar.header("⚙️ Filter Data")

min_year = int(df['Year Entered'].min())
max_year = int(df['Year Entered'].max())

select_year_range = st.sidebar.slider(
    'Pilih Rentang Tahun:',
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year) 
)

filtered_df = df[
    (df['Year Entered'] >= select_year_range[0]) &
    (df['Year Entered'] <= select_year_range[1])
]

st.header(f"Ringkasan Metrik Utama ({select_year_range[0]} - {select_year_range[1]})")

total_applications = filtered_df['Applications'].sum()
total_admits = filtered_df['Admits'].sum()
avg_admit_rate = filtered_df['AdmitRate'].mean() * 100
avg_yield = filtered_df['Yield'].mean() * 100

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Aplikasi", f"{total_applications:,}")
col2.metric("Total Diterima", f"{total_admits:,}")
col3.metric("Rata-rata Tingkat Penerimaan", f"{avg_admit_rate:.2f}%")
col4.metric("Rata-rata Yield", f"{avg_yield:.2f}%")

st.markdown("---")

st.header("Visualisasi Tren Tahunan")

line_total_admisi, bar_tingat_penerimaan = st.columns(2)

with line_total_admisi:

    st.subheader("Tren Jumlah Aplikasi dan Penerimaan")
    if not filtered_df.empty:
        fig_line = px.line(
            filtered_df,
            x='Year Entered',
            y=['Applications', 'Admits'],
            title='Jumlah Aplikasi vs. Diterima per Tahun',
            labels={'value': 'Jumlah', 'Tahun': 'Year Entered', 'variable': 'Kategori'},
            markers=True
        )
        st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.warning("Tidak ada data untuk ditampilkan dengan filter yang dipilih.")

with bar_tingat_penerimaan:
    st.subheader("Tingkat Penerimaan  per Tahun")
    if not filtered_df.empty:
        fig_bar = px.bar(
            filtered_df,
            x='Year Entered',
            y='AdmitRate',
            title='Perkembangan Tingkat Penerimaan',
            labels={'AdmitRate': 'Tingkat Penerimaan', 'Tahun': 'Year Entered'}
        )
        fig_bar.update_layout(yaxis_tickformat='.0%')
        st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.warning("Tidak ada data untuk ditampilkan dengan filter yang dipilih.")


st.header("Analisis Skor Akademik")
st.subheader("Tren Median Skor SAT (Verbal + Math)")

if not filtered_df.empty:
    fig_sat = px.line(
        filtered_df,
        x='Year Entered',
        y='SAT50',
        title='Perkembangan Median Skor SAT Pendaftar per Tahun',
        labels={'SAT50': 'Median Skor SAT (SAT50)', 'Tahun': 'Year Entered'},
        markers=True
    )
    st.plotly_chart(fig_sat, use_container_width=True)
else:
    st.warning("Tidak ada data untuk ditampilkan.")

st.subheader("Rata-rata Skor SAT Berdasarkan Persentil")
if not filtered_df.empty:
    verbal_cols = ['Verbal10th', 'Verbal25th', 'Verbal50th', 'Verbal75th', 'Verbal90th']
    math_cols = ['Math10th', 'Math25th', 'Math50th', 'Math75th', 'Math90th']
    percentiles = [10, 25, 50, 75, 90]

    avg_verbal_scores = filtered_df[verbal_cols].mean().values
    avg_math_scores = filtered_df[math_cols].mean().values

    plot_data = []
    for i, p in enumerate(percentiles):
        plot_data.append({'Persentil': p, 'Skor Rata-rata verbal': avg_verbal_scores[i], 'Skor Rata-rata math': avg_math_scores[i]})

    percentile_df = pd.DataFrame(plot_data)
    if st.checkbox("Tampilkan Data Mentah per Persentil"):
        st.subheader("Data Rata-rata Skor SAT per Persentil")
        st.dataframe(percentile_df)

    fig = px.line(percentile_df, x='Persentil', y=['Skor Rata-rata verbal', 'Skor Rata-rata math'], markers=True)
    fig.update_layout(yaxis_title='Skor')
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Tidak ada data untuk ditampilkan.")

if st.checkbox("Tampilkan Data Mentah"):
    st.subheader("Data Agregat Tahunan")
    st.dataframe(filtered_df)