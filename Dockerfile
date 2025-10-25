FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r python-function-accelerator/requirements.txt
# Default command prints a sample invocation using the package
CMD ["python", "-c", "from src.main import handle_request; print(handle_request({'data':'hello'}))"]
