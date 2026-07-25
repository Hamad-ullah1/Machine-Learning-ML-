# app.py
import streamlit as st
from backend import ChatBot


def main():
    st.set_page_config(page_title="NVTTC Chatbot", page_icon="🤖", layout="wide")

    # Initialize session state
    if "chatbot" not in st.session_state:
        st.session_state.chatbot = None
        st.session_state.messages = []
        st.session_state.model_loaded = False

    # Sidebar for model selection
    with st.sidebar:
        st.title("🤖 Chatbot Settings")

        model_options = {
            "DialoGPT Medium": "microsoft/DialoGPT-medium",
            "GPT-2": "gpt2",
        }

        selected_model = st.selectbox(
            "Choose Model:", list(model_options.keys()), index=0
        )

        model_name = model_options[selected_model]

        # Load model button
        if st.button("Load Model", type="primary"):
            with st.spinner("Loading model... This may take a minute..."):
                st.session_state.chatbot = ChatBot(model_name)
                success = st.session_state.chatbot.load_model()

                if success:
                    st.session_state.model_loaded = True
                    st.success(f"✅ Model '{selected_model}' loaded successfully!")
                    st.session_state.messages = []  # Clear chat history
                else:
                    st.error("❌ Failed to load model. Please try again.")

        # Reset conversation
        if st.button("Reset Conversation"):
            if st.session_state.chatbot:
                st.session_state.chatbot.reset_conversation()
                st.session_state.messages = []
                st.success("Conversation reset!")

        # Model information
        st.divider()
        st.subheader("📚 Educational Info")
        st.markdown(
            """
        **Models Explained:**
        - **GPT-2**: General language model
        - **DialoGPT**: Fine-tuned GPT-2 for dialogue
        
        **Key Concepts Demonstrated:**
        - Pre-trained Models
        - Tokenization
        - Sequence Generation
        """
        )

    # Main chat interface
    st.title("🤖 NVTTC Chatbot")
    st.caption("A practical demonstration of transformer-based conversational AI")

    if not st.session_state.model_loaded:
        st.info("👈 Select a model and click 'Load Model' to get started!")
        show_tutorial()
        return

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    if prompt := st.chat_input("Type your message here..."): # := Walrus operator (Python 3.8+) - assigns AND checks if value is truthy in one line.
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.chatbot.get_response(prompt)
                st.markdown(response)

        # Add assistant response to chat
        st.session_state.messages.append({"role": "assistant", "content": response})


def show_tutorial():
    """Display tutorial information"""
    st.subheader("🎓 Course Wrap-up Tutorial")
    st.markdown(
        """
    ### What You've Learned:
    1. **Machine Learning Fundamentals** - Supervised/Unsupervised learning
    2. **Deep Learning Basics** - Neural networks, backpropagation
    3. **Computer Vision & NLP** - CNNs, RNNs, attention mechanisms  
    4. **Transformer Architecture** - Self-attention, BERT, GPT
    
    ### This Demo Shows:
    - How pre-trained transformers work in practice
    - Real-world application of attention mechanisms
    - Transfer learning benefits
    - Practical deployment considerations
    
    ### Try These Prompts:
    - "Explain what a transformer is"
    - "What's the difference between BERT and GPT?"
    - "Tell me about attention mechanisms"
    - "How does transfer learning work?"
    """
    )


if __name__ == "__main__":
    main()
