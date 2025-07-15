from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="Document_loader/diabetes.csv")

doc = loader.load()

print(len(doc))

print("====================================")
print(doc[0].page_content)

print("====================================")
print(doc[87].metadata)  # Display metadata of the first document

