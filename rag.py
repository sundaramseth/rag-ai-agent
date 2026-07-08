
from langchain_text_splitters import RecursiveCharacterTextSplitter
#for semmentic chunking
# from langchain_experimental.text_splitter import SemmanticChunker
# from langchain.openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from prompts import RAG_PROMPT
from llm import llm


class RAGPipeline:

    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=400,
            chunk_overlap=200,
            separators=[
                "\n\n",
                "\n",
                ".",
                " ",
                ""
            ]
        )

        self.prompt = PromptTemplate.from_template(RAG_PROMPT)
        self.parser = StrOutputParser()

        self.chain = self.prompt | llm | self.parser

    def chunk_documents(self, documents):
        return self.text_splitter.split_documents(documents)

    def generate_answer(self, retrieved_docs, question):

        context = "\n\n".join(
            doc.page_content for doc in retrieved_docs
        )

        answer = self.chain.invoke(
            {
                "context": context,
                "question": question
            }
        )

        return answer