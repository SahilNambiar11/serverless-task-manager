import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from functions.tasks import lambda_handler
import json

# -------- CREATE --------
event_post = {
    "httpMethod": "POST",
    "body": json.dumps({"title": "Test Task"})
}
print("POST:", lambda_handler(event_post, None))

# -------- READ ALL --------
event_get = {"httpMethod": "GET"}
print("GET all:", lambda_handler(event_get, None))

# -------- UPDATE --------
event_update = {
    "httpMethod": "PUT",
    "body": json.dumps({"task_id": "a4c2720a-dcca-4439-8d9f-57264a3ba2e9", "completed": True})
}
print("PUT:", lambda_handler(event_update, None))

# -------- DELETE --------
event_delete = {
    "httpMethod": "DELETE",
    "body": json.dumps({"task_id": "2390a13f-7154-4a48-86ae-f6d619096209"})
}
print("DELETE:", lambda_handler(event_delete, None))


