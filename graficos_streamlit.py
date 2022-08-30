import streamlit as st
import numpy as np
import plotly.graph_objects as go

t = np.linspace(0, 0.05, 1000)
v = 220 * np.sqrt(2) * np.sin(2 * np.pi * 60 * t)
w = v**2

st.sidebar.title('Menu')
paginaSelecionada = st.sidebar.selectbox('Selecione um gráfico', ['Gráficos 1', 'Gráfico 2'])

if paginaSelecionada == 'Gráficos 1':
    fig1 = go.Figure(data=go.Scatter(x=t, y=v))
    st.markdown("Gráfico da função v(t)")
    st.plotly_chart(fig1)
else:
    fig2 = go.Figure(data=go.Scatter(x=t, y=w))
    st.markdown("Gráfico da função w(t)")
    st.plotly_chart(fig2)
