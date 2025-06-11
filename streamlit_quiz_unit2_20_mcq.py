import streamlit as st
import pandas as pd

st.set_page_config(page_title='Structural Mechanics Quiz – Unit 2', layout='wide')

INSTRUCTOR = 'Dr. Prashant Pawar'
INSTITUTE = "Department of Civil Engineering, SVERI's College of Engineering, Pandharpur"

st.title('📘 MCQ Quiz – Structural Mechanics')
st.markdown(f'**Unit 2: Bending and Shear Stresses in Beams**')
st.markdown(f'*Course Instructor: {INSTRUCTOR}*  \n*Institute: {INSTITUTE}*')

quiz = [
  {
    "question": "In simple bending theory, which stress is considered dominant?",
    "options": [
      "Shear stress",
      "Tensile stress",
      "Compressive stress",
      "Normal stress"
    ],
    "answer": "Normal stress",
    "explanation": "Normal stress due to bending is the primary stress in simple bending theory."
  },
  {
    "question": "Which of the following assumptions is made in pure bending?",
    "options": [
      "Plane sections remain plane after bending",
      "Shear deformation is dominant",
      "Material is non-elastic",
      "Strain varies non-linearly"
    ],
    "answer": "Plane sections remain plane after bending",
    "explanation": "Pure bending assumes no distortion of cross-sections\u2014plane sections remain plane."
  },
  {
    "question": "Flexure formula relates bending stress with:",
    "options": [
      "Axial force",
      "Shear force",
      "Moment of inertia",
      "Torque"
    ],
    "answer": "Moment of inertia",
    "explanation": "Flexural stress is proportional to the bending moment and inversely to moment of inertia."
  },
  {
    "question": "Maximum bending stress in a rectangular beam occurs at:",
    "options": [
      "Neutral axis",
      "Top fiber",
      "Bottom fiber",
      "Extreme fibers"
    ],
    "answer": "Extreme fibers",
    "explanation": "Bending stress varies linearly and is maximum at top and bottom (extreme fibers)."
  },
  {
    "question": "What is the unit of bending stress?",
    "options": [
      "kNm",
      "N",
      "N/m",
      "N/m\u00b2"
    ],
    "answer": "N/m\u00b2",
    "explanation": "Stress is force per unit area (N/m\u00b2 or Pascal)."
  },
  {
    "question": "The shear stress distribution across a rectangular section is:",
    "options": [
      "Linear",
      "Parabolic",
      "Uniform",
      "Exponential"
    ],
    "answer": "Parabolic",
    "explanation": "Shear stress follows a parabolic curve with max at neutral axis."
  },
  {
    "question": "What is the shear stress at the extreme fibers of a rectangular section?",
    "options": [
      "Maximum",
      "Zero",
      "Average",
      "Half of max"
    ],
    "answer": "Zero",
    "explanation": "At the top and bottom of the beam, shear stress is zero."
  },
  {
    "question": "Which formula gives maximum shear stress in a rectangular section?",
    "options": [
      "V/A",
      "1.5 V/A",
      "2 V/A",
      "V/(bd)"
    ],
    "answer": "1.5 V/A",
    "explanation": "Maximum shear stress in rectangular beam is 1.5 times average."
  },
  {
    "question": "What is the location of the neutral axis in a symmetric beam cross-section?",
    "options": [
      "Top fiber",
      "Bottom fiber",
      "Centroidal axis",
      "Varies"
    ],
    "answer": "Centroidal axis",
    "explanation": "For symmetric cross-sections, NA lies at the centroid."
  },
  {
    "question": "Which term in the flexural formula \u03c3 = My/I represents bending moment?",
    "options": [
      "\u03c3",
      "M",
      "y",
      "I"
    ],
    "answer": "M",
    "explanation": "M is the applied bending moment in the flexure formula."
  },
  {
    "question": "In flexural formula, 'y' denotes:",
    "options": [
      "Bending moment",
      "Stress",
      "Distance from NA",
      "Shear force"
    ],
    "answer": "Distance from NA",
    "explanation": "\u2018y\u2019 is the distance from neutral axis to the fiber where stress is calculated."
  },
  {
    "question": "Which of these materials is best suited for resisting bending stress?",
    "options": [
      "Cast Iron",
      "Timber",
      "Mild Steel",
      "Concrete"
    ],
    "answer": "Mild Steel",
    "explanation": "Mild steel has high tensile and compressive strength, suitable for bending."
  },
  {
    "question": "In pure bending, shear force is:",
    "options": [
      "Maximum",
      "Zero",
      "Equal to UDL",
      "Equal to axial force"
    ],
    "answer": "Zero",
    "explanation": "Pure bending is a condition with constant moment and zero shear force."
  },
  {
    "question": "A rectangular beam has width 'b' and depth 'd'. Its section modulus is:",
    "options": [
      "bd\u00b3/12",
      "bd/2",
      "bd\u00b2/6",
      "bd\u00b2/8"
    ],
    "answer": "bd\u00b2/6",
    "explanation": "Section modulus Z = I/y = (bd\u00b3/12) / (d/2) = bd\u00b2/6."
  },
  {
    "question": "What is the significance of the section modulus?",
    "options": [
      "Indicates area",
      "Resists axial force",
      "Represents bending strength",
      "Shows weight"
    ],
    "answer": "Represents bending strength",
    "explanation": "Section modulus indicates the ability of a section to resist bending."
  },
  {
    "question": "If I increases, the bending stress in the beam:",
    "options": [
      "Increases",
      "Decreases",
      "Remains same",
      "Becomes zero"
    ],
    "answer": "Decreases",
    "explanation": "Bending stress is inversely proportional to moment of inertia I."
  },
  {
    "question": "Where is the shear stress maximum in a rectangular section?",
    "options": [
      "Top fiber",
      "Bottom fiber",
      "Neutral axis",
      "Extreme fibers"
    ],
    "answer": "Neutral axis",
    "explanation": "Shear stress is maximum at the neutral axis and zero at extreme fibers."
  },
  {
    "question": "A beam has greater resistance to bending if:",
    "options": [
      "Depth is more",
      "Width is more",
      "Weight is more",
      "Length is more"
    ],
    "answer": "Depth is more",
    "explanation": "Bending resistance increases with depth due to higher I and Z values."
  },
  {
    "question": "If the bending stress exceeds permissible limit, the beam will:",
    "options": [
      "Vibrate",
      "Deflect",
      "Fail in bending",
      "Shrink"
    ],
    "answer": "Fail in bending",
    "explanation": "If bending stress exceeds the material strength, beam will fail in bending."
  },
  {
    "question": "In beam design, why is it better to increase depth than width?",
    "options": [
      "Saves material",
      "Increases Z more effectively",
      "Reduces weight",
      "No reason"
    ],
    "answer": "Increases Z more effectively",
    "explanation": "Increasing depth increases section modulus more effectively, improving bending strength."
  }
]

if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.responses = []

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

if st.session_state.index == len(quiz):
    st.success(f"🎯 Quiz Completed! Your Score: {st.session_state.score} / {len(quiz)}")

    with st.expander("🔍 Review Answers"):
        for i, q in enumerate(quiz):
            user = st.session_state.responses[i]
            correct = q["answer"]
            result = "✅" if user == correct else "❌"
            st.markdown(f"**Q{i+1}: {q['question']}**")
            st.markdown(f"Your Answer: *{user}* {result} — Correct Answer: **{correct}**")
            st.markdown(f"Explanation: {q['explanation']}")
            st.markdown("---")

    df = pd.DataFrame({
        "Question": [q["question"] for q in quiz],
        "Your Answer": st.session_state.responses,
        "Correct Answer": [q["answer"] for q in quiz],
        "Result": ["Correct" if ua == ca else "Incorrect"
                   for ua, ca in zip(st.session_state.responses, [q["answer"] for q in quiz])]
    })

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Your Results as CSV",
        data=csv,
        file_name='structural_mechanics_unit2_20_mcq_results.csv',
        mime='text/csv',
    )

    if st.button("🔁 Restart Quiz"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()