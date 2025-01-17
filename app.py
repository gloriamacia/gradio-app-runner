import gradio as gr
import requests

def greet(name):
    return "Hello " + name + "!"

def get_cat_image():
    # Fetch JSON response from The Cat API
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    if response.status_code == 200:
        # Extract the URL of the first image in the response
        return response.json()[0]['url']
    return "https://via.placeholder.com/300"  # Fallback image if API fails

# Fetch image before launching the app
initial_cat_image_url = get_cat_image()

with gr.Blocks() as demo:
    # Use the fetched URL as the initial value
    gr.Markdown("# CATS 🐱")
    gr.Markdown("Cats cats cats")
    gr.Image(value=initial_cat_image_url, label="Random Cat", interactive=False)
    name_input = gr.Textbox(label="Enter your cat name")
    output_text = gr.Textbox(label="Output")
    gr.Button("Submit").click(fn=greet, inputs=name_input, outputs=output_text)

demo.launch()
