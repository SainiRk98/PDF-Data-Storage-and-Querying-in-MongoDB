# Approach 1-store data in previous database and collection
# import pdfplumber
# from pymongo import MongoClient
# import re

# # 1. Connect to MongoDB
# client = MongoClient("mongodb://localhost:27017/")
# db = client["education_agent"]
# collection = db["legal_pdf_data"]

# # 2. Open PDF (updated to your file)
# with pdfplumber.open("road_traffic_rules.pdf") as pdf:
#     for i, page in enumerate(pdf.pages):
#         text = page.extract_text()
#         if text:
#             # Split by sections using regex (numbers or headings)
#             sections = re.split(r"\n\d+\.\s", text)
            
#             for sec in sections:
#                 # Clean lines, remove bullets and extra spaces
#                 lines = [line.strip("• ").strip() for line in sec.split("\n") if line.strip()]
#                 if len(lines) > 1:
#                     doc = {
#                         "section": lines[0],   # First line = heading
#                         "rules": lines[1:],   # Remaining = rules
#                         "page_number": i + 1,
#                         "source": "road_traffic_rules.pdf"
#                     }
#                     collection.insert_one(doc)

# print("✅ Structured PDF data stored in MongoDB like CSV rows")


#approach 2-store in separate databse
import pdfplumber
from pymongo import MongoClient
import re

# 1. Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# ✅ NEW database and collection
db = client["traffic_rules_db"]          # New database for traffic rules
collection = db["road_rules_collection"] # New collection for this PDF

# 2. Open PDF
with pdfplumber.open("road_traffic_rules.pdf") as pdf:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        if text:
            # Split by sections using regex (numbers or headings)
            sections = re.split(r"\n\d+\.\s", text)
            
            for sec in sections:
                # Clean lines, remove bullets and extra spaces
                lines = [line.strip("• ").strip() for line in sec.split("\n") if line.strip()]
                if len(lines) > 1:
                    doc = {
                        "section": lines[0],   # First line = heading
                        "rules": lines[1:],   # Remaining lines = rules
                        "page_number": i + 1,
                        "source": "road_traffic_rules.pdf"
                    }
                    collection.insert_one(doc)

print("✅ Structured PDF data stored in a separate MongoDB database/collection")



