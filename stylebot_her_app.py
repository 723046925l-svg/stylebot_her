
import streamlit as st
import openai

# إعداد مفتاح OpenAI من Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="ستايل بوت - لها", page_icon="👗")

st.title("👗 ستايل بوت - لها")
st.markdown("**احصلي على توصيات لبسك المثالي باستخدام الذكاء الاصطناعي!**")

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
        prompt = f'''
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
        '''

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "أنتِ خبيرة موضة تقدمين نصائح أنثوية باللغة العربية."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=600
            )

            reply = response['choices'][0]['message']['content']
            st.success("✨ توصيتك الأنيقة:")
            st.write(reply)

        except Exception as e:
            st.error("حدث خطأ أثناء التواصل مع الذكاء الاصطناعي.")
            st.code(str(e))
