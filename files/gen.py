import string
import random
import boto3
from random import randint
import time
import subprocess
import datetime
import uuid
import os

def gt():
    return str(int(round(time.time() * 1000000)))+"-"+str( uuid.uuid4())

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def gen(file):
   p=randint(3, 9)
   q=0
   while q < p:
    file.write( "P"+str(q))
    file.write( "\n")

    x=randint(15, 40)
    y=0
    while y<x:
      file.write( str(randint(120, 30000))+","+str(randint(1, 30000))+":"+id_generator(randint(1, 20)))
      file.write( "\n")

      y=y+1
    q = q + 1
   file.write ("18,1:"+str(randint(51000000000, 51999999999)))
   file.write( "\n") 
   file.write("118,1:"+(datetime.datetime.now() - datetime.timedelta(randint(0,2500))).strftime('%Y%m%d%H%M%S'))
   file.write( "\n")

def main():
  bucket = os.environ.get("S3BUCKET")
  while True:
    print(bucket)
    nn=randint(500, 3000)
    q=0
    file = open("/tmp/cdr.txt","w") 
    gen(file)
    while q<nn:
      q = q + 1
      file.write("\n")
      gen(file)
    file.close() 
    subprocess.call(['aws', 's3', 'cp' ,'/tmp/cdr.txt', "s3://"+bucket+"/"+gt()])

if __name__== "__main__":
  main()

