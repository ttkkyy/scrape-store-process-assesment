Python Package Dependencies 🧰
- requests-html (Perform REST requests)
- lxml-html-clean (Extension for requests-html)
- mysql-connector-python (Database connector [depends on database]) 
- psycopg2-binary (Postgres Db was used for deployment)
- fastapi (Web building framework)
- uvicorn (ASGI web server implementation)
- python-dotenv (allow usage of .env file) 

Project Preface : <hr>
This assestment is prepared by MindHive, an AI Automation service company. Despite being really rusty at Python, the project was first attempted without using an AI assistance tools (Chatbot etc), after trying multiple days without AI, the task seemingly took too long. With assistance from AI Tools and chatbot additionally with basic understanding on the language python, this project is done with ease despite not knowing many libraries and methods on doing certain functionalities and methods. AI seemingly done wonders and proved to be of great assisstant if used correctly.  

Project Requirements 🛠️: <hr>
Part 1: Web Scraping and Database Storage
URL to Scrap: https://www.mcdonalds.com.my/locate-us
1. First, filter the search by “kuala lumpur”.
2. Scrape the names, addresses, operating hours, Waze link of outlets from a given webpage
that has multiple pages of content.
3. Ensure your script can handle pagination to navigate through all available pages.
4. Store the scraped data into a database, designing the schema in a way that you find
suitable for this task.

Part 2: Geocoding
For each outlet, retrieve its geographical coordinates based on the stored address.

Part 3: API Development
Develop a backend API (FastAPI) to serve the outlet data, including their geographical
coordinates.

Part 4: Frontend Development and Visualization
1. Create a web application that interacts with your API to visualise the outlets on a map.
2. Implement functionality to display a 5KM radius catchment around each outlet on the
map.
3. Highlight or mark the outlets that intersect with any other outlet’s 5KM radius catchment.

Part 5: Chatbot Functionality
Add a search box to allow the user to enter a query. Examples of query that you would need
to handle include:
1. Which outlets in KL operate 24 hours?
2. Which outlet allows birthday parties?
You are free to use Agentic AI, RAG, LLM or NLP to achieve this.

Part 6: Documentation and Instructions
Provide documentation with setup instructions, key technical decisions (frameworks, libraries,
architecture) with reasoning, and essential information to understand and use the solution.

Project Setup and screenshots 📃: <hr>
Project can be easily start up using uvicorn by opening a server on an existing port [uvicorn main:app --host 0.0.0.0 --port 8000 --reload]
scraper.py can be upgraded to use selenium if the scrapped data is complicated to retrieve


Catchment (2.5 km instead of 5 because each Mcdonalds are too close to each other) 
<img width="1182" height="870" alt="image" src="https://github.com/user-attachments/assets/b9c16a35-e30e-46d9-b8de-c1171edc9244" />

Chat Query (with auto highlighting of outlet)
<img width="1754" height="882" alt="image" src="https://github.com/user-attachments/assets/3bf92b6d-fb8e-456c-88ca-c73989133eda" />

File Structure 📁 : <br>
 	/app
<br>	|--- /db  --- base.sql   [Base SQL to run on initiliazation]
<br>	|--- /style --- style.css  [Frontend styling for web pages]
<br> |--- /templates ---  index.html	 [Main page for web application]
<br>	|--- main.py [Main file, hosts for index.html]
<br>	|--- api.py [API file, hosts for application's API]
<br>	|--- init.py [Initialization file, holds application start and initialization needs (database ,etc)]
<br>	|--- scraper.py [Web Scraping file, host for web scraping applications]
<br>	|--- README.md 
<br> |--- .env [env file, Stores important config information]
<br> |--- requirements.txt [package dependencies files]
