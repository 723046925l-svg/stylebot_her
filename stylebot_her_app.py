
import streamlit as st
from translators import translations  # لو سميت الملف translations.py

# اختيارات اللغة
lang = st.sidebar.selectbox("اختر اللغة / Choose Language", ("العربية", "English"))

if lang == "العربية":
    t = translations["ar"]
else:
    t = translations["en"]

st.set_page_config(page_title=t["title"], page_icon="👗")
st.title(t["title"])
st.markdown(t["subtitle"])

ألوان_البشرة = ['فاتح', 'قمحي', 'حنطي', 'غامق']
الأطوال = ['أقل من 150 سم', '150 - 165 سم', 'أطول من 165 سم']
أشكال_الجسم = ['مستطيل', 'كمثرى', 'تفاحة', 'ساعة رملية']
المناسبات = ['سهرة', 'زواج مساء', 'مشوار نهاري', 'العمل']

skin = st.selectbox(t["skin_color"], ألوان_البشرة)
height = st.selectbox(t["height"], الأطوال)
shape = st.selectbox(t["body_shape"], أشكال_الجسم)
occasion = st.selectbox(t["occasion"], المناسبات)

if st.button(t["get_recommendation"]):
    # الجزء اللي يولّد التوصية...
    # بعدين تعرضها بعنوان:
    st.success(t["recommendation_title"])
    # ثم النص الناتج
