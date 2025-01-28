# Finance Agent Team - Powered by DeepSeek-R1 LLM Model 🧠💼

## Overview
The **Finance Agent Team** is a Streamlit-based application that leverages the **deepseek-r1-distill-llama-70b** model from Groq to provide users with advanced conversational capabilities. This app integrates two specialized agents:

1. **Web Agent**: Searches the web for information using DuckDuckGo.
2. **Finance Agent**: Provides financial data such as stock prices, analyst recommendations, company information, and news using YFinanceTools.

Both agents are backed by Groq's powerful LLM and are designed to deliver accurate and contextual insights.

---

## Key Features
- **Web Search Integration**: The Web Agent fetches real-time information from the web.
- **Financial Data Retrieval**: The Finance Agent delivers comprehensive insights into stocks and companies.
- **Agent Team Collaboration**: Combines the strengths of both agents to answer complex multi-domain queries.
- **SQLite Storage**: Saves conversation history for both agents using SQLite, ensuring context awareness.
- **Streamlit UI**: Clean and interactive user interface for seamless query submission and response visualization.

---

## Installation

### Prerequisites
Ensure you have Python 3.8 or higher installed.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/finance-agent-team.git
   cd finance-agent-team
   ```

2. Install the required Python libraries:
   ```bash
   pip install phi streamlit groq
   ```

3. Set up the Groq API key:
   ```bash
   export GROQ_API_KEY="your_groq_api_key_here"
   ```

---

## Usage

1. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

2. **Interface**:
   - Enter your query in the provided text box.
   - Click **Submit** to receive a detailed response from the agent team.

---

## Technical Details

### Web Agent
- **Role**: Searches the web for real-time information.
- **Tools**: DuckDuckGo.
- **Storage**: Saves conversation history in an SQLite database (`agents.db`).

### Finance Agent
- **Role**: Provides financial insights.
- **Tools**: YFinanceTools (stock prices, analyst recommendations, company information, news).
- **Storage**: Saves conversation history in an SQLite database (`agents.db`).

### Agent Team
- Combines the capabilities of the Web and Finance agents.
- Designed for multi-domain queries with tool call visibility enabled.

---

## Screenshots
### Example Query
- **User Input**: "What is the current stock price of Tesla and the latest news?"
- **Agent Team Response**: 
  - Table displaying Tesla's stock price.
  - Links to the latest news articles about Tesla.

---

## Notes
- The app uses **GroqChat** for conversational AI.
- Ensure the Groq API key is correctly configured.
- SQLite database (`agents.db`) is automatically created to store interaction history.

---

## Future Enhancements
- Add support for additional tools (e.g., weather updates, news summarization).
- Implement user authentication for personalized experiences.
- Expand financial data coverage (e.g., cryptocurrency, global markets).

---

## License
This project is licensed under the **MIT License**.

---

## Contact
For queries or contributions, feel free to reach out:
- **Author**: Siddharth Kharche
- **Email**: siddukharche04@gmail.com
- **GitHub**: [siddharth-Kharche](https://github.com/siddharth-Kharche)
