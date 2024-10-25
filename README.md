# ChatMySQL

This project is a **Streamlit** app that allows users to chat with a **MySQL database**. It utilizes **Langchain** for natural language query processing, making it easier to interact with the database using conversational language.

## Demo
![image](https://github.com/user-attachments/assets/e8a2a243-12bb-4b60-8d01-196270a5b903)


## Features

- User-friendly interface built with Streamlit.
- Query MySQL database using natural language.
- Results from the database are fetched and displayed in real-time.
- Langchain integration for natural language processing.

## Database Used
I have used a sample SQL Database called *classicmodels*.
You can get detailed info on the Database (including download link) [here](https://www.mysqltutorial.org/getting-started-with-mysql/mysql-sample-database/).

## Getting Started

### Prerequisites

Before running the app, ensure you have the following installed:

- Python 3.7 or higher
- MySQL Server
- [Langchain](https://github.com/hwchase17/langchain)
- [Streamlit](https://streamlit.io/)
- [Chroma DB](https://github.com/chroma-core/chroma)

You can refer to [requirements.txt](requirements.txt) for all the dependencies.

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/nirbhaypr/ChatMySQL
   cd chat-with-mysql
   ```
2. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your MySQL Database**:

    - Ensure MySQL is installed and running.
    - Configure your database and update the connection settings in [main.py](src/main.py).

4. **Run the Streamlit app**:

   ```bash
   streamlit run main.py
   ```

## File Structure

- main.py: Main file that runs the Streamlit app.
- langchain_code.py: Handles the Langchain logic for processing user queries.
- few_shots.py: Example prompts or few-shot learning cases for Langchain's query handling.

In addition to these you will also need a mysql_db.py file from which you will retrive your MySQL server authorization essentials (username, password, host, and database name), and a .env file for your Groq API key.
You may also add Langchain API key to the .env file if you intend to use [LangSmith](https://www.langchain.com/langsmith).

## How to Use

1. Upload Queries: Input your natural language queries into the text box.
2. Get Responses: The app processes the query using Langchain and retrieves results from the MySQL database.
3. Explore Results: View the processed results directly on the app interface.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
