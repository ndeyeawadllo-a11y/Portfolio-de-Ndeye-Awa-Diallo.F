import streamlit as st

st.set_page_config(page_title="Portfolio - Ndeye Awa Diallo", page_icon="🌿", layout="wide")

with st.sidebar:

    st.subheader("Ndeye Awa Diallo")
    st.write("*Sciences Alimentaires & Nutrition*")
    st.write("---")

    st.write("**Mes coordonnées**")
    st.write("✉️ diallo.awa@uam.edu.sn")
    st.write("📍 Dakar, Sénégal")
    st.write("🎓 Université Amadou Mahtar Mbow")

st.title("Bonjour, je suis Ndeye Awa Diallo")
st.subheader("Étudiante en Sciences Alimentaires & Nutrition")
st.write("""
Je suis en deuxième année d'agronomie à l'Université Amadou Mahtar Mbow de Dakar.
Je suis motivée, rigoureuse et passionnée par tout ce qui touche à l'alimentation
et à la nutrition. Je recherche actuellement un stage dans l'industrie agroalimentaire
pour mettre en pratique mes connaissances.
""")


st.title("À propos de moi")
st.write("""
Passionnée par les sciences alimentaires et la nutrition, je suis actuellement
en deuxième année à l'Université Amadou Mahtar Mbow de Dakar. Mon objectif est
de contribuer à une alimentation plus saine et plus sûre pour les populations.

Mon récent stage chez Le Lionceau m'a permis de découvrir concrètement le monde
de la production agroalimentaire. Je souhaite continuer à apprendre sur le terrain
en réalisant un nouveau stage.
""")

st.subheader("Mes valeurs")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("**Rigueur**")
    st.write("Précision et méthode dans le travail de laboratoire.")
with col2:
    st.write("**Curiosité**")
    st.write("Toujours envie d'apprendre et de découvrir.")
with col3:
    st.write("**Esprit d'équipe**")
    st.write("J'aime collaborer et travailler en groupe.")


st.title("Ma formation")

st.subheader("2024 - 2027 : Licence")
st.write("Sciences Agricoles, spécialité Sciences Alimentaires et Nutrition")
st.write("*Université Amadou Mahtar Mbow, Dakar*")

st.write("")

st.subheader("2023 - 2024 : Baccalauréat scientifique")


st.title("Mon expérience")

st.subheader("Stagiaire - Production, Qualité & Marketing")
st.write("**Le Lionceau** - Dakar, Sénégal")
st.write("*Du 1er septembre au 10 octobre 2025*")
st.write("""
- Participation aux processus de production alimentaire
- Suivi de la qualité des produits en cours de fabrication
- Respect des normes d'hygiène et de sécurité alimentaire
- Participation à l'emballage et à l'étiquetage des produits
- Contribution aux activités de marketing (promotion, communication)
- Travail en équipe
""")

st.write("---")
st.subheader("Bénévole - Distribution alimentaire (Ramadan)")
st.write("**LTSNT** - Dakar, Sénégal")
st.write("*Depuis 2022*")
st.write("""
- Distribution de repas pendant le Ramadan
- Aide à l'organisation et à la préparation des repas
- Travail en équipe au service de la communauté
- Assistance dans la logistique
""")


st.title("Mes compétences")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Compétences techniques")
    st.write("Microbiologie et biologie cellulaire")
    st.progress(80, text="80%")
    st.write("Culture stérile et microscopie")
    st.progress(75, text="75%")
    st.write("Dosage acido-basique")
    st.progress(80, text="80%")
    st.write("Manipulation d'équipements de laboratoire")
    st.progress(85, text="85%")
    st.write("Analyses chimiques")
    st.progress(70, text="70%")

with col2:
    st.subheader("Compétences comportementales")
    st.write("- Travail en équipe")
    st.write("- Adaptabilité")
    st.write("- Sens du détail")
    st.write("- Intelligence émotionnelle")
    st.write("- Proactivité")
    st.write("- Esprit d'initiative")


st.title("Mes projets")

st.subheader("Portfolio web personnel")
st.write("*Streamlit - Python - 2026*")
st.write("""
Réalisation de ce site portfolio pour présenter mon parcours et mes compétences
aux recruteurs. Application multi-pages avec Streamlit.
""")
st.write("---")

st.subheader("TP Microbiologie alimentaire")
st.write("*Travaux pratiques - UAM - 2025*")
st.write("""
Identification et dénombrement de micro-organismes dans des échantillons
alimentaires : préparation de milieux de culture, ensemencement, observation
au microscope.
""")
st.write("---")

st.subheader("Analyse nutritionnelle")
st.write("*Travaux pratiques - UAM - 2025*")
st.write("""
Étude de la composition nutritionnelle de produits locaux : dosage des
protéines, glucides et lipides, et comparaison aux apports recommandés.
""")
