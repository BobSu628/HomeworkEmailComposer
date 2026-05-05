from homework_data_fetcher import HomeworkDataFetcher

class GoogleSheetsHomeworkFetcher(HomeworkDataFetcher):
    def fetch_homework_data(self):
        # Example placeholder logic
        return [
            {
                "email": "student@example.com",
                "name": "Alice",
                "task": "Math homework",
                "due_date": "2026-05-10"
            }
        ]
