FROM python:3.8-slim
RUN apt-get update && apt-get install -y python3-tk
WORKDIR /app
COPY illusion.py .
CMD ["python", "illusion.py", "--num_spokes", "12", "--colors", "red,blue,yellow", "--radius", "100", "--extent", "60", "--rotation_angle", "5", "--delay", "0.1"]