"""
Study Helper Crew - A CrewAI project with multiple agents to help students study
Uses Google Gemini API as the LLM
"""

import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai.llm import LLM
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Initialize Gemini LLM
def get_gemini_llm():
    """Initialize Google Gemini LLM"""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables")
    
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=api_key,
        temperature=0.7
    )

# Create LLM instance
llm = get_gemini_llm()

# Define Agents
def create_reader_agent():
    """Create the Reader Agent that extracts key points from text"""
    return Agent(
        role="Text Reader and Summarizer",
        goal="Read and extract the most important key points from the given text",
        backstory="""You are an expert at reading and analyzing text. Your job is to:
        1. Read the input text carefully
        2. Identify the main topics and concepts
        3. Extract the most important key points
        4. Organize them in a clear, structured way
        5. Focus on the most relevant information for learning""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

def create_explainer_agent():
    """Create the Explainer Agent that simplifies complex concepts"""
    return Agent(
        role="Concept Explainer",
        goal="Simplify complex concepts into easy-to-understand explanations",
        backstory="""You are a master teacher who excels at explaining complex topics in simple terms. Your job is to:
        1. Take the key points from the Reader Agent
        2. Break down complex concepts into simpler parts
        3. Use analogies, examples, and everyday language
        4. Make sure explanations are clear and easy to follow
        5. Focus on helping students truly understand the material""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

def create_quiz_agent():
    """Create the Quiz Agent that generates practice questions"""
    return Agent(
        role="Quiz Generator",
        goal="Create effective practice questions to test understanding",
        backstory="""You are an expert educator who creates excellent practice questions. Your job is to:
        1. Review the key points and explanations
        2. Create 3-5 high-quality practice questions
        3. Include both multiple choice and short answer questions
        4. Make questions that test different levels of understanding
        5. Provide clear, correct answers for all questions""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

# Define Tasks
def create_reader_task(text_input):
    """Create task for Reader Agent"""
    return Task(
        description=f"""
        Read and analyze the following text carefully:
        
        {text_input}
        
        Extract and summarize the key points. Focus on:
        - Main topics and concepts
        - Important details and facts
        - Key relationships between ideas
        - Most relevant information for learning
        
        Provide a clear, organized summary of the key points.
        """,
        agent=create_reader_agent(),
        expected_output="A well-organized summary of key points from the text, structured for easy understanding."
    )

def create_explainer_task(reader_output):
    """Create task for Explainer Agent"""
    return Task(
        description=f"""
        Take the following key points and explain them in simple, easy-to-understand terms:
        
        {reader_output}
        
        Your explanation should:
        - Use simple, clear language
        - Include analogies or examples where helpful
        - Break down complex concepts into smaller parts
        - Make connections between different ideas
        - Help students truly understand the material
        
        Focus on making the content accessible and memorable.
        """,
        agent=create_explainer_agent(),
        expected_output="Clear, simple explanations of the key concepts that help students understand the material."
    )

def create_quiz_task(explainer_output):
    """Create task for Quiz Agent"""
    return Task(
        description=f"""
        Based on the following explanations, create 3-5 practice questions:
        
        {explainer_output}
        
        Create questions that:
        - Test understanding of the main concepts
        - Include both multiple choice and short answer questions
        - Cover different levels of difficulty
        - Are clear and unambiguous
        - Help students practice and learn
        
        For each question, provide:
        - The question text
        - Multiple choice options (if applicable)
        - The correct answer
        - A brief explanation of why the answer is correct
        """,
        agent=create_quiz_agent(),
        expected_output="3-5 well-crafted practice questions with answers and explanations."
    )

def run_study_helper_crew(text_input):
    """Run the complete Study Helper Crew workflow"""
    print("🚀 Starting Study Helper Crew...")
    print("=" * 50)
    
    # Create tasks
    reader_task = create_reader_task(text_input)
    explainer_task = create_explainer_task("")  # Will be updated with reader output
    quiz_task = create_quiz_task("")  # Will be updated with explainer output
    
    # Create crew
    crew = Crew(
        agents=[create_reader_agent(), create_explainer_agent(), create_quiz_agent()],
        tasks=[reader_task, explainer_task, quiz_task],
        verbose=True,
        process=Process.sequential
    )
    
    # Execute the crew
    result = crew.kickoff()
    
    return result

def main():
    """Main function to run the Study Helper Crew"""
    print("📚 Study Helper Crew - AI-Powered Study Assistant")
    print("=" * 50)
    
    # Get text input from user
    print("\nPlease paste your study text below (press Enter twice when done):")
    print("-" * 30)
    
    lines = []
    while True:
        line = input()
        if line == "" and len(lines) > 0 and lines[-1] == "":
            break
        lines.append(line)
    
    text_input = "\n".join(lines).strip()
    
    if not text_input:
        print("❌ No text provided. Please try again.")
        return
    
    print(f"\n📖 Processing text ({len(text_input)} characters)...")
    
    try:
        # Run the crew
        result = run_study_helper_crew(text_input)
        
        print("\n" + "=" * 50)
        print("✅ Study Helper Crew Complete!")
        print("=" * 50)
        print(result)
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("Please check your GEMINI_API_KEY and try again.")

if __name__ == "__main__":
    main()
