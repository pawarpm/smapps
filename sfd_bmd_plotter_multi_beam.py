#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced SFD and BMD Plotter App with Multiple Beam Types
Created on Fri Jun 6 2025
@author: prashantpawar
"""

import streamlit as st
st.set_page_config(page_title="SFD & BMD Plotter", layout="wide")

import numpy as np
import matplotlib.pyplot as plt

st.title("SFD and BMD for Various Beam Types")

# Sidebar Inputs
st.sidebar.header("Beam Configuration")
beam_type = st.sidebar.selectbox("Select Beam Type", ["Simply Supported", "Cantilever", "Overhanging"])
L = st.sidebar.number_input("Beam Length (m)", min_value=1.0, value=10.0)

st.sidebar.subheader("Loads Configuration")
n_point = st.sidebar.number_input("Number of Point Loads", min_value=0, max_value=5, step=1)
n_udl = st.sidebar.number_input("Number of UDLs", min_value=0, max_value=5, step=1)
n_moment = st.sidebar.number_input("Number of Moments", min_value=0, max_value=5, step=1)

point_loads = []
for i in range(n_point):
    st.sidebar.markdown(f"**Point Load {i+1}**")
    mag = st.sidebar.number_input(f"  Magnitude P{i+1} (kN)", value=10.0, key=f"Pmag{i}")
    pos = st.sidebar.number_input(f"  Position a{i+1} (m)", value=2.0, min_value=0.0, max_value=L, key=f"Ppos{i}")
    point_loads.append((mag, pos))

udl_loads = []
for i in range(n_udl):
    st.sidebar.markdown(f"**UDL {i+1}**")
    mag = st.sidebar.number_input(f"  Magnitude w{i+1} (kN/m)", value=5.0, key=f"Wmag{i}")
    start = st.sidebar.number_input(f"  Start x{i+1} (m)", value=2.0, min_value=0.0, max_value=L, key=f"Wstart{i}")
    end = st.sidebar.number_input(f"  End x{i+1} (m)", value=5.0, min_value=0.0, max_value=L, key=f"Wend{i}")
    udl_loads.append((mag, start, end))

moments = []
for i in range(n_moment):
    st.sidebar.markdown(f"**Moment {i+1}**")
    mag = st.sidebar.number_input(f"  Moment M{i+1} (kNm)", value=10.0, key=f"Mmag{i}")
    pos = st.sidebar.number_input(f"  Position x{i+1} (m)", value=3.0, min_value=0.0, max_value=L, key=f"Mpos{i}")
    moments.append((mag, pos))

x = np.linspace(0, L, 1000)
SF = np.zeros_like(x)
BM = np.zeros_like(x)
RA, RB = 0.0, 0.0

def compute_sfd_bmd():
    global RA, RB
    for i in range(len(x)):
        xi = x[i]
        shear = 0
        moment = 0

        if beam_type == "Simply Supported":
            total_point = sum(p[0] for p in point_loads)
            total_moment = sum(m[0] for m in moments)
            total_udl_force = sum(w[0] * (w[2] - w[1]) for w in udl_loads)
            total_udl_moment = sum(w[0] * (w[2] - w[1]) * ((w[1] + w[2]) / 2) for w in udl_loads)
            R_sum = total_point + total_udl_force
            M_sum = sum(p[0] * (L - p[1]) for p in point_loads) + total_udl_moment + total_moment
            RA = M_sum / L
            RB = R_sum - RA
            shear = RA
            moment = RA * xi

        elif beam_type == "Cantilever":
            shear = 0
            moment = 0

        elif beam_type == "Overhanging":
            total_point = sum(p[0] for p in point_loads)
            total_udl_force = sum(w[0] * (w[2] - w[1]) for w in udl_loads)
            total_udl_moment = sum(w[0] * (w[2] - w[1]) * ((w[1] + w[2]) / 2) for w in udl_loads)
            total_moment = sum(m[0] for m in moments)
            R_sum = total_point + total_udl_force
            M_sum = sum(p[0] * (L - p[1]) for p in point_loads) + total_udl_moment + total_moment
            RA = M_sum / L
            RB = R_sum - RA
            shear = RA
            moment = RA * xi

        for P, a in point_loads:
            if xi >= a:
                shear -= P
                moment -= P * (xi - a)

        for w, a, b in udl_loads:
            if xi >= a:
                x1 = min(xi, b)
                l = x1 - a
                shear -= w * l
                moment -= w * l * (xi - (a + l / 2))

        for M, a in moments:
            if xi >= a:
                moment -= M

        if beam_type == "Cantilever":
            shear *= -1
            moment *= -1

        SF[i] = shear
        BM[i] = moment

compute_sfd_bmd()

fig0, ax0 = plt.subplots()
for P, a in point_loads:
    ax0.arrow(a, 0, 0, -P, head_width=0.1, head_length=0.5, fc='blue', ec='blue')
for w, a, b in udl_loads:
    ax0.plot([a, b], [0, 0], color='green', lw=6)
for M, a in moments:
    ax0.annotate(f'M={M}', (a, 1), color='purple')
ax0.set_xlim(0, L)
ax0.set_ylim(-max([P for P, _ in point_loads]+[w*(b-a) for w,a,b in udl_loads]+[10]), 10)
ax0.set_title("Load Diagram")
ax0.set_xlabel("x (m)")
ax0.set_ylabel("Load")
ax0.grid(True)

fig1, ax1 = plt.subplots()
ax1.plot(x, SF, color='blue')
ax1.axhline(0, color='black', linestyle='--')
ax1.set_title("Shear Force Diagram")
ax1.set_xlabel("x (m)")
ax1.set_ylabel("Shear Force (kN)")
ax1.grid(True)

fig2, ax2 = plt.subplots()
ax2.plot(x, BM, color='red')
ax2.axhline(0, color='black', linestyle='--')
ax2.set_title("Bending Moment Diagram")
ax2.set_xlabel("x (m)")
ax2.set_ylabel("Bending Moment (kNm)")
ax2.grid(True)

st.subheader("Support Reactions")
if beam_type in ["Simply Supported", "Overhanging"]:
    st.write(f"Reaction at A (RA): {RA:.2f} kN")
    st.write(f"Reaction at B (RB): {RB:.2f} kN")
elif beam_type == "Cantilever":
    st.write("Cantilever Beam: Fixed at one end, reactions are internal.")

st.pyplot(fig0)
st.pyplot(fig1)
st.pyplot(fig2)
