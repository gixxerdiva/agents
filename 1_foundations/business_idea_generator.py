import os
from openai import OpenAI
from dotenv import load_dotenv
from IPython.display import Markdown, display

# Load environment variables
load_dotenv(override=True)

# Initialize OpenAI client
openai = OpenAI()

def ask_llm(prompt, model="gpt-4.1-mini"):
    """
    Helper function to ask the LLM a question
    """
    messages = [{"role": "user", "content": prompt}]
    
    response = openai.chat.completions.create(
        model=model,
        messages=messages
    )
    
    return response.choices[0].message.content

def generate_business_idea():
    """
    Step 1: Ask LLM to pick a business idea about data engineering in universities
    """
    prompt = """
    Please identify a specific business opportunity in the field of data engineering 
    that could be applied within university environments. Focus on areas where 
    universities struggle with data management, analytics, or data-driven decision making.
    
    Provide a clear, specific business idea that addresses a real need in higher education.
    """
    
    print("🔍 Generating business idea for data engineering in universities...")
    business_idea = ask_llm(prompt)
    print(f"\n📊 Business Idea:\n{business_idea}\n")
    
    return business_idea

def identify_pain_points(business_idea):
    """
    Step 2: Ask LLM to identify pain points in this industry
    """
    prompt = f"""
    Based on this business idea about data engineering in universities:
    
    "{business_idea}"
    
    Please identify the top 3-5 specific pain points that universities currently face 
    in this area. Be specific about the challenges, inefficiencies, and problems 
    that make this business opportunity viable.
    
    Format your response as a numbered list of pain points with brief explanations.
    """
    
    print("🎯 Identifying pain points in the industry...")
    pain_points = ask_llm(prompt)
    print(f"\n💡 Pain Points:\n{pain_points}\n")
    
    return pain_points

def propose_solutions(business_idea, pain_points):
    """
    Step 3: Ask LLM to propose 3 different solutions
    """
    prompt = f"""
    Based on this business idea and pain points:
    
    Business Idea: {business_idea}
    
    Pain Points: {pain_points}
    
    Please propose 3 different Agentic AI solutions that could address these challenges. 
    Each solution should be distinct and innovative, focusing on different aspects 
    of the problem or different approaches to solving it.
    
    For each solution, provide:
    1. A clear name/title
    2. Brief description of how it works
    3. Key features and capabilities
    4. How it specifically addresses the identified pain points
    
    Format as "Solution 1:", "Solution 2:", "Solution 3:" with detailed explanations.
    """
    
    print("🚀 Proposing 3 Agentic AI solutions...")
    solutions = ask_llm(prompt)
    print(f"\n💻 Proposed Solutions:\n{solutions}\n")
    
    return solutions

def main():
    """
    Main function to run the complete business idea generation process
    """
    print("🎓 University Data Engineering Business Idea Generator")
    print("=" * 60)
    
    # Step 1: Generate business idea
    business_idea = generate_business_idea()
    
    # Step 2: Identify pain points
    pain_points = identify_pain_points(business_idea)
    
    # Step 3: Propose solutions
    solutions = propose_solutions(business_idea, pain_points)
    
    # Display final summary
    print("\n" + "=" * 60)
    print("📋 FINAL SUMMARY")
    print("=" * 60)
    
    print(f"\n🎯 Business Opportunity:\n{business_idea}")
    print(f"\n⚠️  Key Pain Points:\n{pain_points}")
    print(f"\n🔧 Proposed Solutions:\n{solutions}")
    
    return {
        "business_idea": business_idea,
        "pain_points": pain_points,
        "solutions": solutions
    }

if __name__ == "__main__":
    # Check if API key is available
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ OpenAI API Key not found. Please set OPENAI_API_KEY in your .env file")
    else:
        print(f"✅ OpenAI API Key found: {os.getenv('OPENAI_API_KEY')[:8]}...")
        results = main() 