# Automated TestCase Generator

This project provides a tool to generate detailed testing instructions based on uploaded screenshots and optional context. It uses a multimodal language model to create test cases, which are displayed on the frontend in blocks organized by each screenshot.

## Features

- Upload multiple screenshots and view previews before submission.
- Provide optional context to refine the generated test cases.
- Displays generated test cases for each screenshot in a user-friendly format using Markdown.

<img src="/photos/assignment1.png" width="600px">
<img src="/photos/assignment2.png" width="600px">
<img src="/photos/assignment3.png" width="600px">
<img src="/photos/assignment4.png" width="600px">

## Technologies Used

- **Frontend**: Streamlit
- **Backend**: Python
- **Additional Libraries**:
  - `google-generativeai`: A library to work with Google's generative AI models.
  - `Pillow`: For handling and displaying images.
  - `markdown2`: 

## Installation

### Prerequisites
- **Python 3.10** and **pip** should be installed on your machine.

### Steps

1. **Clone the repository** or download the files.

   ```bash
   git clone https://github.com/sharmatanikesh/ai_assignment

2. **Navigate to the project directory**:

   ```bash
   cd myracle
   ```

3. **(Optional) Create a Virtual Environment**:

   Run the following command to install the necessary npm packages:

   ```bash
    python3 -m venv venv
    source venv/bin/activate
   ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt

   ```

5. **Set up environment variables**:

   Create a .env file in the root of the project and add your Google API key:
    ```bash
   GOOGLE_API_KEY=your_google_api_key_here

   ```
6. **Run the Streamlit application**:

   Start the Streamlit server by running:
    ```bash
   streamlit run app.py

   ```
## Usage

1. Upload multiple screenshots.
2. Optionally, provide some context related to the screenshots.
3. Click the Generate Test Instructions button.
4. The generated test cases for each screenshot will be displayed in the output   section.

## Dependencies

- **Streamlit**: For the frontend interface.
- **google-generativeai**: To work with Google's generative AI models.
- **Pillow**: To handle and display images.
- **python-dotenv**: To manage environment variables.



