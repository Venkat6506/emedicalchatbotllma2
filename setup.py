from setuptools import find_packages,setup

setup(
    name='Medical Chatbot',
    version='0.0.1',
    author='Satyaprakash Nayak',
    author_email='n.satyaprakash@yahoo.com',
    packages=find_packages(),
    install_requires=["ctransformers","sentence-transformers","langchain","langchain_community","flask","huggingface_hub","PyPDF","chromadb","openai"]
)