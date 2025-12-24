# agent_log_repository.py
from datetime import datetime


class AgentLogRepository:
    """
    Handles all MongoDB operations related to agent logs.
    """

    def __init__(self, database):
        self.collection = database["agent_logs"]

    # -----------------------------
    # CREATE
    # -----------------------------
    def create_log(self, log_data: dict):
        """
        Insert a new agent log.
        """
        log_data["created_at"] = datetime.utcnow()
        log_data["deleted"] = False

        result = self.collection.insert_one(log_data)
        return result.inserted_id

    # -----------------------------
    # READ
    # -----------------------------
    def get_logs_by_user(self, user_id: str):
        """
        Fetch all non-deleted logs for a user.
        """
        return list(self.collection.find({
            "user_id": user_id,
            "deleted": {"$ne": True}
        }))

    def get_log_by_thread(self, thread_id: str):
        """
        Fetch single log by thread_id.
        """
        return self.collection.find_one({
            "thread_id": thread_id,
            "deleted": {"$ne": True}
        })

    # -----------------------------
    # UPDATE
    # -----------------------------
    def update_tokens(self, thread_id: str, tokens: int):
        """
        Update token count for a log.
        """
        self.collection.update_one(
            {"thread_id": thread_id},
            {
                "$set": {
                    "tokens": tokens,
                    "updated_at": datetime.utcnow()
                }
            }
        )

    # -----------------------------
    # SOFT DELETE
    # -----------------------------
    def soft_delete_log(self, thread_id: str):
        """
        Soft delete a log (mark as deleted).
        """
        self.collection.update_one(
            {"thread_id": thread_id},
            {
                "$set": {
                    "deleted": True,
                    "deleted_at": datetime.utcnow()
                }
            }
        )
