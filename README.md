# PDF to Audiobook Converter

A Python-based application that extracts text from PDF documents and converts it into speech using the Google Cloud Text-to-Speech API.

## Features

- Extracts text from PDF files using `pypdf`
- Converts extracted text into speech using Google Cloud Text-to-Speech
- Splits large documents into smaller chunks to stay within the API's text limit
- Generates MP3 audio files for each text chunk
- Automatically stores generated audio files in an `output` folder
- Supports Unicode text using UTF-8 encoding

## Technologies Used

- **Python 3.12**
- **pypdf** – Used to extract text from PDF documents
- **Google Cloud Text-to-Speech** – Used to convert extracted text into speech
- **pathlib** – Used for file and directory management

## Project Structure

```text
PDF-to-Audiobook/
│
├── Data/
│   └── sample_pdf.pdf
│
├── output/
│   └── Generated MP3 files
│
├── main.py
├── .gitignore
└── README.md
```
  ## Requirements

Before running the project, make sure you have:

- Python 3.12 or later
- A Google Cloud account
- A Google Cloud project
- The Google Cloud Text-to-Speech API enabled
- A Google Cloud service account
- A service account JSON key

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd PDF-to-Audiobook
```

### 2. Install the required Python packages

```bash
pip install pypdf google-cloud-texttospeech
```

### 3. Set up Google Cloud Text-to-Speech

Create a Google Cloud project and enable the **Cloud Text-to-Speech API**.

Create a service account and generate a JSON key for it.

Place the JSON key inside your local project folder.

**Do not upload the JSON key to GitHub.**

Add the JSON filename to `.gitignore`, for example:

```text
google_credentials.json
```

### 4. Set the credentials environment variable

If you are using Git Bash on Windows:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="C:/path/to/your/google_credentials.json"
```

Verify that the variable has been set:

```bash
echo $GOOGLE_APPLICATION_CREDENTIALS
```

### 5. Add a PDF

Place the PDF you want to convert inside the `Data` folder.

For example:

```text
Data/sample_pdf.pdf
```

If your PDF has a different filename or location, update the path in `main.py`.

## Usage

Run the application with:

```bash
python main.py
```
## License

This project is created for educational and personal use.
