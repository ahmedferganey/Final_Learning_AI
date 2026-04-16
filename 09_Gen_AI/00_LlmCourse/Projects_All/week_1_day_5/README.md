# 🎨 AI Company Brochure Generator

A Python application that uses Claude AI to generate professional, engaging company brochures automatically.

## Features

- 🤖 **AI-Powered Content**: Uses Claude Sonnet 4 to generate compelling brochure copy
- 📝 **Interactive Input**: Step-by-step data collection for your company
- 📄 **Example Data**: Test with pre-loaded sample company data
- 📦 **JSON Support**: Load company data from JSON files
- 💾 **Auto-Save**: Automatically saves brochures in markdown format
- 🎯 **Professional Structure**: Creates well-organized, marketing-ready brochures

## Installation

1. **Install Python dependencies**:
```bash
pip install -r requirements.txt
```

2. **Set up your Anthropic API key**:
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

Or add it to your `.bashrc` or `.zshrc` for persistence.

## Usage

### Basic Usage

Run the script:
```bash
python brochure_generator.py
```

You'll be prompted to choose an input method:
1. **Interactive input** - Enter company information step by step
2. **Example data** - Use pre-loaded TechVision AI sample data
3. **JSON file** - Load data from a JSON file

### Using JSON Input

1. Copy and customize the template:
```bash
cp company_template.json my_company.json
# Edit my_company.json with your company information
```

2. Run with your JSON file:
```bash
python brochure_generator.py
# Choose option 3, then enter: my_company.json
```

### JSON Template Structure

```json
{
  "company_name": "Your Company Name",
  "industry": "Your Industry",
  "founded": "2024",
  "location": "City, Country",
  "about": "Company description and history",
  "products_services": "List of products/services",
  "mission_vision": "Mission and vision statements",
  "differentiators": "What makes you unique",
  "target_audience": "Who you serve",
  "contact_info": "Contact details",
  "additional_notes": "Special notes or emphasis"
}
```

## Programmatic Usage

You can also use the `BrochureGenerator` class in your own Python code:

```python
from brochure_generator import BrochureGenerator

# Initialize generator
generator = BrochureGenerator(api_key='your-api-key')

# Prepare company data
company_data = {
    'company_name': 'TechCorp',
    'industry': 'Technology',
    'founded': '2020',
    # ... other fields
}

# Generate brochure
brochure = generator.generate_brochure(company_data)

# Save to file
output_path = generator.save_brochure(brochure, 'techcorp_brochure.md')
print(f"Brochure saved to: {output_path}")
```

## Output

The generated brochure includes:

1. **Cover Section** - Eye-catching headline and tagline
2. **About Us** - Company story and background
3. **What We Do** - Products/services with benefits
4. **Mission & Vision** - Purpose and future goals
5. **Why Choose Us** - Key differentiators
6. **Who We Serve** - Target audience
7. **Get In Touch** - Contact information and CTA

Output files are saved in markdown format to `/mnt/user-data/outputs/` with timestamps.

## Example Output

When you run with example data, you'll get a professionally formatted brochure for "TechVision AI" - a sample AI company.

## Customization

### Change the AI Model

Edit the `model` parameter in the `BrochureGenerator` class:

```python
self.model = "claude-sonnet-4-20250514"  # Default
# or
self.model = "claude-opus-4-20250514"    # For even better quality
```

### Modify the Prompt

Edit the `_build_prompt()` method to customize the structure, tone, or sections of the generated brochure.

### Adjust Token Limit

Change `max_tokens` in the `generate_brochure()` method:

```python
max_tokens=4000  # Default, increase for longer brochures
```

## Requirements

- Python 3.7+
- anthropic library (>=0.18.0)
- Valid Anthropic API key

## Troubleshooting

### "API key not found" Error

Make sure you've set the `ANTHROPIC_API_KEY` environment variable:
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

### Import Errors

Install dependencies:
```bash
pip install -r requirements.txt
```

### Empty or Short Brochures

Try increasing the `max_tokens` parameter or providing more detailed company information.

## License

MIT License - feel free to modify and use for your projects!

## Tips for Best Results

1. **Be Detailed**: Provide comprehensive information about your company
2. **Be Specific**: Include concrete examples and numbers when possible
3. **Target Audience**: Clearly define who you're trying to reach
4. **Differentiators**: Explain what truly makes you unique
5. **Review & Edit**: The AI generates a draft - refine it to match your brand voice

---

Built with ❤️ using Claude AI by Anthropic
