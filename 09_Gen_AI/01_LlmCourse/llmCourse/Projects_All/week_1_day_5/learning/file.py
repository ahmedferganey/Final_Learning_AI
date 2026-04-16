from click import prompt

import anthropic
import json
import sys
import os
from datetime import datetime
from pathlib import Path
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")


class BrochureGenerator:
    def __init__(self, api_key: str):
        self.client = Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-6"


    def generate_brochure(self, company_data: dict) -> str:
        prompt - self._build_prompt(company_data)

        print("Generating brochure...")

        message = self.client.messages.create(
            model=self.model,
            max_tokens=4000,
            messages=[{
                "role" : "user",
                "content" : prompt
                }
            ]
        )

        brocher_content = message.content[0].text
        return brocher_content
    

    def _build_prompt(self, data: dict) -> str:
        prompt = f"""
        You are a marketing expert tasked with creating a compelling brochure for a company. 
        Use the following information about the company to craft an engaging and informative brochure.

        Company Name: {data.get('company_name', 'N/A')}
        Industry: {data.get('industry', 'N/A')}
        Products/Services: {data.get('products_services', 'N/A')}
        Unique Selling Points: {data.get('unique_selling_points', 'N/A')}
        Target Audience: {data.get('target_audience', 'N/A')}
        Contact Information: {data.get('contact_information', 'N/A')}

        Please create a brochure that highlights the company's strengths and appeals to its target audience.
        """
        return prompt   
    
    def save_brochure(self, content: str, filename: str = None) -> str:
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"brochure_{timestamp}.md"

        output_path = Path("/home/fragello/ME/Github/Learning/LlmAssistantApi/Projects_All/week_1_day_5") / filename
        output_path.write_text(content, encoding='utf-8')

        return str(output_path)
    

    