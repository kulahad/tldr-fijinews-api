# News Webscraping API

This project aims to automate the collection of news from various local platforms and provide a unified access point through an API. This approach allows for easy consumption of aggregated news data by any type of application, whether mobile or desktop.

## Disclaimer

This project is an educational passion project and is not intended for commercial use. All data and content scraped and aggregated by this application are copyrighted by their respective sources. The creator of this project has no intention to monetize or sell this software, website, or any of the content it aggregates. This tool is meant for personal use and learning purposes only.

Users of this project should be aware of and respect the copyright and terms of use of the original news sources. Always ensure you have the right to use the data as intended and consider reaching out to the original sources for permission if you plan to use the aggregated data for anything other than personal, non-commercial purposes.

## Project Overview

Web scraping offers an efficient way to automate many of our daily web routines. This project leverages that concept to create a service that:

1. Scrapes data from multiple local news platforms - Only [Fijivillage](https://fijivillage.com/news) is supported for now.
2. Aggregates the collected information
3. Provides the data via an API endpoint

## Technologies Used

- **BeautifulSoup (BS4)**: For parsing HTML and extracting data from web pages
- **Sumy**: A text summarization library to create concise news summaries
- **FastAPI**: For creating the API
- **MongoDB**: As the database backend
- **Poetry**: For dependency management and packaging

## Setup and Installation

1. Ensure you have Python and Poetry installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory and run `poetry install` to install dependencies.
4. Create a `.env` file in the project root and add the following:

   ```
   MONGODB_URI=your_mongodb_uri_here
   MONGODB_DBNAME=your_collection_name_here
   ```

## Starting the API

To start the API server, run the following command:

```bash
poetry run uvicorn api:app --reload
```

This command starts the FastAPI server with hot-reloading enabled for development purposes.

## API Usage

The API provides the following endpoints:

1. **Main Endpoint**

   - URL: `/`
   - Method: GET
   - Description: Main entry point of the API
   - Response: 200 OK with JSON content

2. **News Endpoint**

   - URL: `/news`
   - Method: GET
   - Description: Retrieve aggregated news data
   - Response: 200 OK with JSON content containing news items

3. **Grab News Endpoint**
   - URL: `/grabnews`
   - Method: POST
   - Description: Trigger the news scraping process
   - Response: 200 OK with JSON content (likely a confirmation or status message)

All endpoints return JSON responses. For more detailed information about request and response schemas, you can access the OpenAPI documentation by navigating to `/docs` when the API is running.

## Contributing

Contributions to this project are welcome! If you'd like to contribute, please feel free to open a Pull Request (PR) with your proposed changes. Here are some guidelines for contributing:

1. Fork the repository and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. Ensure your code follows the project's coding style.
4. Make sure your code lints.
5. Issue that pull request!
