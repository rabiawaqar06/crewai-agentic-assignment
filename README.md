# Study Helper Crew

An AI-powered study assistant built with CrewAI and Google Gemini API that helps students learn more effectively through intelligent text analysis and practice questions.

## 🎯 Project Overview

The Study Helper Crew uses multiple AI agents to transform any study material into an interactive learning experience:

1. **Reader Agent** - Extracts key points from your study material
2. **Explainer Agent** - Simplifies complex concepts into easy-to-understand explanations  
3. **Quiz Agent** - Generates practice questions to test your understanding

## 🤖 Agents and Their Roles

### Reader Agent
- **Role**: Text Reader and Summarizer
- **Goal**: Extract the most important key points from study material
- **Capabilities**: 
  - Identifies main topics and concepts
  - Organizes information in a structured way
  - Focuses on the most relevant learning content

### Explainer Agent  
- **Role**: Concept Explainer
- **Goal**: Simplify complex concepts into easy-to-understand explanations
- **Capabilities**:
  - Breaks down complex topics into simpler parts
  - Uses analogies and examples
  - Makes connections between different ideas
  - Uses everyday language for clarity

### Quiz Agent
- **Role**: Quiz Generator  
- **Goal**: Create effective practice questions to test understanding
- **Capabilities**:
  - Generates 3-5 high-quality practice questions
  - Creates both multiple choice and short answer questions
  - Tests different levels of understanding
  - Provides correct answers with explanations

## 🛠 Tech Stack

- **Python 3.10+**
- **CrewAI** - Multi-agent AI framework
- **Google Gemini API** - Large Language Model
- **LangChain** - LLM integration
- **Streamlit** - Optional web UI (for future enhancement)

## 📁 Project Structure

```
study-helper-crew/
├── main.py            # Command line CrewAI workflow
├── app_simple.py      # Streamlit web interface
├── requirements.txt   # Python dependencies
├── .env.example      # Environment variables template
├── .gitignore        # Git ignore file
├── README.md          # This file
└── .env              # Environment variables (create this)
```

## 🚀 Setup Instructions

### 1. Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt
```

### 2. Get Google Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the API key for the next step

### 3. Set Environment Variables

Create a `.env` file in the project directory:

```bash
# Copy the example file
cp .env.example .env

# Edit the .env file and add your API key
# GEMINI_API_KEY=your_actual_api_key_here
```

Or create the file manually:
```bash
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

Replace `your_api_key_here` with your actual Google Gemini API key.

### 4. Run the Application

#### Option A: Streamlit Web Interface (Recommended)
```bash
# Run the web interface
streamlit run app_simple.py
```

#### Option B: Command Line Interface
```bash
# Run the command line version
python main.py
```

## 📖 How to Use

### Web Interface (Streamlit)
1. **Start the web app**: Run `streamlit run app_simple.py`
2. **Open your browser**: Navigate to the URL shown in the terminal (usually http://localhost:8501)
3. **Paste your study material**: Use the text area to input your study content
4. **Click 'Process Text'**: The AI agents will analyze your text
5. **Review the results**: Get summaries, explanations, and practice questions
6. **Download results**: Save your analysis as a text file

### Command Line Interface
1. **Start the application**: Run `python main.py`
2. **Paste your study material**: Copy and paste any text from textbooks, articles, or notes
3. **Press Enter twice**: This signals that you're done entering text
4. **Get your results**: The crew will process your text and provide:
   - Key points summary
   - Simple explanations
   - Practice questions with answers

## 💡 Example Usage

```
📚 Study Helper Crew - AI-Powered Study Assistant
==================================================

Please paste your study text below (press Enter twice when done):
------------------------------
[Paste your study material here]

📖 Processing text (1,234 characters)...
🚀 Starting Study Helper Crew...
==================================================

[AI agents work on your text...]

==================================================
✅ Study Helper Crew Complete!
==================================================

[Your personalized study materials appear here]
```

## 🔧 Configuration

You can modify the agents' behavior by editing the `main.py` file:

- **Temperature**: Adjust creativity vs consistency (default: 0.7)
- **Model**: Change Gemini model (default: gemini-1.5-flash)
- **Agent roles**: Customize agent goals and backstories
- **Task descriptions**: Modify how agents process information

## 🐛 Troubleshooting

### Common Issues

1. **"GEMINI_API_KEY not found"**
   - Make sure you've created a `.env` file
   - Check that your API key is correct
   - Ensure the `.env` file is in the same directory as `main.py`

2. **Import errors**
   - Make sure all dependencies are installed: `pip install -r requirements.txt`
   - Check that you're using Python 3.10 or higher

3. **API rate limits**
   - Google Gemini has usage limits
   - Try shorter text inputs if you hit limits
   - Consider upgrading your API plan

## 🚀 Future Enhancements

- **Multiple file formats**: Support for PDF, Word documents
- **Study sessions**: Save and track learning progress
- **Custom agents**: Add specialized agents for different subjects
- **Export options**: Save results as PDF or text files
- **User accounts**: Personal study history and progress tracking
- **Mobile responsive**: Better mobile device support

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

---

**Happy Studying! 📚✨**
