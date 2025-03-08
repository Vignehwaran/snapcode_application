# SnapCode

SnapCode is a Streamlit-based web application that utilizes the **Gemini API** for AI-powered processing and converts images into base64-encoded byte strings.

## Features

- **Gemini API Integration**: Uses Google's Gemini API for AI-powered functionalities.
- **Image Conversion**: Upload an image and convert it to base64-encoded bytes.
- **Streamlit UI**: A user-friendly web interface for seamless interaction.

## Installation

To get started, clone the repository and install the necessary dependencies.

```bash
# Clone the repository
git clone https://github.com/yourusername/snapcode.git
cd snapcode

# Install dependencies
pip install -r requirements.txt
```

## API Key Configuration

Ensure you have access to the Gemini API and set up your API key in an environment variable or directly in the script (not recommended for security reasons).

```bash
export GEMINI_API_KEY="your_api_key_here"
```

## Usage

Run the Streamlit app using the following command:

```bash
streamlit run app.py
```

### Steps:
1. Upload an image.
2. Click the **Convert** button.
3. The base64-encoded bytes will be displayed.

## Example Output

```json
{
  "filename": "image.png",
  "base64_bytes": "iVBORw0KGgoAAAANSUhEUgAA..."
}
```

## Dependencies
- Python 3.8+
- Streamlit
- Requests
- OpenAI API (Gemini API)

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.

---

### Contact
For any questions or support, please reach out via [GitHub Issues](https://github.com/yourusername/snapcode/issues).

