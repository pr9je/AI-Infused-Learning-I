# AI-Infused Learning 🚀

A hands-on repository for learning and building applications with **Artificial Intelligence, Large Language Models (LLMs), Python, and Generative AI APIs**.

This project documents my practical journey in AI/ML through coding exercises, API integrations, and interactive AI applications.

## 🎯 Project Objectives

- Develop practical experience integrating LLMs into Python applications.
- Explore model responses and compare different language models.
- Build AI-powered applications using API integrations.
- Learn web scraping, text extraction, summarization, and interactive UI development.
- Practice Python development, environment configuration, and Git/GitHub workflows.

## ✨ Projects and Features

### 1. LLM Arena — AI Model Comparison

An interactive application built with Gradio that sends the same prompt to two language models and displays their responses side by side.

**Features**
- Compare responses from different LLMs using a common prompt.
- Integrate models through Groq's OpenAI-compatible API.
- Display responses in a web-based interface.
- Collect user feedback through voting buttons.

**Models configured**
- GPT-OSS 120B
- Qwen model configured in the application

### 2. Website Content Extraction and Summarization

A Python-based workflow for retrieving website content and preparing it for AI-powered summarization.

**Features**
- Fetch webpage HTML using `requests`.
- Parse HTML using BeautifulSoup.
- Extract page titles and readable text.
- Prepare website content for an LLM summarization workflow.

### 3. LLM API Integration

Hands-on practice connecting Python applications to language models using API clients.

**Concepts explored**
- API authentication and environment variables
- Chat completions and message roles
- Model selection and API parameters
- Error handling and dependency management
- Secure API key configuration

## 🛠️ Technology Stack

- **Language:** Python
- **LLM integration:** OpenAI Python SDK, Groq API
- **Interface:** Gradio
- **Web scraping:** Requests, BeautifulSoup
- **Configuration:** python-dotenv
- **Version control:** Git and GitHub

## ⚙️ Getting Started

### Prerequisites

- Python installed on your system
- Git
- A Groq API key
- An OpenAI API key only if you use OpenAI-hosted models

### 1. Clone the repository

```bash
git clone https://github.com/pr9je/AI-Infused-Learning-I.git
cd AI-Infused-Learning-I
```

### 2. Install dependencies

```bash
python -m pip install --upgrade openai gradio python-dotenv requests beautifulsoup4
```

### 3. Configure environment variables

Create a `.env` file in the project root:

```dotenv
GROQ_API_KEY=your_groq_api_key
```

Add `OPENAI_API_KEY` only if a script calls the OpenAI API directly.

### 4. Run the application

If your Gradio application is saved as `app.py`:

```bash
python app.py
```

Open the local URL displayed in your terminal.

**Note:** The application filename and model IDs must match the files and models available in your local setup and API provider account.

## 🔐 Security

- Keep API keys in environment variables.
- Never commit `.env` files or API keys to GitHub.
- Add `.env`, `__pycache__/`, and `*.pyc` to `.gitignore`.
- Rotate any API key that has been exposed publicly.

## 📚 What I'm Learning

This repository is part of my ongoing learning journey in AI and Machine Learning, with an emphasis on practical implementation, LLM integration, and building interactive AI applications.

## 👨‍💻 Author

**Mitesh Prajapati**

MSc in Artificial Intelligence and Machine Learning

GitHub: https://github.com/pr9je

---

If you find this project useful, feel free to explore the repository and share feedback.
