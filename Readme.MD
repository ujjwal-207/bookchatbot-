# 📚 BookChatBot 🤖

An intelligent chatbot that allows users to have interactive conversations about books using AI-powered natural language processing.

## ✨ Features

- **Book Conversations**: Chat with an AI about any book from a pre-loaded library
- **Context-Aware Responses**: The bot uses information from the book to provide accurate answers
- **File Upload**: Support for uploading new books in PDF format
- **Vector Database**: Efficient storage and retrieval of book content using Pinecone

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **AI/ML**: Google Generative AI (Gemini)
- **Vector Database**: Pinecone
- **NLP Framework**: LangChain
- **Document Processing**: PyPDF2, LangChain document loaders
- **Text Chunking**: LangChain text splitters
- **Frontend**: HTML, CSS, JavaScript

## 🔧 Installation

1. Clone the repository:
   ```
   git clone https://github.com/ujjwal-207/bookchatbot.git
   cd bookchatbot
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory with the following:
   ```
   GOOGLE_API_KEY=your_google_api_key
   PINECONE_API_KEY=your_pinecone_api_key
   PINECONE_ENVIRONMENT=your_pinecone_environment
   INDEX_NAME=your_pinecone_index_name
   ```

## 🚀 Usage

1. Run the Flask application:
   ```
   python app.py
   ```


## 🧠 How It Works

1. **Document Processing**: Books are processed and chunked into smaller segments
2. **Vector Embedding**: Text chunks are converted to vector embeddings using Google's embedding model
3. **Storage**: Embeddings are stored in Pinecone's vector database
4. **Retrieval**: When a user asks a question, the system:
   - Converts the query to an embedding
   - Finds similar vectors in Pinecone
   - Retrieves relevant text chunks
5. **Response Generation**: The retrieved context is passed to Google's Gemini model along with the query to generate a contextually relevant response


## 🔍 Future Improvements

- Add user authentication
- Support more file formats (EPUB, MOBI, etc.)
- Implement conversation history
- Add multi-language support
- Improve similarity search with metadata filtering

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

- **Ujjwal**
- GitHub: [ujjwal-207](https://github.com/ujjwal-207)

## 🙏 Acknowledgements

- Google Generative AI for providing the AI capabilities
- Pinecone for vector database services
- LangChain for the NLP framework