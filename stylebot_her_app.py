
import streamlit as st
from transformers import pipeline

# نحمّل النموذج من Hugging Face
@st.cache_resource
def load_model():
    model_name = "gpt2"  # ممكن تغيّر إلى نموذج يدعم اللغة العربية إذا تلاقيه
    gen = pipeline("text-generation", model=model_name, tokenizer=model_name)
    return gen

generator = load_model()

st.set_page_config(page_title="ستايل بوت - لها", page_icon="👗")
st.title("👗 ستايل بوت - لها")
st.markdown("احصلي على توصيات لبسك المثالي بدون استخدام مفتاح OpenAI")

ألوان_البشرة = ['فاتح', 'قمحي', 'حنطي', 'غامق']
الأطوال = ['أقل من 150 سم', '150 - 165 سم', 'أطول من 165 سم']
أشكال_الجسم = ['مستطيل', 'كمثرى', 'تفاحة', 'ساعة رملية']
المناسبات = ['سهرة', 'زواج مساء', 'مشوار نهاري', 'العمل']

لون_البشرة = st.selectbox("🌸 لون البشرة:", ألوان_البشرة)
الطول = st.selectbox("📏 الطول:", الأطوال)
شكل_الجسم = st.selectbox("👗 شكل الجسم:", أشكال_الجسم)
المناسبة = st.selectbox("🎉 نوع المناسبة:", المناسبات)

if st.button("احصلي على توصيتك"):
    with st.spinner("جاري التفكّر... 💭"):
        prompt = (
            f"لون البشرة: {لون_البشرة}. الطول: {الطول}. شكل الجسم: {شكل_الجسم}. المناسبة: {المناسبة}. "
            "اقترح لي لبس مناسب، الألوان المناسبة، تسريحة شعر، وأكسسوارات بأسلوب أنثوي."
        )
        try:
            result = generator(prompt, max_length=200)
            reply = result[0]['generated_text']
            st.success("✨ توصيتك الأنيقة:")
            st.write(reply)
        except Exception as e:
            st.error("حدث خطأ أثناء توليد التوصية.")
            st.write(str(e))
