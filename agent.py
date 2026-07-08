try:
    from langchain_core.tools import Tool
except ImportError:  # Fallback for older LangChain versions
    from langchain.tools import Tool

from rag import RAGPipeline


class DocumentSearchTool:

    def __init__(self, retriever):
        self.retriever = retriever
        self.rag_pipeline = RAGPipeline()

    def _get_documents(self, question: str):
        if self.retriever is None:
            return []

        if hasattr(self.retriever, "invoke"):
            documents = self.retriever.invoke(question)
        elif callable(self.retriever):
            documents = self.retriever(question)
        else:
            documents = self.retriever

        if documents is None:
            return []

        if hasattr(documents, "page_content"):
            return [documents]

        return list(documents)

    def search(self, question: str):

        documents = self._get_documents(question)
        result = self.rag_pipeline.generate_answer(
            documents,
            question
        )

        if isinstance(result, tuple):
            answer = result[0]
            sources = result[1] if len(result) > 1 else documents
        else:
            answer = result
            sources = documents

        return {
            "answer": answer,
            "sources": sources
        }

    def get_tool(self):

        return Tool(
            name="Document Search",
            description=(
                "Search the uploaded documents and answer questions "
                "using the document context."
            ),
            func=self.search,
        )


class AIAgent:

    def __init__(self, tools):
        self.tools = {tool.name: tool for tool in tools}

    def ask(self, question: str):

        # Decision Layer
        # Today we have only one tool.
        # Later this can route to SQL, Web Search, Calculator, etc.

        document_tool = self.tools["Document Search"]

        return document_tool.func(question)