
import streamlit as st

# تعريف الترجمات
translations = {
    "ar": {
        "title": "ستايل بوت - لها",
        "subtitle": "احصلي على توصيات لبسك المثالي",
        "skin_color": "لون البشرة:",
        "height": "الطول:",
        "body_shape": "شكل الجسم:",
        "occasion": "المناسبة:",
        "button": "احصلي على توصيتك",
        "recommendation_title": "✨ توصيتك:"
    },
    "en": {
        "title": "StyleBot Her",
        "subtitle": "Get your perfect outfit recommendation",
        "skin_color": "Skin Color:",
        "height": "Height:",
        "body_shape": "Body Shape:",
        "occasion": "Occasion:",
        "button": "Get Your Recommendation",
        "recommendation_title": "✨ Your Recommendation:"
    }
}

# واجهة اختيار اللغة
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

if st.button(t["button"]):
    # تستبدل الكود اللي يولد التوصية حسب النموذج اللي تستخدمه
    st.success(t["recommendation_title"])
    st.write("هنا تطلع التوصية تلقائيًا حسب مدخلاتك")
