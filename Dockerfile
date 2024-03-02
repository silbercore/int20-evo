FROM python:3.9

# 
WORKDIR /int20-evo

# 
COPY ./requirements.txt .

# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 
COPY . .

RUN chmod a+x docker/*.sh