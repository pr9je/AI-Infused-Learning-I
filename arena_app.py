
# Install dependencies:
# python -m pip install openai gradio python-dotenv

import os
import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Read Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq client
groq_client = (
    OpenAI(
        api_key=GROQ_API_KEY,
        base_url="https://api.groq.com/openai/v1"
    )
    if GROQ_API_KEY
    else None
)


def ask(client, model, prompt):
    """Send a prompt to a model and return its answer."""

    if client is None:
        return "Error: GROQ_API_KEY is missing. Check your .env file."

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=1024
        )

        return (
            response.choices[0].message.content
            or "The model returned an empty response."
        )

    except Exception as e:
        return f"Error calling {model}: {str(e)}"


def battle(prompt):
    """Compare two models using the same prompt."""

    if not prompt or not prompt.strip():
        message = "Please enter a prompt before starting the battle."
        return message, message

    # Model A: GPT-OSS 120B
    answer_a = ask(
        groq_client,
        "openai/gpt-oss-120b",
        prompt
    )

    # Model B: Qwen 3.8 27B
    answer_b = ask(
        groq_client,
        "qwen/qwen3.8-27b",
        prompt
    )

    return answer_a, answer_b


def vote(label):
    """Display the user's vote."""

    return f"🗳️ Thanks for voting: **{label}**"


# Build Gradio interface
with gr.Blocks(title="LLM Arena") as demo:

    gr.Markdown(
        """
        # 🥊 LLM Arena
        ### Compare two AI models using the same prompt

        Ask a question and compare their responses side by side.
        """
    )

    prompt = gr.Textbox(
        label="Your prompt",
        placeholder="For example: Explain gradient descent with an example.",
        lines=4
    )

    go = gr.Button("⚔️ Battle!", variant="primary")

    with gr.Row():

        # Model A
        with gr.Column():
            gr.Markdown("### 🤖 Model A — GPT-OSS 120B")

            out_a = gr.Markdown(
                "Model A's response will appear here."
            )

            with gr.Row():
                up_a = gr.Button("👍 Vote A")
                down_a = gr.Button("👎 Vote A")

        # Model B
        with gr.Column():
            gr.Markdown("### 🤖 Model B — Qwen 3.8 27B")

            out_b = gr.Markdown(
                "Model B's response will appear here."
            )

            with gr.Row():
                up_b = gr.Button("👍 Vote B")
                down_b = gr.Button("👎 Vote B")

    verdict = gr.Markdown()

    # Run both models
    go.click(
        fn=battle,
        inputs=[prompt],
        outputs=[out_a, out_b]
    )

    # Voting buttons
    up_a.click(
        fn=lambda: vote("👍 Model A — GPT-OSS 120B"),
        outputs=[verdict]
    )

    down_a.click(
        fn=lambda: vote("👎 Model A — GPT-OSS 120B"),
        outputs=[verdict]
    )

    up_b.click(
        fn=lambda: vote("👍 Model B — Qwen 3.8 27B"),
        outputs=[verdict]
    )

    down_b.click(
        fn=lambda: vote("👎 Model B — Qwen 3.8 27B"),
        outputs=[verdict]
    )


# Launch the application locally
if __name__ == "__main__":
    demo.launch()
