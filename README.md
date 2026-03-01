# Image Background Remover

A simple web application built with Flask that allows users to upload images and automatically remove their backgrounds.

## Tech Stack

*   **Language**: Python
*   **Framework**: Flask
*   **Key Libraries**:
    *   `rembg`: For intelligent background removal.
    *   `Pillow` (PIL): For image processing and manipulation.

## Project Structure

```
.
├── app.py
├── static/
│   └── uploads/
└── templates/
    ├── about.html
    ├── index.html
    └── result.html
```

## Key Features

*   Upload images through a web interface.
*   Automatic background removal from uploaded images.
*   Display of original and processed images.
*   Download processed images with transparent backgrounds.

## API Endpoints

*   **GET `/`**
    *   Renders the main page where users can upload images.
*   **GET `/about`**
    *   Renders the about page.
*   **POST `/remove`**
    *   Accepts an image file for background removal.
    *   Processes the image and saves the output.
    *   Returns a page displaying the original and background-removed images.
*   **GET `/download/<filename>`**
    *   Initiates a download for the specified processed image file.

## Setup Instructions

### Installation

1.  Clone the repository (if applicable, or create the files as above).
2.  Navigate to the project directory.
3.  Install the required Python packages:

    ```bash
    pip install Flask rembg Pillow
    ```

### How to Run Locally

1.  Ensure all dependencies are installed.
2.  Run the Flask application:

    ```bash
    python app.py
    ```
3.  Open your web browser and navigate to `http://127.0.0.1:5000`.
