import streamlit as st
import requests

st.title("Login")

email = st.text_input("Email")
password = st.text_input("Senha", type="password")

if st.button("Entrar"):
    response = requests.post(
        "http://localhost:5000/api/login",
        json={"email": email, "password": password}
    )
    if response.status_code == 200:
        user = response.json()
        st.success(f"Bem-vindo, {user['username']}!")
        # Buscar métricas após login
        metrics_response = requests.get(
            "http://localhost:5000/api/metrics",
            params={"role": user["role"]}
        )
        if metrics_response.status_code == 200:
            metrics = metrics_response.json()["metrics"]
            st.write("Métricas:")
            st.dataframe(metrics)
    else:
        st.error("Credenciais inválidas")
