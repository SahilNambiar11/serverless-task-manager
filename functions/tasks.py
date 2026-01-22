import json
import uuid
import boto3
import time
from boto3.dynamodb.conditions import Key

# Connect to DynamoDB table
dynamodb = boto3.resource("dynamodb", region_name="us-east-2")
table = dynamodb.Table("Tasks")

print("CI/CD test: Lambda deployed!")


def lambda_handler(event, context):
    """
    Lambda function that handles task management.
    Supports POST (create), GET (read), PUT (update), DELETE (delete).
    """
    start_time = time.time()

    method = event.get("httpMethod", "POST")  # default POST if not specified

    # Determine where the body is (Function URL vs API Gateway)
    body_str = event.get("body") if "body" in event else json.dumps(event)
    try:
        body = json.loads(body_str)
    except Exception:
        body = {}

    # ---------------- CREATE ----------------
    if method == "POST":
        task_id = str(uuid.uuid4())
        item = {
            "task_id": task_id,
            "title": body.get("title", ""),
            "completed": False
        }
        table.put_item(Item=item)
        return {
            "statusCode": 201,
            "body": json.dumps(item)
        }

    # ---------------- READ ----------------
    elif method == "GET":
        # If task_id provided, get single task; else scan all tasks
        task_id = event.get("queryStringParameters", {}).get("task_id")
        if task_id:
            response = table.get_item(Key={"task_id": task_id})
            item = response.get("Item")
            if not item:
                return {"statusCode": 404, "body": json.dumps({"error": "Task not found"})}
            return {"statusCode": 200, "body": json.dumps(item)}
        else:
            # return all tasks
            response = table.scan()
            return {"statusCode": 200, "body": json.dumps(response["Items"])}

    # ---------------- UPDATE ----------------
    elif method in ["PUT", "PATCH"]:
        task_id = body.get("task_id")
        if not task_id:
            return {"statusCode": 400, "body": json.dumps({"error": "task_id required"})}

        # Build the update expression
        update_expr = []
        expr_attr_values = {}
        if "title" in body:
            update_expr.append("title = :t")
            expr_attr_values[":t"] = body["title"]
        if "completed" in body:
            update_expr.append("completed = :c")
            expr_attr_values[":c"] = body["completed"]

        if not update_expr:
            return {"statusCode": 400, "body": json.dumps({"error": "Nothing to update"})}

        response = table.update_item(
            Key={"task_id": task_id},
            UpdateExpression="SET " + ", ".join(update_expr),
            ExpressionAttributeValues=expr_attr_values,
            ReturnValues="ALL_NEW"
        )

        return {"statusCode": 200, "body": json.dumps(response["Attributes"])}

    # ---------------- DELETE ----------------
    elif method == "DELETE":
        task_id = event.get("queryStringParameters", {}).get("task_id") or body.get("task_id")
        if not task_id:
            return {"statusCode": 400, "body": json.dumps({"error": "task_id required"})}

        response = table.delete_item(Key={"task_id": task_id})
        return {"statusCode": 200, "body": json.dumps({"deleted_task_id": task_id})}

    # ---------------- INVALID METHOD ----------------
    else:
        return {"statusCode": 405, "body": json.dumps({"error": f"Method {method} not allowed"})}
    
    end_time = time.time()
    print(f"Execution time: {(end_time - start_time) * 1000:.2f} ms")
