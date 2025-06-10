import streamlit as st
import pandas as pd

# App config
st.set_page_config(page_title="Structural Mechanics Quiz – Unit 1", layout="wide")

# Instructor & Institute info
INSTRUCTOR = "Dr. Prashant Pawar"
INSTITUTE = "Department of Civil Engineering, SVERI's College of Engineering, Pandharpur"

st.title("📘 MCQ Quiz – Structural Mechanics")
st.markdown(f"**Unit 1: Analysis of Statically Determinate Beams**")
st.markdown(f"*Course Instructor: {INSTRUCTOR}*  \n*Institute: {INSTITUTE}*")

# Quiz with explanations
quiz = [
    {"question": "What is the shape of the shear force diagram under a single point load?",
     "options": ["Parabolic", "Constant", "Linear", "Exponential"], "answer": "Linear",
     "explanation": "Shear force under a single point load changes linearly between the load points."},

    {"question": "Where does the maximum bending moment occur in a simply supported beam with a central load?",
     "options": ["At the support", "At midspan", "At quarter span", "Anywhere on the span"], "answer": "At midspan",
     "explanation": "With a central point load, maximum bending moment occurs exactly at the center of the beam."},

    {"question": "Which of the following represents the differential relation for bending moment?",
     "options": ["dM/dx = w", "dM/dx = M", "dM/dx = V", "dM/dx = -V"], "answer": "dM/dx = V",
     "explanation": "The derivative of the bending moment is equal to the shear force at a point: dM/dx = V."},

    {"question": "The shear force variation in a beam subjected to a UDL is:",
     "options": ["Constant", "Linear", "Parabolic", "Cubic"], "answer": "Linear",
     "explanation": "Under UDL, shear force changes linearly along the beam length."},

    {"question": "A UDL over the span of a simply supported beam results in a bending moment diagram that is:",
     "options": ["Linear", "Constant", "Parabolic", "Triangular"], "answer": "Parabolic",
     "explanation": "The bending moment under UDL is a parabolic curve due to integration of linear shear."},

    {"question": "For a cantilever beam with a point load at the free end, the shear force at the fixed end is:",
     "options": ["Zero", "Equal to the load", "Half the load", "Twice the load"], "answer": "Equal to the load",
     "explanation": "The full load is transferred to the fixed end, so SF = Load."},

    {"question": "A uniformly varying load (UVL) produces which type of shear force diagram?",
     "options": ["Constant", "Linear", "Parabolic", "Triangular"], "answer": "Parabolic",
     "explanation": "UVL increases/decreases linearly, and integrating it gives a parabolic SF diagram."},

    {"question": "Which of the following causes a sudden jump in the shear force diagram?",
     "options": ["UDL", "UVL", "Point load", "Moment"], "answer": "Point load",
     "explanation": "A concentrated point load causes a vertical jump in the shear force graph."},

    {"question": "A sudden jump in the bending moment diagram is caused by:",
     "options": ["Point load", "UDL", "UVL", "Couple"], "answer": "Couple",
     "explanation": "A couple introduces a sudden moment, causing a discontinuity (jump) in BM diagram."},

    {"question": "For a simply supported beam with full-span UDL, the maximum bending moment occurs at:",
     "options": ["Quarter span", "Support", "Center", "End"], "answer": "Center",
     "explanation": "The maximum BM occurs at the center of the beam for symmetric UDL loading."},

    {"question": "The slope of the bending moment diagram at a point is equal to:",
     "options": ["Load at that point", "Shear force at that point", "Beam deflection", "Zero"], "answer": "Shear force at that point",
     "explanation": "Slope of BM diagram = Shear force: dM/dx = V."},

    {"question": "Under inclined point loading, S.F. and B.M. analysis should consider:",
     "options": ["Horizontal component", "Vertical component", "Total magnitude", "Axial component"], "answer": "Vertical component",
     "explanation": "Only vertical components contribute to shear and bending moment."},

    {"question": "The rate of change of shear force under UDL is:",
     "options": ["+w", "-w", "Zero", "w²"], "answer": "-w",
     "explanation": "dV/dx = -w (w is the intensity of UDL)."},

    {"question": "The area under the shear force diagram between two sections gives:",
     "options": ["Bending moment", "Deflection", "Load", "Axial force"], "answer": "Bending moment",
     "explanation": "Bending moment is the integral (area under curve) of the shear force diagram."},

    {"question": "A cantilever beam with an applied couple at the free end produces a bending moment diagram that is:",
     "options": ["Linear", "Parabolic", "Constant", "Varying"], "answer": "Constant",
     "explanation": "A couple applied at the free end results in a constant bending moment throughout."},

    {"question": "In a beam subjected to UVL, the shape of the bending moment diagram is:",
     "options": ["Linear", "Parabolic", "Cubic", "Exponential"], "answer": "Cubic",
     "explanation": "BM is integral of SF (which is parabolic under UVL), thus BM is cubic."},

    {"question": "If the shear force at two supports is +20 kN and -20 kN, the net external load on the beam is:",
     "options": ["Zero", "20 kN", "40 kN", "-40 kN"], "answer": "Zero",
     "explanation": "If SF changes from +20 to -20, it indicates a symmetric loading — net external force is zero."},

    {"question": "Which of the following differential equations is correct?",
     "options": ["d²M/dx² = -w", "dM/dx = -w", "dV/dx = M", "dM/dx = w"], "answer": "d²M/dx² = -w",
     "explanation": "The second derivative of BM is related to loading: d²M/dx² = -w."},

    {"question": "Where does the shear force become zero in a simply supported beam with UDL?",
     "options": ["At the start of load", "At the support", "At midspan", "Nowhere"], "answer": "At midspan",
     "explanation": "In UDL on a simply supported beam, SF is zero at the midspan where BM is maximum."},

    {"question": "A clockwise couple at the midspan of a beam results in the shear force diagram:",
     "options": ["Showing sudden drop", "Showing sudden rise", "Remaining unaffected", "Showing linear variation"], "answer": "Remaining unaffected",
     "explanation": "A couple affects the BM diagram, not the shear force diagram."},
]

# Session state
if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.responses = []

# Current question
if st.session_state.index < len(quiz):
    current = quiz[st.session_state.index]
    st.markdown(f"### Q{st.session_state.index + 1}: {current['question']}")
    choice = st.radio("Choose your answer:", current["options"], key=f"q{st.session_state.index}")

    if st.button("Next"):
        st.session_state.responses.append(choice)
        if choice == current["answer"]:
            st.session_state.score += 1
        st.session_state.index += 1
        st.rerun()
      
# After quiz completed
if st.session_state.index == len(quiz):
    st.success(f"🎯 Quiz Completed! Your Score: {st.session_state.score} / {len(quiz)}")

    with st.expander("🔍 Review Answers and Explanations"):
        for i, q in enumerate(quiz):
            user = st.session_state.responses[i]
            correct = q["answer"]
            result = "✅" if user == correct else "❌"
            st.markdown(f"**Q{i+1}: {q['question']}**")
            st.markdown(f"Your Answer: *{user}* {result} — Correct Answer: **{correct}**")
            st.markdown(f"📘 *Explanation:* {q['explanation']}")
            st.markdown("---")

    df = pd.DataFrame({
        "Question": [q["question"] for q in quiz],
        "Your Answer": st.session_state.responses,
        "Correct Answer": [q["answer"] for q in quiz],
        "Result": ["Correct" if ua == ca else "Incorrect"
                   for ua, ca in zip(st.session_state.responses, [q["answer"] for q in quiz])],
        "Explanation": [q["explanation"] for q in quiz],
    })

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Results with Explanations (CSV)",
        data=csv,
        file_name='unit1_structural_mechanics_quiz.csv',
        mime='text/csv',
    )

    if st.button("🔁 Restart Quiz"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
