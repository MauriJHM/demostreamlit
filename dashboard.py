
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard afluencia de clientes - Cafe internet ")

#Vamos a leer los datos
dfCafe = pd.read_excel("datos/resultadoLimpieza.xlsx")

anios = list(set(dfCafe["fechaEntrada"].dt.year))
meses = list(set(dfCafe["fechaEntrada"].dt.month))
# Vamos a usar el sidebar para mostrar los controles que nos sirven para aplicar los filtros
#########################################
#1. Año
#2. Mes


anioSeleccionado = st.sidebar.selectbox('Seleccionar año', anios)
mesSeleccionado = st.sidebar.selectbox('Seleccionar mes', meses) # Esto tiene que estar ordenado en orden de los meses (nombres)

########################################
# Antes de las gráficas mostramos tambien el df ya filtrado
dfFiltradoMesanio = dfCafe[ (dfCafe['fechaEntrada'].dt.month == mesSeleccionado) & (dfCafe['fechaEntrada'].dt.year == anioSeleccionado) ]
dfMes = dfFiltradoMesanio.groupby(pd.Grouper(key="fechaEntrada",freq="1D")).count().reset_index()
dfMes["fechaStr"] = dfMes["fechaEntrada"].astype(str) + " - "
dfMes["Día"] = dfMes["fechaEntrada"].dt.day_name() + " - " + dfMes["fechaStr"]
# En la parte central vamos a mostrar la gráfica comparativa por mes de los dos años


# La gráfica de dias por mes seleccionado
fig = px.bar(dfMes, x='Día', y='horaEntrada', labels={'horaEntrada': 'Número de Clientes'}, title='Número de Clientes por semana')
st.plotly_chart(fig, use_container_width=True)
# prompt: elimina las columnas que tengan valores 0

# Iterate through the loaded dataframes and remove columns with all zeros
for df_name, df in dfs.items():
  # Select only numeric columns for checking
  numeric_cols = df.select_dtypes(include=['number']).columns
  # Identify columns where all values are zero
  cols_to_drop = [col for col in numeric_cols if (df[col] == 0).all()]
  if cols_to_drop:
    st.write(f"Dropping columns with all zeros in {df_name}: {cols_to_drop}")
    dfs[df_name] = df.drop(columns=cols_to_drop)
  else:
    st.write(f"No columns with all zeros found in {df_name}.")

# You might want to re-concatenate the dataframes after dropping columns
# all_data = pd.concat(dfs.values(), ignore_index=True)
# st.write("Combined Data after dropping zero columns:")
# st.dataframe(all_data)
