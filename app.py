import gradio as gr
import requests
import os 

def greet(name):
    return "¡Pspspsps, " + name + "! ¡Sus leales súbditos humanos requieren su presencia!"

def get_cat_image():
    # Fetch JSON response from The Cat API
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    if response.status_code == 200:
        # Extract the URL of the first image in the response
        return response.json()[0]['url']

# Fetch image before launching the app
initial_cat_image_url = get_cat_image()

# URL of the GIF
gif_url = "./assets/cat.gif" 

# LinkedIn Button HTML
linkedin_button_html = """
<style>
    .libutton {
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 7px;
        text-align: center;
        outline: none;
        text-decoration: none !important;
        color: #ffffff !important;
        width: 200px;
        height: 32px;
        border-radius: 16px;
        background-color: #0A66C2;
        font-family: "SF Pro Text", Helvetica, sans-serif;
    }
</style>
<a class="libutton" href="https://www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=gloriamacia" target="_blank">Sígueme en LinkedIn</a>
"""

with gr.Blocks(theme=gr.themes.Ocean()) as demo:
    with gr.Tab("App"):
        gr.Markdown("# <div style='text-align: center;'>👑 Ronroneros 🐱</div>")
        gr.Markdown("Gatos, gatos, gatos y más gatos!")
        gr.Image(value=initial_cat_image_url, label="Random Cat", interactive=False)
        with gr.Row():
            with gr.Column(scale=1):
                name_input = gr.Textbox(label="Da nombre al gato")
                output_text = gr.Textbox(label="Output")
                gr.Button("Submit").click(fn=greet, inputs=name_input, outputs=output_text)
            with gr.Column(scale=1):
                # Embed the GIF
                gr.Image(value=gif_url, show_download_button=False, show_label=False, container=False, show_fullscreen_button=False, interactive=False, format="gif")
    with gr.Tab("El Proyecto"):
        gr.Markdown("# Hola! Soy Gloria") 
        gr.HTML(linkedin_button_html)  # Add LinkedIn Button
        gr.Markdown("### De qué va este proyecto?")
        gr.HTML("""<iframe src="https://www.linkedin.com/embed/feed/update/urn:li:share:7281651711541198848" height="916" width="504" frameborder="0" allowfullscreen="" title="Embedded post"></iframe>""")

demo.launch()
