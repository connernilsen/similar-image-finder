from db.database import DatabaseWorker, default_path


class DatabaseImageHandler:
    def __init__(self, db_path=default_path):
        self.worker = DatabaseWorker(db_path)

    def find_image(self, md5):
        self.worker.execute("SELECT * FROM image WHERE md5_hash = :hash_val;", {"hash_val": md5})
        return self.worker.get_single_result()