# Use official Python image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK data
RUN python -m nltk.downloader punkt stopwords

# Create necessary directories with proper permissions
RUN mkdir -p /app/exports /app/logs /app/database /app/cache && \
    chmod 777 /app /app/exports /app/logs /app/database /app/cache

# Copy project files
COPY . .

# Create Jupyter config directory
RUN mkdir -p /root/.jupyter

# Copy Jupyter configuration
COPY jupyter_notebook_config.py /root/.jupyter/

# Expose ports for Jupyter and optional API
EXPOSE 8888 5000

# Command to run Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
