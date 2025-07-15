Python Package Dependencies 🧰
- requests-html (Perform REST requests)
- lxml-html-clean (Extension for requests-html)
- mysql-connector-python (Database connector [depends on database]) 
- fastapi (Web building framework)
- uvicorn (ASGI web server implementation)
- python-dotenv (allow usage of .env file) 

Project Preface : <hr>
asdfas


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

File Structure 📁 : <br>
 	/app
<br>	|--- /db  --- base.sql
<br>	|--- /style --- style.css
<br> 	|--- /templates ---  index.html	
<br>	|--- main.py
<br>	|--- api.py
<br>	|--- init.py
<br>	|--- scraper.py
<br>	|--- README.md

