#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 09:27:37 2025

@author: prashantpawar
"""

import streamlit as st
st.set_page_config(page_title="Flexural Stress Analyzer", layout="centered")

import numpy as np
import matplotlib.pyplot as plt

st.title("Flexural Stress Distribution with Safety Check")

# Section type selection
section_type = st.sidebar.selectbox("Select Section Shape", ["Rectangular", "Circular"])

# Bending moment input
M_kNm = st.sidebar.number_input("Bending Moment M (kNm)", min_value=0.0, value=20.0)
M = M_kNm * 1e6  # Convert to Nmm

# Material property
fy = st.sidebar.number_input("Yield Stress of Material (N/mm²)", min_value=1.0, value=250.0)

# Section properties
if section_type == "Rectangular":
    st.sidebar.markdown("### Rectangular Section")
    b = st.sidebar.number_input("Width b (mm)", min_value=1.0, value=300.0)
    d = st.sidebar.number_input("Depth d (mm)", min_value=1.0, value=500.0)
    I = (b * d**3) / 12
    y = np.linspace(-d/2, d/2, 500)
    ymax = d/2

elif section_type == "Circular":
    st.sidebar.markdown("### Circular Section")
    D = st.sidebar.number_input("Diameter D (mm)", min_value=1.0, value=400.0)
    I = (np.pi * D**4) / 64
    y = np.linspace(-D/2, D/2, 500)
    ymax = D/2

# Stress distribution using flexure formula
sigma = (M * y) / I

# Safety check
sigma_max = np.max(np.abs(sigma))
is_safe = sigma_max <= fy
safety_message = "✅ Safe under given bending moment" if is_safe else "❌ NOT SAFE: Stress exceeds yield strength"

# Plotting
fig, ax = plt.subplots()
ax.plot(sigma, y, label="σ = My/I")
ax.axhline(0, color='black', linestyle='--')
ax.axvline(0, color='black', linestyle='--')

# Annotate extreme values
ax.plot([np.min(sigma)], [y[0]], 'ro')
ax.plot([np.max(sigma)], [y[-1]], 'go')
ax.annotate(f'{np.min(sigma):.2f} N/mm² (Top)', (np.min(sigma), y[0]), textcoords="offset points", xytext=(-50,10), ha='right', color='red')
ax.annotate(f'{np.max(sigma):.2f} N/mm² (Bottom)', (np.max(sigma), y[-1]), textcoords="offset points", xytext=(10,-15), ha='left', color='green')

ax.set_xlabel("Bending Stress σ (N/mm²)")
ax.set_ylabel("y (mm) from Neutral Axis")
ax.set_title(f"Stress Distribution - {section_type} Section")
ax.grid(True)
ax.legend()

# Display outputs
st.subheader("Results")
st.write(f"Moment of Inertia (I): **{I:,.2f} mm⁴**")
st.write(f"Maximum Bending Stress: **{sigma_max:.2f} N/mm²**")
st.write(f"Yield Stress: **{fy:.2f} N/mm²**")
st.markdown(f"### Safety Check: {safety_message}")

# Show plot
st.pyplot(fig)
