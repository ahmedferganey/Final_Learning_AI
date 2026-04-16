# imports
# If these fail, please check you're running from an activated environment

import os
import json
from dotenv import load_dotenv
from IPython.display import Markdown, display, update_display
from scraper import fetch_website_links, fetch_website_contents
from anthropic import Anthropic

# ======================
# Initialize and constants
# ======================

load_dotenv(override=True)
api_key = os.getenv("ANTHROPIC_API_KEY")

if api_key and api_key.startswith("sk-") and len(api_key) > 10:
    print("Anthropic API key looks good so far")
else:
    print("There might be a problem with your Anthropic API key. Please check your .env or environment variables.")

MODEL_LINKS = "claude-haiku-4-5"
MODEL_BROCHURE = "claude-sonnet-4-6"

client = Anthropic(api_key=api_key)

# ======================
# Helpers
# ======================

def extract_text(response) -> str:
    """Extract text safely from Anthropic content blocks."""
    return "\n".join(
        block.text for block in response.content
        if getattr(block, "type", None) == "text"
    ).strip()


# ======================
# Link selection
# ======================

link_system_prompt = """
You are provided with a list of links found on a webpage.
You are able to decide which of the links would be most relevant to include in a brochure about the company,
such as links to an About page, or a Company page, or Careers/Jobs pages.

You must respond with valid JSON only, in this exact shape:

{
  "links": [
    {"type": "about page", "url": "https://full.url/goes/here/about"},
    {"type": "careers page", "url": "https://another.full.url/careers"}
  ]
}

Rules:
- Return only JSON
- Use full https URLs
- Do not include Terms of Service, Privacy, login, signup, or email links
- Prefer company/about, products, customers, team, careers, jobs, mission, culture
"""

def get_links_user_prompt(url: str) -> str:
    user_prompt = f"""
Here is the list of links on the website {url}.
Please decide which of these are relevant web links for a brochure about the company.

Respond with the full https URL in JSON format.
Do not include Terms of Service, Privacy, email links, login pages, or signup pages.

Links (some might be relative links):
"""
    links = fetch_website_links(url)
    user_prompt += "\n".join(links)
    return user_prompt.strip()


def select_relevant_links(url: str) -> dict:
    print(f"Selecting relevant links for {url} by calling {MODEL_LINKS}")

    response = client.messages.create(
        model=MODEL_LINKS,
        max_tokens=1200,
        system=link_system_prompt,
        messages=[
            {"role": "user", "content": get_links_user_prompt(url)}
        ],
    )

    result = extract_text(response)

    try:
        links = json.loads(result)
    except json.JSONDecodeError as e:
        raise ValueError(f"Claude did not return valid JSON.\nRaw response:\n{result}") from e

    print(f"Found {len(links.get('links', []))} relevant links")
    return links


# ======================
# Page aggregation
# ======================

def fetch_page_and_all_relevant_links(url: str) -> str:
    contents = fetch_website_contents(url)
    relevant_links = select_relevant_links(url)

    result = f"## Landing Page:\n\n{contents}\n\n## Relevant Links:\n"

    for link in relevant_links.get("links", []):
        result += f"\n\n### Link: {link['type']}\n"
        result += fetch_website_contents(link["url"])

    return result


# ======================
# Brochure generation
# ======================

brochure_system_prompt = """
You are an assistant that analyzes the contents of several relevant pages from a company website
and creates a short brochure about the company for prospective customers, investors, and recruits.

Respond in markdown without code blocks.
Include details of company culture, customers, products, and careers/jobs if you have the information.
Be accurate and do not invent facts that are not supported by the provided content.
"""

# Humorous variant if needed:
# brochure_system_prompt = """
# You are an assistant that analyzes the contents of several relevant pages from a company website
# and creates a short, humorous, entertaining, witty brochure about the company for prospective customers, investors, and recruits.
# Respond in markdown without code blocks.
# Include details of company culture, customers, and careers/jobs if you have the information.
# Be accurate and do not invent facts that are not supported by the provided content.
# """


def get_brochure_user_prompt(company_name: str, url: str) -> str:
    user_prompt = f"""
You are looking at a company called: {company_name}

Here are the contents of its landing page and other relevant pages.
Use this information to build a short brochure of the company in markdown without code blocks.
"""
    user_prompt += "\n\n" + fetch_page_and_all_relevant_links(url)

    # Truncate to reduce prompt size
    user_prompt = user_prompt[:5000]
    return user_prompt.strip()


def create_brochure(company_name: str, url: str) -> str:
    response = client.messages.create(
        model=MODEL_BROCHURE,
        max_tokens=2000,
        system=brochure_system_prompt,
        messages=[
            {"role": "user", "content": get_brochure_user_prompt(company_name, url)}
        ],
    )

    result = extract_text(response)
    display(Markdown(result))
    return result


def stream_brochure(company_name: str, url: str) -> None:
    with client.messages.stream(
        model=MODEL_BROCHURE,
        max_tokens=2000,
        system=brochure_system_prompt,
        messages=[
            {"role": "user", "content": get_brochure_user_prompt(company_name, url)}
        ],
    ) as stream:
        response = ""
        display_handle = display(Markdown(""), display_id=True)

        for text in stream.text_stream:
            response += text
            update_display(Markdown(response), display_id=display_handle.display_id)


# ======================
# Example usage
# ======================

links = fetch_website_links("https://edwarddonner.com")
print(links)

print(get_links_user_prompt("https://edwarddonner.com"))

selected = select_relevant_links("https://edwarddonner.com")
print(selected)

selected_hf = select_relevant_links("https://huggingface.co")
print(selected_hf)

print(fetch_page_and_all_relevant_links("https://huggingface.co"))

get_brochure_user_prompt("HuggingFace", "https://huggingface.co")

create_brochure("HuggingFace", "https://huggingface.co")
stream_brochure("HuggingFace", "https://huggingface.co")
