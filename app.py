import os
import random
import requests
import streamlit as st
from PIL import Image

API_KEY = os.environ.get('api_key')
import google.generativeai as palm
palm.configure(api_key=API_KEY)
response = palm.generate_text(prompt=" recipe")


def generate_recipe(type_of_recipe, number_of_servings, recipe,scale_ingredients=True):
    response = palm.generate_text(
        prompt=f"{type_of_recipe} recipe with number of servings: {number_of_servings} and recipe details: {recipe}"
    )
    return response.result


def main():
    st.title("Recipe Generator")

    type_of_recipe = st.selectbox(
        "Select the type of recipe you want:",
        options=["Indian", "American", "Mexican", "Italian","Chinese"],
    )
    number_of_servings = st.number_input("Number of servings:", step=1, min_value=1)
    recipe = st.text_area("Recipe details")
    scale_ingredients = st.checkbox("Scale ingredients?")

    if st.button("Generate Recipe"):
        recipe = generate_recipe(type_of_recipe, number_of_servings, recipe, scale_ingredients)
        st.subheader(f"{type_of_recipe} Recipe")
        st.write(recipe)


if __name__ == '__main__':
    main()

# Background Image
background_image_url = "https://source.unsplash.com/1600x900/?indian-food"
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url('{background_image_url}') no-repeat center center;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)








