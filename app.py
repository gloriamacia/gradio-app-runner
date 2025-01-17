import gradio as gr
from diffusers import StableDiffusionPipeline
import torch
import spaces

# Load the Stable Diffusion pipeline
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")

# Automatically move the pipeline to CUDA if available
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe.to(device)

# Define the image generation function
@spaces.GPU
def generate(prompt: str):
    image = pipe(prompt).images[0]
    return image

# Gradio Interface
interface = gr.Interface(
    fn=generate,
    inputs=gr.Textbox(label="Enter your text prompt"),
    outputs=gr.Image(label="Generated Image"),
    title="Stable Diffusion Generator",
    description="Generate images from text using Stable Diffusion. Automatically uses GPU if available!"
)

if __name__ == "__main__":
    interface.launch()
