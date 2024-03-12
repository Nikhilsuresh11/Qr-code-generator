import streamlit as st
import qrcode
from PIL import Image
import io
import base64

def generate_qr_code(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    return qr_img

st.title("QR Code Generator")

link = st.text_input("Enter a link:")
custom_filename = st.text_input("Enter a custom filename for the QR code image (optional):")

if st.button("Generate QR Code"):
    qr_code = generate_qr_code(link)
    
    # Convert PIL image to bytes
    img_bytes = io.BytesIO()
    qr_code.save(img_bytes, format='PNG')
    img_bytes.seek(0)  # Reset the pointer to the beginning of the stream
    
    # Display QR code image
    st.image(img_bytes, caption="QR Code", use_column_width=True)
    
    # Add download button with custom filename if provided
    if custom_filename:
        filename = custom_filename + ".png"
    else:
        filename = "qr_code.png"
        
    # Add download button
    st.download_button(
        label="Download QR Code Image",
        data=img_bytes.getvalue(),
        file_name=filename,
        mime="image/png"
    )

    
    # Add share button
    st.write("Share QR Code:")
    st.write("[Facebook](https://www.facebook.com/sharer/sharer.php?u=" + link + ")")
    st.write("[Twitter](https://twitter.com/intent/tweet?url=" + link + "&text=Check%20out%20this%20QR%20Code)")
    st.write("[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=" + link + "&title=QR%20Code&summary=Check%20out%20this%20QR%20Code&source=)")
