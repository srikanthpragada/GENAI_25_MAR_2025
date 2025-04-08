from transformers import pipeline
# Load the TTS pipeline
tts = pipeline("text-to-speech", model="microsoft/speecht5_tts")

# Generate speech
output = tts("Hello from Hugging Face!")

# Save to file
with open("output.wav", "wb") as f:
    f.write(output["audio"])

print("Done!")