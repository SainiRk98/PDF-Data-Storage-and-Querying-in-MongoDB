Project Overview
This project demonstrates how to **store and manage legal PDF data in MongoDB** using CSV and JSON files.  
It includes:
- Uploading CSV/JSON data into MongoDB collection `legal_pdf_data`.
- Performing queries and aggregations on legal documents.
- Example scripts to extract, upload, and analyze PDF metadata.
- 
Tech Stack
  Python – for scripting and data handling  
  PyMongo – to connect and interact with MongoDB  
  MongoDB – NoSQL database to store PDF data  
  CSV / JSON– input data formats  
  MongoDB Compass – for visual inspection and manual queries  

Project Structure
legal-pdf-mongodb/
│
├── data/ 
│ ├── legal_pdf_data.csv
│ └── legal_pdf_data.json
│
├── scripts/ 
│ ├── upload_csv.py
│ ├── upload_json.py 
│ └── example_queries.py
│
├── requirements.txt
├── README.md 
└── .gitignore 
