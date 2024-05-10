# Quote Image Generator with Instagram Bot With Gemini Ai

This project is an Instagram bot that generates images with quotes from famous people and uploads them to your Instagram account. It uses the Google Generative AI API to generate relevant quotes based on the given author's name, and the Python Imaging Library (PIL) to overlay the quote text on a background image.

## Features

- Fetches a random author's name from a list of famous people
- Generates a relevant quote for the chosen author using the Google Generative AI API
- Overlays the quote text on a background image using PIL
- Uploads the final image to your Instagram account

## Prerequisites

- Python 3.x
- Google Generative AI API key
- Instagram account credentials (username and password)
- Required Python packages (listed in the requirements.txt file)

## Installation

1. Clone the repository:

    ```
    https://github.com/shaikhazrath/ai-ig-manager
    ```

3. Install the required packages:

    ```
    pip install -r requirements.txt
    ```

4. Set up the required environment variables:

    - `API_KEY`: Your Google Generative AI API key
    - `IG_USERNAME`: Your Instagram username
    - `IG_PASSWORD`: Your Instagram password

## Usage

1. Ensure that you have a `bg.png` file in the project directory, which will be used as the background image for the quote.
2. Ensure that you have a `Roboto-Medium.ttf` file in the project directory, which will be used as the font for the quote text.
3. Run the `main.py` script:

    ```
    python main.py
    ```

    The script will randomly choose an author's name, generate a quote using the Google Generative AI API, overlay the quote on the background image, and upload the final image to your Instagram account.

## Configuration

You can modify the following settings in the `imageEdit.py` file:

- `text_color`: The color of the quote text (RGB tuple)
- `text_size`: The size of the font used for the quote text
- `padding`: The padding around the quote text
- `line_spacing`: The spacing between lines of the quote text

## Contributing

Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Google Generative AI API
- Python Imaging Library (PIL)
- Instagram API (instagrapi)
