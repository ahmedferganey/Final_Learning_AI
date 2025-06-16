FROM demisto/opencv:1.0.0.3252732

WORKDIR /app

COPY requirements.txt .
# Downgrade NumPy first
RUN pip install "numpy<2"


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

CMD ["python", "main.py"]

