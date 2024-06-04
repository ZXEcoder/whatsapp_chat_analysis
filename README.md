# WhatsApp Chat Analysis

Welcome to the WhatsApp Chat Analysis project! This repository hosts a tool that allows you to analyze your WhatsApp group chat data. By using this tool, you can generate a comprehensive report of your group chat activities and visualize the data in various insightful ways.

## Features

- **Upload WhatsApp Chat Data**: Easily upload your exported WhatsApp group chat text file.
- **Message Analysis**: Get detailed statistics on the number of messages sent by each participant.
- **Word Count**: Analyze the word frequency and identify the most commonly used words.
- **Activity Patterns**: Visualize the chat activity over time to identify trends and patterns.
- **Interactive Visualizations**: Explore your chat data through interactive graphs and charts.

## Getting Started

### Prerequisites

- Python 3.7+
- Streamlit
- pandas
- matplotlib
- wordcloud

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/whatsapp_chat_analysis.git
    cd whatsapp_chat_analysis
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Export your WhatsApp chat data:
   - Open WhatsApp on your phone.
   - Go to the group chat you want to analyze.
   - Tap on the group name to open the group info.
   - Scroll down and select "Export chat".
   - Choose "Without Media" to keep the export file manageable.
   - Save the exported file to your computer.

2. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

3. Open your web browser and go to `http://localhost:8501`.

4. Upload your exported WhatsApp chat text file and start exploring your chat data!

## Project Structure

- `app.py`: Main application script that runs the Streamlit app.
- `chat_analysis.py`: Contains functions for processing and analyzing chat data.
- `visualization.py`: Contains functions for generating visualizations.
- `requirements.txt`: List of required Python packages.
- `sample_chat.txt`: A sample WhatsApp chat text file for testing.

## Contributing

We welcome contributions! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the desire to gain insights from WhatsApp group chats.
- Thanks to the open-source community for the tools and libraries used in this project.

## Live Demo

Check out the live demo of the application [here](https://huggingface.co/spaces/SurajJha21/Whatsapp_chat_analysis).

## Contact

If you have any questions, feel free to reach out:

- GitHub: [yourusername](https://github.com/yourusername)
- Email: youremail@example.com

Enjoy analyzing your WhatsApp group chats! 🚀
