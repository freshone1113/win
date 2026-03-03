 Before running the code, ensure the following key dependencies are installed—they support core
 functionalities like environment management, API deployment, UI rendering, and vector retrieval:
 conda: For creating and activating the project environment
 uvicorn: To run the RAG API backend
 npm: For managing and launching the frontend UI
 docker: To start containerized services
 pymilvus==2.6.3: Integrates the Milvus Lite vector database for legal text storage and retrieval
 langchain: Enables document processing, chunking, and retrieval chain development
 pdfplumber: Extracts text and validates Hong Kong legal PDFs
 jieba: Used for Chinese keyword extraction in legal document standardization
 2.Step-by-Step Code Execution
（1）Activate the Conda Environment
 First, launch the dedicated project environment to ensure dependency consistency.
（2）Runthe RAGAPIBackend
 Navigate to the API directory and start the backend service (auto-reloads on code changes):
 cd poc/demo
 uvicorn rag_api:app--reload--host 127.0.0.1--port 8000
（3） LaunchtheFrontend UI
Open a new terminal, move to the UI folder, and start the development server:
 cd ui
 npm run dev
（4）Start Docker Services
 Open Docker, then use PowerShell to navigate to the project directory and launch containerized
 services:
 docker-compose up-d
（5）Access the System
 Open a browser and visit the frontend interface to use the legal query tool:
 http://localhost:5173/law-query
 That's it! You have successfully set up and launched the Hong Kong Legal Q&A System. Now you
 can freely input legal inquiries, and the system will leverage RAG technology and the Milvus vector
 database to provide accurate and efficient responses based on Hong Kong legal documents.

