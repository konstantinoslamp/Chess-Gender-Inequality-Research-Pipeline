# Chess Gender Inequality Research Pipeline

An enterprise-grade research pipeline for automatically searching and analyzing academic papers related to gender inequality in chess.

## Features

- Automated Google Scholar scraping for academic papers
- Custom relevance scoring for ranking papers
- SQLite database integration for persistent storage
- RESTful API for programmatic access to research data
- Comprehensive data visualization
- Docker containerization for consistent deployment

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Git

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/konstantinoslamp/Chess-Gender-Inequality-Research-Pipeline.git
   cd Chess-Gender-Inequality-Research-Pipeline
   ```

2. Start the container with Docker Compose
   ```bash
   docker-compose up -d
   ```

3. Access the Jupyter notebook at http://localhost:8888
4. Access the API at http://localhost:5000

### Alternative: Run with Docker Directly

If you prefer not to use Docker Compose:

1. Build the Docker image:
   ```bash
   docker build -t chess-gender-inequality .
   ```

2. Start the container:
   ```bash
   docker run -p 8888:8888 -p 5000:5000 -v ${PWD}:/app -v ${PWD}/exports:/app/exports -v ${PWD}/logs:/app/logs --user root chess-gender-inequality
   ```

## Usage

The main workflow is in `Chess_Gender_Inequality_Scholar_Pipeline.ipynb`. Run through the notebook cells to:

1. Search for papers on gender inequality in chess
2. Analyze and score the papers by relevance
3. Visualize the results
4. Access the data through the API

## API Endpoints

- `GET /api/papers` - Retrieve all papers from the current run
- `GET /api/top_papers` - Get the top 5 most relevant papers
- `POST /api/search` - Perform a new search (requires JSON body with query parameter)

## Database Structure

The project uses SQLite for data storage with two main tables:

- **runs**: Stores metadata about each research run
- **papers**: Stores paper details with references to runs

## Interactive Dashboard (Optional)

The project includes a commented-out dashboard service in docker-compose.yml that can be enabled for interactive data visualization on port 8050.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Scholar for the academic paper data
- The research community studying gender inequality in chess

## Connecting VS Code to Docker Jupyter Server

1. Start the Docker container as described above
2. In VS Code:
   - Open the notebook file
   - Click on the kernel selector in the top right corner (it might show "Select Kernel")
   - Choose "Select Another Kernel..."
   - Select "Existing Jupyter Server..."
   - Enter the URL: `http://localhost:8888` (no token required)
   - Select the kernel from the Docker environment

## Enterprise Features

### Database Integration
The pipeline stores all research data in an SQLite database for persistent storage and analysis:
- Run history is tracked with timestamps
- Paper metadata and analysis results are stored with proper relationships
- Each run has a unique identifier for tracking purposes

### Advanced Analytics
The pipeline includes several NLP features:
- Sentiment analysis of paper abstracts
- Key term extraction for better understanding of paper content
- Relevance scoring based on domain-specific keywords

### Interactive Dashboards
The pipeline generates interactive visualizations:
- Bar charts of relevance scores
- Sentiment analysis visualization
- Comparative view of papers
- HTML exports that can be shared and viewed in any browser

## Files in this Repository

- `Chess_Gender_Inequality_Scholar_Pipeline.ipynb`: Main notebook file
- `Dockerfile`: Docker configuration
- `requirements.txt`: Python dependencies
- `jupyter_notebook_config.py`: Jupyter configuration file
- `docker-commands.txt`: Helpful Docker commands
- `database/`: SQLite database storage
- `exports/`: CSV and visualization exports with timestamps
- `logs/`: Execution logs with timestamps
- `cache/`: Performance cache for repeated searches
