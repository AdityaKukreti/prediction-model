import requests
import json

month = int(input("Enter a month: "))
year = int(input("Enter a year: "))
wool = input("Enter a type of wool: ")

response = requests.post("http://127.0.0.1:5000/get-prediction",json={"month":month,"year":year,"type":wool})
data = json.loads(response.text)

print("\nPrediction Result:")
print("  Month:",data["month"])
print("  Year:",data["year"])
print("  Type:",data["type"])
print("  Price",data["prediction"])