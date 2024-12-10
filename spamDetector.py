import streamlit as st
import pickle

# Load the model and vectorizer
model = pickle.load(open('spam.pkl', 'rb'))
cv = pickle.load(open('vec.pkl', 'rb'))

# Add custom CSS for styling
def add_custom_css():
    st.markdown(
        """
        <style>
        body {
            background: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
            font-family: 'Arial', sans-serif;
        }
        .main {
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
        }
        h1 {
            text-align: center;
            color: white;
            font-family: 'Verdana', sans-serif;
            margin-bottom: 10px;
        }
        h2 {
            color: white;
            text-align: center;
            margin-bottom: 15px;
        }
        .stButton>button {
            background-color: #008CBA;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 12px 24px;
            font-size: 18px;
            cursor: pointer;
            box-shadow: 0px 4px 6px rgba(0, 123, 255, 0.3);
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #005f73;
            transform: translateY(-2px);
            box-shadow: 0px 6px 12px rgba(0, 123, 255, 0.5);
        }
        .success {
            background-color: #d4edda;
            color: #155724;
            padding: 20px;
            border-radius: 8px;
            margin-top: 15px;
            font-weight: bold;
        }
        .error {
            background-color: #f8d7da;
            color: #721c24;
            padding: 20px;
            border-radius: 8px;
            margin-top: 15px;
            font-weight: bold;
        }
        .stTextArea>div>textarea {
            border: 2px solid #008CBA;
            border-radius: 8px;
            padding: 10px;
            font-size: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Main app function
def main():
    add_custom_css()  # Apply custom styles
    st.title("📧 Email Spam Classification Application")
    st.markdown("This is a Machine Learning application to classify emails as Spam or Ham. 🚀")

    st.subheader("🔍 Enter Email for Classification:")
    user_input = st.text_area(
        "📬 Type your email content below:", 
        height=150, 
        placeholder="Example: Congratulations! You have won a lottery. Click here to claim your prize."
    )

    if st.button("Classify Email"):
        if user_input:
            data = [user_input]
            vec = cv.transform(data).toarray()
            result = model.predict(vec)
            if result[0] == 0:
                st.markdown('<div class="success">✅ This is Not A Spam Email!</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="error">🚫 This is A Spam Email!</div>', unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please enter an email to classify.")
    
    st.markdown("---")
    st.info("💡 **Tip:** Use realistic email samples to test the application.")

# Run the app
if __name__ == '__main__':
    main()
