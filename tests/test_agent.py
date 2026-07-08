import unittest
from types import SimpleNamespace
from unittest.mock import patch

import agent


class FakeRetriever:
    def __init__(self, docs):
        self.docs = docs

    def invoke(self, question):
        return self.docs


class FakeRAGPipeline:
    def __init__(self):
        self.received_docs = None
        self.received_question = None

    def generate_answer(self, retrieved_docs, question):
        self.received_docs = retrieved_docs
        self.received_question = question
        return "answer", [SimpleNamespace(page_content="context")]


class DocumentSearchToolTests(unittest.TestCase):
    def test_search_invokes_retriever_and_passes_documents(self):
        fake_retriever = FakeRetriever([SimpleNamespace(page_content="chunk")])
        fake_pipeline = FakeRAGPipeline()

        with patch("agent.RAGPipeline", return_value=fake_pipeline):
            tool = agent.DocumentSearchTool(fake_retriever)
            result = tool.search("What is this?")

        self.assertEqual(result["answer"], "answer")
        self.assertEqual(fake_pipeline.received_question, "What is this?")
        self.assertEqual(fake_pipeline.received_docs, fake_retriever.docs)


if __name__ == "__main__":
    unittest.main()
