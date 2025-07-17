

from langchain_community.document_loaders import (
    PyPDFLoader,
    WebBaseLoader,
    WikipediaLoader,
    YoutubeLoader
)

# Load PDF documenT
def load_pdf(path):
    try:
        loader = PyPDFLoader(path)
        documents = loader.load()
        print(f"Loaded {len(documents)} pages from PDF.")
        return documents
    except Exception as e:
        print(f"Error loading PDF: {e}")
        return []

# Load website content
def load_web(url):
    try:
        loader = WebBaseLoader(url)
        documents = loader.load()
        print(f"Loaded content from website: {url}")
        return documents
    except Exception as e:
        print(f"Error loading website: {e}")
        return []

# Load Wikipedia content
def load_wiki(query):
    try:
        loader = WikipediaLoader(query=query, lang="en", load_max_docs=1)
        documents = loader.load()
        print(f"Loaded content from Wikipedia for: {query}")
        return documents
    except Exception as e:
        print(f"Error loading Wikipedia: {e}")
        return []

# Load YouTube transcript
def load_youtube(url):
    try:
        loader = YoutubeLoader.from_youtube_url(url, add_video_info=False)
        documents = loader.load()
        print(f"Loaded transcript from YouTube: {url}")
        return documents
    except Exception as e:
        print(f"Error loading YouTube: {e}")
        return []

# Optional CLI usage
def main():
    print("\nChoose source:\n1. PDF\n2. Website\n3. Wikipedia\n4. YouTube\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        path = input("Enter PDF file path: ")
        docs = load_pdf(path)
    elif choice == '2':
        url = input("Enter website URL: ")
        docs = load_web(url)
    elif choice == '3':
        topic = input("Enter Wikipedia topic: ")
        docs = load_wiki(topic)
    elif choice == '4':
        url = input("Enter YouTube URL: ")
        docs = load_youtube(url)
    else:
        print("Exiting.")
        return

    print("\nPreview of loaded document:\n")
    for i, doc in enumerate(docs[:1]):
        print(doc.page_content[:500])
        print("\n---\n")

if __name__ == "__main__":
    main()
