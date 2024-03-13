import streamlit as st
import langchain_helper

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine ",("Italian", "Mexican", "Japanese", "Indian", "Chinese", "French", "Thai", "Greek","Spanish", "Lebanese", "Arabic"))

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)

    # Input field to select menu item
    menu_item = st.text_input("Enter the number of the menu item to view its recipe:")
    if st.button("Generate Recipe"):
        # Display recipe for selected menu item
        if menu_item.isdigit() and 0 < int(menu_item) <= len(menu_items):
            recipe = langchain_helper.generate_recipe(menu_items[int(menu_item) - 1])
            st.subheader(f"Recipe for {menu_items[int(menu_item) - 1]}")
            st.write(recipe)
        else:
            st.error("Invalid selection. Please enter a valid number.")

