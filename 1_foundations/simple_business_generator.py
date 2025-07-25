# Simple Business Idea Generator for Data Engineering in Universities
# This code can be run directly in your lab notebook

# Step 1: Generate Business Idea
business_prompt = """
Please identify a specific business opportunity in the field of data engineering 
that could be applied within university environments. Focus on areas where 
universities struggle with data management, analytics, or data-driven decision making.

Provide a clear, specific business idea that addresses a real need in higher education.
"""

print("🔍 Generating business idea for data engineering in universities...")
messages = [{"role": "user", "content": business_prompt}]
response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)
business_idea = response.choices[0].message.content
print(f"\n📊 Business Idea:\n{business_idea}\n")

# Step 2: Identify Pain Points
pain_points_prompt = f"""
Based on this business idea about data engineering in universities:

"{business_idea}"

Please identify the top 3-5 specific pain points that universities currently face 
in this area. Be specific about the challenges, inefficiencies, and problems 
that make this business opportunity viable.

Format your response as a numbered list of pain points with brief explanations.
"""

print("🎯 Identifying pain points in the industry...")
messages = [{"role": "user", "content": pain_points_prompt}]
response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)
pain_points = response.choices[0].message.content
print(f"\n💡 Pain Points:\n{pain_points}\n")

# Step 3: Propose Solutions
solutions_prompt = f"""
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
messages = [{"role": "user", "content": solutions_prompt}]
response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)
solutions = response.choices[0].message.content
print(f"\n💻 Proposed Solutions:\n{solutions}\n")

# Display final summary with markdown
from IPython.display import Markdown, display

summary = f"""
# 🎓 University Data Engineering Business Idea Summary

## 🎯 Business Opportunity
{business_idea}

## ⚠️ Key Pain Points
{pain_points}

## 🔧 Proposed Agentic AI Solutions
{solutions}

---
*Generated using OpenAI GPT-4.1-mini*
"""

display(Markdown(summary)) 