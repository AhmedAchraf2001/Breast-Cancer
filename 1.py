import streamlit as st
from PIL import Image, ImageDraw
import joblib
import numpy as np
import base64
def resize_image(image_path, size=(300, 300)):
    image = Image.open(image_path)
    return image.resize(size)
def create_circular_image(image_path, size=(100, 100)):
    image = Image.open(image_path).convert("RGBA")
    image = image.resize(size, Image.LANCZOS)
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size[0], size[1]), fill=255)
    result = Image.composite(image, Image.new("RGBA", size, (0, 0, 0, 0)), mask)
    return result
def create_rounded_image(image_path, size=(600, 400), radius=30):
    image = Image.open(image_path).convert("RGBA")
    image = image.resize(size, Image.LANCZOS)
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, size[0], size[1]), radius=radius, fill=255)
    result = Image.composite(image, Image.new("RGBA", size, (0, 0, 0, 0)), mask)
    return result
def set_page_style():
    st.markdown("""
        <style>
            .sidebar{
                background-color: #FF8DA1;
                }
            .stApp {
                background-color: #ffebf3;
                font-family: 'Segoe UI', sans-serif;
            }
            .sidebar .css-1d391kg, .css-1yn4zz9 {
                background-color: #e3f2fd;
                color: #0d47a1;
            }
            .stRadio > div > label:hover {
                background-color: #ffebf3;
                cursor: pointer;
            }
            h1, h2, h3, p {
                color: #0d47a1;
            }
            .custom-text {
                font-weight: normal;
            }
            .caption {
                color: black;
                font-size: 18px;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)
def navigate_to(page):
    st.session_state.page = page

def Welcome():
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{get_base64_of_bin_file('8.jpg')}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
    """, unsafe_allow_html=True)
    st.markdown("""
            <p style='text-align: left; color: black; font-size: 24px;'>
     Welcome to our tool, using machine learning to assess Breast Cancer and Diabetes risk, helping users take early preventive steps.
            </p>
        """, unsafe_allow_html=True)

    if st.button("Cancer Detection"):
        navigate_to("Cancer")
    if st.button("Pima Indian women"):
        navigate_to("Pima_Indian_women")
    if st.button("Meet the Team"):
        navigate_to("Meet the team")

def Pima_Indian_women():
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{get_base64_of_bin_file('9.jpg')}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
    """, unsafe_allow_html=True)

    st.title("Pima Indian women")
    st.markdown("""
            <p style='text-align: left; color: black; font-size: 24px;'>
            Pima Indian women have higher rates of type 2 diabetes compared to the general population in the United States. Some studies suggest that around 50% of Pima Indian women over the age of 40 may develop diabetes.
            </p>
        """, unsafe_allow_html=True)

    st.markdown("<p class='custom-text'>Statistics about Pima Indian women:</p>", unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("""
            <p style='text-align: left; color: black; font-size: 20px;'>
            *Type 1 Diabetes*: A chronic autoimmune condition where the body's immune system attacks and destroys the insulin-producing beta cells in the pancreas, resulting in little to no insulin production.
            </p>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
            <p style='text-align: left; color: black; font-size: 20px;'>
            *Type 2 Diabetes*: The most common form of diabetes, it occurs when the body does not use insulin effectively (insulin resistance) or when the pancreas does not produce enough insulin.
            </p>
        """, unsafe_allow_html=True)

    if st.button("Go to Home"):
        navigate_to("Home")
    if st.button("Go to Test"):
        navigate_to("Test")
def Cancer():
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{get_base64_of_bin_file('6.jpg')}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
    """, unsafe_allow_html=True)

    st.title("Breast Cancer Detection")
    st.markdown("""
            <p style='text-align: left; color: black; font-size: 24px;'>
            Breast cancer is one of the most common cancers affecting people globally, 
            including men. It happens when cells in the breast grow uncontrollably, forming a tumor. 
            Early detection is crucial for better outcomes. Our model uses advanced techniques to help detect cancer early, 
            aiming to support better health and outcomes.
            </p>
        """, unsafe_allow_html=True)

    image1 = resize_image("1.png", size=(1000, 1000))
    image2 = resize_image('22.png', size=(1000, 1000))
    image3 = resize_image("4.png", size=(1000, 1000))
    image4 = resize_image('2.png', size=(1000, 1000))
    st.markdown("<p class='custom-text'>Statistics about the disease:</p>", unsafe_allow_html=True)

    col3, col4 = st.columns(2)
    with col3:
        st.image(image1)
        st.markdown("""
            <p style='text-align: left; color: black; font-size: 20px;'>
            •  Prevalence: Breast cancer is the most common cancer worldwide, with an estimated 2.3 million new cases reported in 2020.
            </p>
        """, unsafe_allow_html=True)
    with col4:
        st.image(image2) 
        st.markdown("""
         <p style='text-align: left; color: black; font-size: 20px;'>
            •  Mortality Rate: It is the second leading cause of cancer-related deaths globally, with approximately 685,000 deaths in 2020.
        </p>
        """, unsafe_allow_html=True)

    col5, col6 = st.columns(2)
    with col5:
        st.image(image3)
        st.markdown("""
         <p style='text-align: left; color: black; font-size: 20px;'>
            Genetic Mutations: About 5-10% of breast cancer cases are linked to genetic mutations (e.g., BRCA1 and BRCA2).
        </p>
        """, unsafe_allow_html=True)
    with col6:
        st.image(image4)
        st.markdown("""
        <p style='text-align: left; color: black; font-size: 20px;'>
            Gender: Women are at a higher risk than men, though men can also develop breast cancer.
        </p>
        """, unsafe_allow_html=True)

    if st.button("Go to Test"):
        navigate_to("Test")
    if st.button("Go to Meet the Team"):
        navigate_to("About")
def test_of_Cancer():
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{get_base64_of_bin_file('6.jpg')}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
    """, unsafe_allow_html=True)
    st.markdown("""
    <style>
    .custom-title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
    }
    </style>
    <p class='custom-title'>Breast Cancer Prediction</p>
    """, unsafe_allow_html=True)
    radius_mean = st.slider('Radius Mean:', min_value=0.0, max_value=30.0, step=0.1)
    texture_mean = st.slider('Texture Mean:', min_value=0.0, max_value=40.0, step=0.1)
    smoothness_mean = st.slider('Smoothness Mean:', min_value=0.0, max_value=0.2, step=0.01)
    compactness_mean = st.slider('Compactness Mean:', min_value=0.0, max_value=0.2, step=0.01)
    symmetry_mean = st.slider('Symmetry Mean:', min_value=0.0, max_value=0.3, step=0.01)
    fractal_dimension_mean = st.slider('Fractal Dimension Mean:', min_value=0.0, max_value=0.1, step=0.001)
    radius_se = st.slider('Radius SE:', min_value=0.0, max_value=5.0, step=0.1)
    texture_se = st.slider('Texture SE:', min_value=0.0, max_value=10.0, step=0.1)
    smoothness_se = st.slider('Smoothness SE:', min_value=0.0, max_value=0.05, step=0.001)
    compactness_se = st.slider('Compactness SE:', min_value=0.0, max_value=0.05, step=0.001)
    symmetry_se = st.slider('Symmetry SE:', min_value=0.0, max_value=0.05, step=0.001)
    fractal_dimension_se = st.slider('Fractal Dimension SE:', min_value=0.0, max_value=0.05, step=0.001)
    if st.button('Predict'):
        user_data = [radius_mean, texture_mean, smoothness_mean, compactness_mean,
                     symmetry_mean, fractal_dimension_mean, radius_se, texture_se, 
                      smoothness_se, compactness_se, symmetry_se, fractal_dimension_se]
        user_data = np.array(user_data).reshape(1, -1)
        model = joblib.load('model.pkl')
        prediction = model.predict(user_data)
        if prediction[0] == 1:
            st.success('The model predicts the tumor is Malignant.')
        else:
            st.success('The model predicts the tumor is Benign.')
    if st.button("Go to Home"):
        navigate_to("Home")
    if st.button("Go to Blood Pressure"):
        navigate_to("Blood Pressure")
def Test_of_Pima_Indian_women():
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{get_base64_of_bin_file('9.jpg')}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
    """, unsafe_allow_html=True)
    model = joblib.load('model.pkl')
    st.markdown("""
    <style>
    .custom-title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #FF5733;
    }
    </style>
    <p class='custom-title'>Pima Indian women Prediction</p>
    """, unsafe_allow_html=True)
    pregnancies = st.slider('Pregnancies:', min_value=0.0, max_value=17.0, value=1.0, step=1.0)
    glucose = st.slider('Glucose:', min_value=0.0, max_value=199.0, value=100.0, step=1.0)
    blood_pressure = st.slider('Blood Pressure:', min_value=0.0, max_value=122.0, value=80.0, step=1.0)
    skin_thickness = st.slider('Skin Thickness:', min_value=0.0, max_value=99.0, value=20.0, step=1.0)
    insulin = st.slider('Insulin:', min_value=0.0, max_value=846.0, value=80.0, step=1.0)
    bmi = st.slider('Body Mass Index (BMI):', min_value=0.0, max_value=67.1, value=22.0, step=0.1)
    diabetes_pedigree_function = st.slider('Diabetes Pedigree Function:', min_value=0.078, max_value=2.42, value=0.5, step=0.01)
    age = st.slider('Age:', min_value=21, max_value=81, value=30, step=1)
    if st.button('Predict Anemia'):
        user_data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]
        user_data = np.array(user_data).reshape(1, -1)
        prediction = model.predict(user_data)
        st.success(f'Predicted Anemia Category: {prediction[0]}')
    if st.button("Go to Home"):
        navigate_to("Home")
    if st.button("Go to Test"):
        navigate_to("Test")
def Meet_the_team():
 st.title("About")
 st.markdown("<p class='custom-text'>Website developers</p>", unsafe_allow_html=True)
 people = [
        {"image": "2.jpg", "name": "Mostafa Arafat", "description": "Team member"},
        {"image": "1.jpg", "name": "Mostafa Ibrahim", "description": "Team member"},
        {"image": "WhatsApp Image 2024-09-11 at 18.26.48_6dfb3807.jpg", "name": "Rofaida Abdelaleem", "description": "Team member"},
        {"image": "WhatsApp Image 2024-09-11 at 22.55.17_1251f220.jpg", "name": "Basant Fathi", "description": "Team member"}
    ]
 for person in people:
        st.image(create_circular_image(person["image"]), caption=f"Photo of {person['name']}", width=150)
        st.markdown(f"<p class='custom-text'>{person['name']} - {person['description']}</p>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)
 if st.button("Go to Home"):
        navigate_to("Home")
def main():
    if 'page' not in st.session_state:
        st.session_state.page = "Welcome"

    set_page_style()

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Cancer", "Pima Indian women","Test of Cancer", "Test of Pima Indian women", "Meet the team"])
    
    navigate_to(page)

    if st.session_state.page == "Home":
        Welcome()
    elif st.session_state.page == "Cancer":
        Cancer()
    elif st.session_state.page == "Pima Indian women":
        Pima_Indian_women()
    elif st.session_state.page == "Test of Cancer":
        test_of_Cancer()
    elif st.session_state.page == "Test of Pima Indian women":
        Test_of_Pima_Indian_women()
    elif st.session_state.page == "Meet the team":
        Meet_the_team()

if __name__ == "__main__":
    main()
