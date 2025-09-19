
from transformers import pipeline

# تحميل النموذج
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')

def get_recommendation(prompt):
    result = generator(prompt, max_length=200)
    return result[0]['generated_text']

# في مكان ما في تطبيقك Streamlit:
prompt = f"""
بناءً على المعلومات التالية:
- لون البشرة: {لون_البشرة}
- الطول: {الطول}
- شكل الجسم: {شكل_الجسم}
- نوع المناسبة: {المناسبة}

اقترح لوك كامل يشمل:
- نوع اللبس المناسب
- الألوان المثالية
- تسريحة شعر
- أكسسوارات مقترحة

بأسلوب أنثوي ناعم وباللغة العربية.
"""

reply = get_recommendation(prompt)
st.write(reply)
إذا تحب، أجهز لك الكود الكامل لتطبيقك باستخدام Hugging Face بدل OpenAI وبصيغة “ما يحتاج تسجيل مفتاح”، وأرسللك المشروع جاهز؟ هل تريد هيچ؟






Sources
You said:
يله جهزلي وخبرني شنو اسوي لحد مايكمل التطبيق 

ChatGPT said:
زين يا علي، لقيت لك بديل من Hugging Face يستخدم نموذج عربي، ونقدر ندمجه بدال OpenAI حتى يصير المشروع ما يحتاج تسجيل مفتاح OpenAI.

راح أشرحلك النموذج وأعطيك كود كامل لتطبيقك يستخدم هذا النموذج.

🔍 البديل اللي نستخدمه
مثلاً النموذج Hezam/ArabicT5-news-classification-generation يستخدم لتحويل نص عربي إلى نص آخر، ممكن نستغلّه لتوليد التوصيات. 
Hugging Face

⚙️ الكود المعدّل لاستخدام Hugging Face بدال OpenAI
هذا الكود تكتبه داخل stylebot_her_app.py أو ملف تطبيقك:

python
Copy code
import streamlit as st
from transformers import pipeline

# تحميل النموذج من Hugging Face
@st.cache_resource
def load_model():
    # النموذج اللي اخترناه
    model_name = "Hezam/ArabicT5-news-classification-generation"
    gen = pipeline("text2text-generation", model=model_name, tokenizer=model_name)
    return gen

generator = load_model()

# عنوان التطبيق
st.set_page_config(page_title="ستايل بوت - لها", page_icon="👗")
st.title("👗 ستايل بوت - لها")
st.markdown("**احصلي على توصيات لبسك المثالي باستخدام الذكاء الاصطناعي البديل**")

# اختيارات المستخدم
ألوان_البشرة = ['فاتح', 'قمحي', 'حنطي', 'غامق']
الأطوال = ['أقل من 150 سم', '150 - 165 سم', 'أطول من 165 سم']
أشكال_الجسم = ['مستطيل', 'كمثرى', 'تفاحة', 'ساعة رملية']
المناسبات = ['سهرة', 'زواج مساء', 'مشوار نهاري', 'العمل']

لون_البشرة = st.selectbox("🌸 لون البشرة:", ألوان_البشرة)
الطول = st.selectbox("📏 الطول:", الأطوال)
شكل_الجسم = st.selectbox("👗 شكل الجسم:", أشكال_الجسم)
المناسبة = st.selectbox("🎉 نوع المناسبة:", المناسبات)

if st.button("احصلي على توصيتك"):
    with st.spinner("جاري التفكير... 💭"):
        prompt = (
            f"لون البشرة: {لون_البشرة}, الطول: {الطول}, شكل الجسم: {شكل_الجسم}, "
            f"المناسبة: {المناسبة}. "
            "اقترح لي لبس مناسب، الألوان، تسريحة شعر، أكسسوارات، بطريقة أنثوية."
        )

        try:
            result = generator(prompt, max_length=200)
            # الناتج كنص
            reply = result[0]['generated_text']
            st.success("✨ توصيتك الأنيقة:")
            st.write(reply)
        except Exception as e:
            st.error("حدث خطأ أثناء توليد التوصية:")
            st.write(str(e))
