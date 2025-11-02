"""
Study Helper Crew - Simple Streamlit Frontend
A web interface for the Study Helper Crew AI application using direct Gemini API
"""

import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
import time

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Study Helper Crew",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .agent-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #1f77b4;
    }
    .result-section {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border: 1px solid #dee2e6;
    }
    .success-message {
        color: #28a745;
        font-weight: bold;
    }
    .error-message {
        color: #dc3545;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

def initialize_gemini():
    """Initialize Google Gemini API"""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        st.error("❌ GEMINI_API_KEY not found in environment variables. Please set your API key in the .env file.")
        return None
    
    try:
        genai.configure(api_key=api_key)
        return genai.GenerativeModel('gemini-2.0-flash')
    except Exception as e:
        st.error(f"❌ Error initializing Gemini: {str(e)}")
        return None

def run_reader_agent(model, text_input):
    """Reader Agent - Extract key points"""
    prompt = f"""
    You are a Text Reader and Summarizer. Your job is to:
    1. Read the input text carefully
    2. Identify the main topics and concepts
    3. Extract the most important key points
    4. Organize them in a clear, structured way
    5. Focus on the most relevant information for learning
    
    Text to analyze:
    {text_input}
    
    Please provide a well-organized summary of the key points from the text, structured for easy understanding.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"❌ Reader Agent error: {str(e)}")
        return None

def run_explainer_agent(model, reader_output):
    """Explainer Agent - Simplify concepts"""
    prompt = f"""
    You are a Concept Explainer. Your job is to:
    1. Take the key points and explain them in simple, easy-to-understand terms
    2. Use simple, clear language
    3. Include analogies or examples where helpful
    4. Break down complex concepts into smaller parts
    5. Make connections between different ideas
    6. Help students truly understand the material
    
    Key points to explain:
    {reader_output}
    
    Please provide clear, simple explanations of the key concepts that help students understand the material.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"❌ Explainer Agent error: {str(e)}")
        return None

def run_quiz_agent(model, explainer_output):
    """Quiz Agent - Generate practice questions"""
    prompt = f"""
    You are a Quiz Generator. Your job is to:
    1. Review the explanations and create 3-5 high-quality practice questions
    2. Include both multiple choice and short answer questions
    3. Test different levels of understanding
    4. Make questions clear and unambiguous
    5. Help students practice and learn
    
    Explanations to create questions from:
    {explainer_output}
    
    For each question, provide:
    - The question text
    - Multiple choice options (if applicable)
    - The correct answer
    - A brief explanation of why the answer is correct
    
    Please create 3-5 well-crafted practice questions with answers and explanations.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"❌ Quiz Agent error: {str(e)}")
        return None

def main():
    """Main Streamlit application"""
    
    # Header
    st.markdown('<h1 class="main-header">📚 Study Helper Crew</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">AI-Powered Study Assistant</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("🤖 AI Agents")
        
        st.markdown("""
        <div class="agent-card">
            <h4>📖 Reader Agent</h4>
            <p>Extracts key points from your study material</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="agent-card">
            <h4>💡 Explainer Agent</h4>
            <p>Simplifies complex concepts into easy explanations</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="agent-card">
            <h4>❓ Quiz Agent</h4>
            <p>Generates practice questions to test your understanding</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.header("⚙️ Settings")
        
        # API Key status
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key:
            st.success("✅ API Key configured")
        else:
            st.error("❌ API Key not found")
            st.info("Please set GEMINI_API_KEY in your .env file")
        
        st.header("📋 Instructions")
        st.markdown("""
        1. **Paste your study material** in the text area
        2. **Click 'Process Text'** to start the AI analysis
        3. **Review the results** from all three agents
        4. **Use the practice questions** to test your understanding
        """)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("📝 Input Your Study Material")
        
        # Text input area
        text_input = st.text_area(
            "Paste your study text here:",
            height=300,
            placeholder="Enter your textbook passage, article, or any study material here...",
            help="The AI agents will analyze this text and provide summaries, explanations, and practice questions."
        )
        
        # Process button
        if st.button("🚀 Process Text", type="primary", use_container_width=True):
            if not text_input.strip():
                st.warning("⚠️ Please enter some text to process.")
            elif not os.getenv("GEMINI_API_KEY"):
                st.error("❌ Please configure your GEMINI_API_KEY in the .env file.")
            else:
                # Initialize Gemini
                model = initialize_gemini()
                if model:
                    with st.spinner("🤖 AI agents are working on your text..."):
                        # Show progress
                        progress_bar = st.progress(0)
                        status_text = st.empty()
                        
                        # Reader Agent
                        progress_bar.progress(25)
                        status_text.text("📖 Reader Agent is analyzing the text...")
                        reader_result = run_reader_agent(model, text_input)
                        
                        if reader_result:
                            # Explainer Agent
                            progress_bar.progress(50)
                            status_text.text("💡 Explainer Agent is simplifying concepts...")
                            explainer_result = run_explainer_agent(model, reader_result)
                            
                            if explainer_result:
                                # Quiz Agent
                                progress_bar.progress(75)
                                status_text.text("❓ Quiz Agent is creating practice questions...")
                                quiz_result = run_quiz_agent(model, explainer_result)
                                
                                if quiz_result:
                                    progress_bar.progress(100)
                                    status_text.text("✅ Analysis complete!")
                                    time.sleep(1)
                                    
                                    # Clear progress indicators
                                    progress_bar.empty()
                                    status_text.empty()
                                    
                                    # Display results
                                    st.success("🎉 Study Helper Crew has completed the analysis!")
                                    
                                    # Store results in session state
                                    st.session_state['reader_result'] = reader_result
                                    st.session_state['explainer_result'] = explainer_result
                                    st.session_state['quiz_result'] = quiz_result
                                else:
                                    st.error("❌ Quiz Agent failed. Please try again.")
                            else:
                                st.error("❌ Explainer Agent failed. Please try again.")
                        else:
                            st.error("❌ Reader Agent failed. Please try again.")
    
    with col2:
        st.header("📊 Text Statistics")
        if text_input:
            st.metric("Characters", len(text_input))
            st.metric("Words", len(text_input.split()))
            st.metric("Lines", len(text_input.split('\n')))
        else:
            st.info("Enter text to see statistics")
    
    # Display results
    if 'reader_result' in st.session_state:
        st.header("📋 Analysis Results")
        
        # Reader Results
        with st.expander("📖 Key Points Summary", expanded=True):
            st.markdown(st.session_state['reader_result'])
        
        # Explainer Results
        with st.expander("💡 Simple Explanations", expanded=True):
            st.markdown(st.session_state['explainer_result'])
        
        # Quiz Results
        with st.expander("❓ Practice Questions", expanded=True):
            st.markdown(st.session_state['quiz_result'])
        
        # Download button
        full_result = f"""
# Study Helper Crew Analysis

## 📖 Key Points Summary
{st.session_state['reader_result']}

## 💡 Simple Explanations
{st.session_state['explainer_result']}

## ❓ Practice Questions
{st.session_state['quiz_result']}
        """
        
        st.download_button(
            label="💾 Download Results",
            data=full_result,
            file_name="study_analysis.txt",
            mime="text/plain",
            use_container_width=True
        )
        
        # Clear results button
        if st.button("🗑️ Clear Results", use_container_width=True):
            for key in ['reader_result', 'explainer_result', 'quiz_result']:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; margin-top: 2rem;">
        <p>Built with ❤️ using CrewAI, Google Gemini, and Streamlit</p>
        <p>Transform any text into an interactive learning experience!</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
