#!/usr/bin/env python3
"""
AI Company Brochure Generator
Generates professional company brochures using Claude API
"""

import anthropic
import json
import sys
import os
from datetime import datetime
from pathlib import Path
from anthropic import Anthropic
from dotenv import load_dotenv

# ======================
# LOAD ENV
# ======================
load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError("❌ ANTHROPIC_API_KEY is not set")
    


class BrochureGenerator:
    """Main class for generating company brochures using Claude API"""
    
    def __init__(self, api_key: str = None):
        """
        Initialize the brochure generator
        
        Args:
            api_key: Anthropic API key (if None, will use ANTHROPIC_API_KEY env var)
        """
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-6"
    
    def generate_brochure(self, company_data: dict) -> str:
        """
        Generate a complete brochure based on company data
        
        Args:
            company_data: Dictionary containing company information
            
        Returns:
            Generated brochure content in markdown format
        """
        # Build the prompt for Claude
        prompt = self._build_prompt(company_data)
        
        # Call Claude API
        print("🤖 Generating brochure with Claude API...")
        message = self.client.messages.create(
            model=self.model,
            max_tokens=4000,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        
        # Extract the text response
        brochure_content = message.content[0].text
        return brochure_content
    
    def _build_prompt(self, data: dict) -> str:
        """Build the prompt for Claude based on company data"""
        
        prompt = f"""You are a professional marketing copywriter specializing in creating compelling company brochures.

Create a professional, engaging company brochure based on the following information:

**Company Information:**
- Company Name: {data.get('company_name', 'N/A')}
- Industry: {data.get('industry', 'N/A')}
- Founded: {data.get('founded', 'N/A')}
- Location: {data.get('location', 'N/A')}

**About:**
{data.get('about', 'Not provided')}

**Products/Services:**
{data.get('products_services', 'Not provided')}

**Mission & Vision:**
{data.get('mission_vision', 'Not provided')}

**Key Differentiators:**
{data.get('differentiators', 'Not provided')}

**Target Audience:**
{data.get('target_audience', 'Not provided')}

**Contact Information:**
{data.get('contact_info', 'Not provided')}

**Additional Notes:**
{data.get('additional_notes', 'None')}

---

Please create a compelling, professional brochure with the following structure:

1. **Cover Section** - Eye-catching headline and tagline
2. **About Us** - Engaging company story and background
3. **What We Do** - Clear description of products/services with benefits
4. **Our Mission & Vision** - Inspiring statements about purpose and future
5. **Why Choose Us** - Key differentiators and unique value propositions
6. **Who We Serve** - Target audience and how we help them
7. **Get In Touch** - Contact information and call-to-action

Use professional, persuasive language. Make it engaging and reader-friendly. Format in clean markdown with proper headings and sections. Include relevant emojis where appropriate to make it more visually appealing.
"""
        return prompt
    
    def save_brochure(self, content: str, filename: str = None) -> str:
        """
        Save brochure content to a file
        
        Args:
            content: Brochure content to save
            filename: Output filename (auto-generated if None)
            
        Returns:
            Path to saved file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"brochure_{timestamp}.md"
        
        output_path = Path("/home/fragello/ME/Github/Learning/LlmAssistantApi/Projects_All/week_1_day_5") / filename
        output_path.write_text(content, encoding='utf-8')
        
        return str(output_path)


def get_interactive_input() -> dict:
    """Get company information interactively from user"""
    
    print("\n" + "="*60)
    print("🎨 AI COMPANY BROCHURE GENERATOR")
    print("="*60 + "\n")
    
    print("Please provide your company information:\n")
    
    company_data = {}
    
    # Basic Information
    company_data['company_name'] = input("Company Name: ").strip()
    company_data['industry'] = input("Industry: ").strip()
    company_data['founded'] = input("Founded (year): ").strip()
    company_data['location'] = input("Location: ").strip()
    
    print("\n--- Detailed Information ---\n")
    
    # About
    print("About your company (press Enter twice when done):")
    about_lines = []
    while True:
        line = input()
        if line == "":
            if about_lines and about_lines[-1] == "":
                about_lines.pop()
                break
        about_lines.append(line)
    company_data['about'] = "\n".join(about_lines)
    
    # Products/Services
    print("\nProducts/Services (press Enter twice when done):")
    products_lines = []
    while True:
        line = input()
        if line == "":
            if products_lines and products_lines[-1] == "":
                products_lines.pop()
                break
        products_lines.append(line)
    company_data['products_services'] = "\n".join(products_lines)
    
    # Mission & Vision
    print("\nMission & Vision (press Enter twice when done):")
    mission_lines = []
    while True:
        line = input()
        if line == "":
            if mission_lines and mission_lines[-1] == "":
                mission_lines.pop()
                break
        mission_lines.append(line)
    company_data['mission_vision'] = "\n".join(mission_lines)
    
    # Key Differentiators
    print("\nKey Differentiators (what makes you unique, press Enter twice when done):")
    diff_lines = []
    while True:
        line = input()
        if line == "":
            if diff_lines and diff_lines[-1] == "":
                diff_lines.pop()
                break
        diff_lines.append(line)
    company_data['differentiators'] = "\n".join(diff_lines)
    
    # Target Audience
    company_data['target_audience'] = input("\nTarget Audience: ").strip()
    
    # Contact Information
    company_data['contact_info'] = input("Contact Information (email, phone, website): ").strip()
    
    # Additional Notes
    company_data['additional_notes'] = input("Additional Notes (optional): ").strip()
    
    return company_data


def use_example_data() -> dict:
    """Return example company data for testing"""
    return {
        'company_name': 'TechVision AI',
        'industry': 'Artificial Intelligence & Machine Learning',
        'founded': '2020',
        'location': 'San Francisco, CA',
        'about': '''TechVision AI is a cutting-edge artificial intelligence company dedicated to transforming 
how businesses leverage data and automation. Founded by a team of PhD researchers and industry veterans, 
we combine deep technical expertise with practical business understanding to deliver AI solutions that 
actually work in the real world.''',
        'products_services': '''- Custom AI Model Development
- Machine Learning Consulting
- Natural Language Processing Solutions
- Computer Vision Systems
- AI Strategy & Implementation
- Training & Workshops''',
        'mission_vision': '''Mission: To democratize AI technology and make it accessible to businesses of all sizes.
Vision: A world where every organization can harness the power of AI to solve their unique challenges.''',
        'differentiators': '''- PhD-level expertise with 50+ years combined experience
- Focus on explainable and ethical AI
- Proven track record with Fortune 500 clients
- Rapid prototyping and deployment
- Ongoing support and optimization''',
        'target_audience': 'Mid to large-size enterprises looking to implement AI solutions, startups seeking competitive advantage through AI',
        'contact_info': 'Email: hello@techvision.ai | Phone: (415) 555-0123 | Website: www.techvision.ai',
        'additional_notes': 'Emphasize our commitment to ethical AI and transparency'
    }


def main():
    """Main execution function"""
    
    print("\n" + "="*60)
    print("🎨 AI COMPANY BROCHURE GENERATOR")
    print("="*60 + "\n")
    
    # Check for API key
    print("Checking for Anthropic API key...")
    try:
        generator = BrochureGenerator()
        print("✓ API key found\n")
    except Exception as e:
        print("\n❌ ERROR: Anthropic API key not found!")
        print("Please set your ANTHROPIC_API_KEY environment variable:")
        print("  export ANTHROPIC_API_KEY='your-api-key-here'")
        print("\nOr pass it when initializing BrochureGenerator(api_key='your-key')")
        sys.exit(1)
    
    # Choose input method
    print("How would you like to provide company information?")
    print("1. Interactive input")
    print("2. Use example data (TechVision AI)")
    print("3. Load from JSON file")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    if choice == "1":
        company_data = get_interactive_input()
    elif choice == "2":
        print("\nUsing example data for TechVision AI...")
        company_data = use_example_data()
    elif choice == "3":
        json_path = input("Enter path to JSON file: ").strip()
        try:
            with open(json_path, 'r') as f:
                company_data = json.load(f)
            print(f"✓ Loaded data from {json_path}")
        except Exception as e:
            print(f"❌ Error loading JSON: {e}")
            sys.exit(1)
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)
    
    # Generate brochure
    print("\n" + "="*60)
    try:
        brochure_content = generator.generate_brochure(company_data)
        
        # Save brochure
        output_file = generator.save_brochure(brochure_content)
        
        print(f"\n✅ Brochure generated successfully!")
        print(f"📄 Saved to: {output_file}")
        
        # Display preview
        print("\n" + "="*60)
        print("PREVIEW:")
        print("="*60 + "\n")
        print(brochure_content[:500] + "...\n")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ Error generating brochure: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
