from langchain_community.document_loaders import WebBaseLoader
import os
os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

url ="https://datatalks.club/blog/guide-to-free-online-courses-at-datatalks-club.html"
loader = WebBaseLoader(url)

doc = loader.load()

print(doc[0].page_content)
print("====================================")
print(len(doc))