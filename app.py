import gradio as gr
from transformers import pipeline

# Load the Whisper model
transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base")

def transcribe_audio(audio):
    if audio is None:
        return "Please upload an audio file."
    transcription = transcriber(audio, generate_kwargs={"language": "es"})
    return transcription["text"]

# Create the Gradio interface
with gr.Blocks() as app:
    gr.Markdown("# 🎤 Audio Transcription App")
    gr.Markdown(
        "Upload an audio file (e.g., Spanish speech) and get the transcription below."
    )

    with gr.Row():
        audio_input = gr.Audio(label="Upload Audio", type="filepath")
        transcription_output = gr.Textbox(
            label="Transcription", placeholder="Transcribed text will appear here.", lines=5
        )

    transcribe_button = gr.Button("Transcribe Audio")
    transcribe_button.click(transcribe_audio, inputs=audio_input, outputs=transcription_output)

    gr.Markdown("---\nMade with ❤️ using Whisper and Gradio.")

# Launch the app
app.launch()
  