# Thread Chatbot

A document analysis system that uses CrewAI to analyze different types of documents (sales, HR, finance, marketing) and answer questions based on their content.

## Features

- Sequential document analysis workflow
- Specialized agents for different document types
- Automatic document type selection based on content
- Clean, minimal user interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ashishm61/thread_chatbot.git
cd thread_chatbot
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
Create a `.env` file with your API keys:
```
OPENAI_API_KEY=your_openai_api_key
```

## Usage

Run the main script:
```bash
python main.py
```

The chatbot will prompt you to ask questions about your documents. It will sequentially search through sales, HR, finance, and marketing documents to find relevant information.

## Document Structure

Place your document text files in the appropriate folders:
- `documents/sales/` - For sales reports
- `documents/hr/` - For HR reports
- `documents/finance/` - For finance reports
- `documents/marketing/` - For marketing reports
