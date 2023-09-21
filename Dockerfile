# Use an official Python runtime as a parent image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Copy the current directory contents into the container at /app
COPY ./app /app

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app:$PYTHONPATH

# Install any needed packages specified in requirements.txt
ADD requirements.txt /app/
RUN pip install -r requirements.txt

# Expose the port that your application will run on
EXPOSE 8080

# Command to run your application using Gunicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
