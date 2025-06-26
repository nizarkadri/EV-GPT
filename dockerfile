# Use the stable and widely compatible Python 3.11 as the base image.
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy ALL your application files into the container.
# This assumes you have already run setup_vector_db.py locally
# and the 'db' folder exists in your project directory.
COPY . .

# Add a non-root user and change ownership for security and permissions.
RUN useradd -m -u 1000 python
RUN chown -R python:python /app
USER python

# Expose the port for Streamlit
EXPOSE 8501

# Use the "exec form" of CMD. This runs the command as the main process (PID 1),
# allowing it to properly receive and handle OS signals like SIGTERM from 'docker stop'.
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableCORS=false"]
