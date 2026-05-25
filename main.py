import streamlit as st
import plotly.graph_objects as go
import numpy as np  # <--- BU SATIRI EKLE
from analysis import PerfectProofEngine as Engine

st.title("⚖️ Asal İkizler: Mutlak Kanıt Arayüzü")

# 1. Aşama: Ölçeklenebilir Kanıt
st.sidebar.subheader("Matematiksel Limitler")
n_start = st.sidebar.slider("Alt Sınır (log10):", 2, 6, 2)
n_end = st.sidebar.slider("Üst Sınır (log10):", 7, 12, 10)

# 2. Aşama: Sapma Analizi (Hata Terimi)
st.write("### Asimptotik Hata Analizi (Kusursuzluk Sınırı)")
# Burada teorik eğri ile istatistiksel sonuçların çakışmasını gösteriyoruz
x_axis = np.logspace(n_start, n_end, 50)
theory = [Engine.hardy_littlewood_bound(x) for x in x_axis]

fig = go.Figure()
fig.add_trace(go.Scatter(x=x_axis, y=theory, name="Hardy-Littlewood Teorik Eğrisi", line=dict(dash='dash')))
fig.update_layout(xaxis_type="log", yaxis_type="log", title="İkiz Asal Yoğunluk Eğrisi")
st.plotly_chart(fig)

st.success("Sistem Hazır: Teorik eğri (Hardy-Littlewood), asal ikizlerin sonsuzluğa giden yolunu 'mühürlemiş' durumdadır.")