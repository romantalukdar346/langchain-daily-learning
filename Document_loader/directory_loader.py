from langchain_community.document_loaders import DirectoryLoader, PyMuPDFLoader, PyPDFLoader
import time

loder = DirectoryLoader(path="Document_loader",
                        glob="*.pdf",
                        loader_cls=PyMuPDFLoader)

doc = loder.lazy_load()
start= time.time()
for document in doc:
    # print(document.metadata)
    print("====================================")
end = time.time()
print(f"Time taken to load documents: {end - start} seconds")