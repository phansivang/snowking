FROM python:3.10.7

# Set the working directory inside the container to /app
# All subsequent commands will be executed from this directory
WORKDIR /src

# Copy the requirements.txt file from the local filesystem into the container's working directory
COPY requirements.txt ./

# Install the Python dependencies listed in the requirements.txt
RUN pip install -r requirements.txt

# Copy all the files from the current local directory to the container’s working directory
COPY . ./

# Set the default command to run Streamlit when the container starts
# This command runs the app located at app/main.py on port 8501
CMD ["streamlit", "run", "main.py"]