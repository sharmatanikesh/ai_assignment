# AI ASSIGNMENT

This project provides a tool to generate detailed testing instructions based on uploaded screenshots and optional context. It uses a multimodal language model to create test cases for each functionality, and the results are presented on the frontend in blocks organized by each screenshot. Each block includes the test cases along with the expected results.

## Prompt Strategy
I started by making a general description for the assignment so the prompt could be used in different ways. After refining the prompt a few times, I got better results. I also added options for users to choose the target platform—Android, iOS, or Web—and pick the testing framework they want. This way, the tool can generate code based on their choices. These features are optional, giving users more flexibility without limiting the output.
## Features

- Upload multiple screenshots and view previews before submission.
- Provide optional context to refine the generated test cases.
- Displays generated test cases for each screenshot in a user-friendly format using Markdown.
- Platform Selection and Testing Framework: Users can select the target platform—Android, iOS, or Web. Based on the selection, the tool will provide the relevant testing framework for code generation. This feature is optional, allowing users to tailor the output according to their preferences.

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
  - `python-dotenv`: A library to manage environment variables in `.env` files.

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
    conda create  venv python==3.10
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



