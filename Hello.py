# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import cv2
import numpy as np

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )
    st.write("# :balloon: CV Activity 1")
    


    st.title("Image Transformation ")
    
    st.write("Name : Prachi Jadhav (0120200180)")

    # Upload an image
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_image is not None:
        image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), 1)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Transformation options
        transform_option = st.selectbox("Select Transformation", ["Translation", "Rotation", "Scaling", "Shearing", "Horizontal Flip"])

        if transform_option == "Translation":
            translation_x = st.number_input("Enter translation in X direction", min_value=-500, max_value=500, value=0)
            translation_y = st.number_input("Enter translation in Y direction", min_value=-500, max_value=500, value=0)

            translation_matrix = np.float32([[1, 0, translation_x], [0, 1, translation_y]])
            translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
            st.image(translated_image, caption="Translated Image", use_column_width=True)

        elif transform_option == "Rotation":
            rotation_angle = st.number_input("Enter rotation angle in degrees", min_value=-360, max_value=360, value=0)
            rotation_matrix = cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), rotation_angle, 1)
            rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
            st.image(rotated_image, caption="Rotated Image", use_column_width=True)

        elif transform_option == "Scaling":
            scaling_factor = st.number_input("Enter scaling factor", min_value=0.1, max_value=10.0, value=1.0)
            scaling_matrix = np.float32([[scaling_factor, 0, 0], [0, scaling_factor, 0]])
            scaled_image = cv2.warpAffine(image, scaling_matrix, (image.shape[1], image.shape[0]))
            st.image(scaled_image, caption="Scaled Image", use_column_width=True)

        elif transform_option == "Shearing":
            shear_factor = st.number_input("Enter shear factor", min_value=-10, max_value=10, value=0)
            shear_matrix = np.float32([[1, shear_factor, 0], [shear_factor, 1, 0]])
            sheared_image = cv2.warpAffine(image, shear_matrix, (image.shape[1], image.shape[0]))
            st.image(sheared_image, caption="Sheared Image", use_column_width=True)

        elif transform_option == "Horizontal Flip":
            flipped_image = cv2.flip(image, 1)
            st.image(flipped_image, caption="Horizontally Flipped Image", use_column_width=True)
    

if __name__ == "__main__":
    run()
