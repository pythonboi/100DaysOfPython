import gzip
import shutil

with open(r'C:\Users\htukuru\Downloads\efw-1390300394-firewall-20220926.log', 'rb') as file_in:
    with gzip.open(r'C:\Users\htukuru\Downloads\efw-1390300394-firewall-20220926.log.gz', 'wb') as file_out:
        shutil.copyfileobj(file_in, file_out)
