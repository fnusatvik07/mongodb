# main.py
from mongo_client import MongoDBClient
from agent_log import AgentLogRepository

# Step 1: Create MongoDB connection
mongo_client = MongoDBClient()
db = mongo_client.get_database("ai_app")

# Step 2: Create repository
log_repo = AgentLogRepository(db)

# Step 3: Insert a log
log_id = log_repo.create_log({
    "user_id": "u1",
    "thread_id": "t100",
    "event": "chat",
    "model": "gpt-4o",
    "tokens": 320
})

print("Inserted log ID:", log_id)

# Step 4: Read logs
logs = log_repo.get_logs_by_user("u1")
print("User logs:", logs)

# Step 5: Update tokens
log_repo.update_tokens("t100", 400)
print("Tokens updated")

# Step 6: Soft delete
log_repo.soft_delete_log("t100")
print("Log soft deleted")

# Step 7: Verify deletion
logs_after_delete = log_repo.get_logs_by_user("u1")
print("Logs after delete:", logs_after_delete)
