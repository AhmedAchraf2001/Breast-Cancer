# import streamlit as st
# from PIL import Image, ImageDraw
# import joblib
# def resize_image(image_path, size=(300, 300)):
#     image = Image.open(image_path)
#     return image.resize(size)
# def create_circular_image(image_path, size=(150, 150)):
#     image = Image.open(image_path).convert("RGBA")
#     image = image.resize(size, Image.LANCZOS)
#     mask = Image.new("L", size, 0)
#     draw = ImageDraw.Draw(mask)
#     draw.ellipse((0, 0, size[0], size[1]), fill=255)
#     result = Image.composite(image, Image.new("RGBA", size, (0, 0, 0, 0)), mask)
#     return result

# def create_rounded_image(image_path, size=(300, 300), radius=30):
#     image = Image.open(image_path).convert("RGBA")
#     image = image.resize(size, Image.LANCZOS)
#     mask = Image.new("L", size, 0)
#     draw = ImageDraw.Draw(mask)
#     draw.rounded_rectangle((0, 0, size[0], size[1]), radius=radius, fill=255)
#     result = Image.composite(image, Image.new("RGBA", size, (0, 0, 0, 0)), mask)
#     return result

# def set_page_style():
#     st.markdown("""
#         <style>
#             .stApp {
#                 background-color: #e3f2fd; /* Light blue background */
#                 font-family: 'Segoe UI', sans-serif;
#             }
#             .sidebar .css-1d391kg, .css-1yn4zz9 {
#                 background-color: #e3f2fd;
#                 color: #0d47a1;
#             }
#             .sidebar .stRadio > div > label:hover {
#                 background-color: #1976d2;
#                 cursor: pointer;
#             }
#             h1, h2, h3, p {
#                 color: #0d47a1;
#             }
#             .custom-text {
#                 font-weight: normal;
#             }
#             .caption {
#                 color: black;
#                 font-size: 16px; /* Adjust the size as needed */
#             }
#         </style>
#     """, unsafe_allow_html=True)

# def navigate_to(page):
#     st.session_state.page = page

# def home():
#     st.title("Breast cancer detection")

#     # استخدام الأعمدة لوضع الصورة والنص بجانبها
#     col1, col2 = st.columns([1, 2])  # تحديد العرض النسبي للأعمدة

#     # العمود الأول للصورة
#     with col1:
#         rounded_image = create_rounded_image("5.jpg", size=(700, 700))  # تغيير الحجم للصورة الكبيرة
#         st.image(rounded_image)

#     # العمود الثاني للنص بجانب الصورة
#     with col2:
#         st.markdown("""
#             <p style='text-align: left; color: black; font-size: 24px;'>
#             Breast cancer is one of the most common cancers affecting people globally, 
#             including men. It happens when cells in the breast grow uncontrollably, forming a tumor. 
#             Early detection is crucial for better outcomes. Our model uses advanced techniques to help detect cancer early, 
#             aiming to support better health and outcomes.
#             </p>
#         """, unsafe_allow_html=True)

#     # بقية الكود لعرض باقي الصور
#     image1 = resize_image("1.png", size=(700,700))
#     image2 = resize_image('22.png', size=(700, 700))
#     image3 = resize_image("4.png", size=(700, 700))
#     image4 = resize_image('2.png', size=(700, 700))

#     st.markdown("""
#         <p class='custom-text'>
#          Statistics about the disease: 
#         </p>
#     """, unsafe_allow_html=True)

#     col3, col4 = st.columns(2)
#     with col3:
#         st.image(image1, caption="•  Prevalence: Breast cancer is the most common cancer worldwide, with an estimated 2.3 million new cases reported in 2020", use_column_width=True)
#     with col4:
#         st.image(image2, caption="•  Mortality Rate: It is the second leading cause of cancer-related deaths globally, with approximately 685,000 deaths in 2020.", use_column_width=True)

#     col5, col6 = st.columns(2)
#     with col5:
#         st.image(image3, caption="Genetic Mutations: About 5-10% of breast cancer cases are linked to genetic mutations (e.g., BRCA1 and BRCA2).", use_column_width=True)
#     with col6:
#         st.image(image4, caption="Gender: Women are at a higher risk than men, though men can also develop breast cancer.",
#                 use_column_width=True)

#     # أزرار الانتقال
#     if st.button("Go to Test"):
#         navigate_to("Test")
#     if st.button("Go to Meet the team"):
#         navigate_to("About")




# def test():
#     model = joblib.load('model.pkl')



#     st.markdown("""
#     <style>
#     .custom-title {
#         font-size: 40px;
#         font-weight: bold;
#         text-align: center;
#         color: #4CAF50;
#     }
#     </style>
#     <p class='custom-title'>Breast Cancer Prediction</p>
#     """, unsafe_allow_html=True)


#     radius_mean = st.slider('Radius Mean:', min_value=5.0, max_value=30.0, step=0.1)
#     texture_mean = st.slider('Texture Mean:', min_value=10.0, max_value=40.0, step=0.1)
#     smoothness_mean = st.slider('Smoothness Mean:', min_value=0.05, max_value=0.2, step=0.01)
#     compactness_mean = st.slider('Compactness Mean:', min_value=0.05, max_value=0.3, step=0.01)
#     symmetry_mean = st.slider('Symmetry Mean:', min_value=0.1, max_value=0.3, step=0.01)
#     fractal_dimension_mean = st.slider('Fractal Dimension Mean:', min_value=0.05, max_value=0.1, step=0.001)
#     radius_se = st.slider('Radius SE:', min_value=0.2, max_value=1.5, step=0.1)
#     texture_se = st.slider('Texture SE:', min_value=0.5, max_value=3.0, step=0.1)
#     smoothness_se = st.slider('Smoothness SE:', min_value=0.001, max_value=0.01, step=0.001)
#     compactness_se = st.slider('Compactness SE:', min_value=0.01, max_value=0.05, step=0.001)
#     symmetry_se = st.slider('Symmetry SE:', min_value=0.01, max_value=0.05, step=0.001)
#     fractal_dimension_se = st.slider('Fractal Dimension SE:', min_value=0.001, max_value=0.01, step=0.001)

#     if st.button('Predict'):

#         user_data = [[radius_mean, texture_mean, smoothness_mean, compactness_mean,
#                       symmetry_mean, fractal_dimension_mean, radius_se, texture_se, 
#                       smoothness_se, compactness_se, symmetry_se, fractal_dimension_se]]

#         prediction = model.predict(user_data)

#         if prediction[0] == 1:
#             st.success('The model predicts the tumor is Malignant.')
#         else:
#             st.success('The model predicts the tumor is Benign.')









#     # st.markdown("<p class='custom-text'>Test different features here.</p>", unsafe_allow_html = True)


#     model = joblib.load('model.pkl')
#     if st.button("Go to Home"):
#         navigate_to("Home")



# def about():
#     st.title("Meet the team")
#     st.markdown("<p class='custom-text'>Website developers</p>", unsafe_allow_html=True)
#     people = [
#         {"image": "2.jpg", "name": "Mostafa Arafat", "description": "Team member"},
#         {"image": "1.jpg", "name": "Mostafa Ibrahim", "description": "Team member"},
#         {"image": "WhatsApp Image 2024-09-11 at 18.26.48_6dfb3807.jpg", "name": "Rofaida Abdelaleem", "description": "Team member"},
#         {"image": "WhatsApp Image 2024-09-11 at 22.55.17_1251f220.jpg", "name": "Basant Fathi", "description": "Team member"}
#     ]
#     for person in people:
#         st.image(create_circular_image(person["image"]), caption=f"Photo of {person['name']}", width=150)
#         st.markdown(f"<p class='custom-text'>{person['name']} - {person['description']}</p>", unsafe_allow_html=True)
#         st.markdown("<hr>", unsafe_allow_html=True)
#     if st.button("Go to Home"):
#         navigate_to("Home")

# def main():
#     set_page_style()
#     if 'page' not in st.session_state:
#         st.session_state.page = "Home"
#     st.sidebar.title("Navigation")
#     selected_page = st.sidebar.radio("Menu:", ["Home", "Test", "About"], index=["Home", "Test", "About"].index(st.session_state.page))
#     navigate_to(selected_page)
#     if st.session_state.page == "Home":
#         home()
#     elif st.session_state.page == "Test":
#         test()
#     elif st.session_state.page == "About":
#         about()

# if __name__ == "__main__":
#     st.set_page_config(page_title="Hypersonix", layout="wide")
#     main()