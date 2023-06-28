import streamlit as st
def app():
    st.header("Ways for Healthier Lifestyle")
    st.markdown(
        """The lifestyle of an individual plays an important role in determining if a person is most likely to get 
                Coronary Thrombosis in the nearby future.
                A person who is more active physically and has a healthy diet and avoids smoking has  way less chance of 
                getting coronary thrombosis than the one who is in his bed all day, eating junks and smokes a lot.
                \nHere we try to suggest few ways in which we can improve an individual's lifestyle.
                At first, we have YOGA, which helps an individual move his body around physically and regulates the blood flow through out his body
                Diet follows Yoga. As the famous saying goes "Abs are made in the Kitchen" what we eat defines our health. 
                \nClick on the tabs given below to learn more about them.""")
    with st.expander("YOGA"):
        st.markdown("Here is a video which shows us various yoga asanas which help us in improving our overall health")
        st.video("https://youtu.be/CS7uNgsrlYA")
    with st.expander("DIET"):
        st.markdown("Diet plays an important role in our day to day life and is underrated so much. We can spread awareness and learn more by watching the video given below")
        st.video("https://youtu.be/jUm8fFcTbG0")

        col1, col2=st.columns(2)
        with col1:
            st.markdown("Here's a list of food items to avoid:-")
            st.markdown("1. High amounts of Sugar, Salt and Saturated Fat")
            st.markdown("2. Fried food items")
            st.markdown("3. Bacon and Processed Meats")
            st.markdown("4. Soda")

        with col2:
            st.markdown("Here's a list of food items to include:-")
            st.markdown("1. Fresh Fruits and Vegetables")
            st.markdown("2. Whole Grain")
            st.markdown("3. Lean Protein")
            st.markdown("4. Replace seasonings with herbs")


