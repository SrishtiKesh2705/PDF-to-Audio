from pypdf import PdfReader
from pathlib import Path
from google.cloud import texttospeech

reader=PdfReader("Data/sample_pdf.pdf")
no_of_pages=(len(reader.pages))

with open("conversion.txt", "w", encoding="utf-8") as file:
    for i in range(0,no_of_pages):
        page=reader.pages[i]
        file.write(page.extract_text())
        file.write("\n")

file_content=Path('conversion.txt').read_text(encoding="utf-8")
file_content=file_content.replace('\n',' ')

def synthesize_text():

    client = texttospeech.TextToSpeechClient()

    # Keep each request safely below Google's 5000-byte limit
    max_bytes = 4500

    chunks = []
    current_chunk = ""

    # Split roughly at words rather than cutting words in half
    for word in file_content.split():
        test_chunk = current_chunk + " " + word

        if len(test_chunk.encode("utf-8")) > max_bytes:
            chunks.append(current_chunk)
            current_chunk = word
        else:
            current_chunk = test_chunk

    if current_chunk:
        chunks.append(current_chunk)

    print(f"Text split into {len(chunks)} chunks.")

    output_folder = Path("output")
    output_folder.mkdir(exist_ok=True)

    for i, chunk in enumerate(chunks):

        input_text = texttospeech.SynthesisInput(text=chunk)

        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Chirp3-HD-Charon",
        )

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        response = client.synthesize_speech(
            input=input_text,
            voice=voice,
            audio_config=audio_config,
        )

        filename = output_folder / f"output_{i + 1}.mp3"

        with open(filename, "wb") as out:
            out.write(response.audio_content)

        print(f"Created {filename}")


synthesize_text()