from abc import ABC, abstractmethod
from typing import Any, List, Dict


class HomeworkDataFetcher(ABC):
    """
    Abstract base class for fetching homework data from any source
    (e.g., Google Sheets, database, API, etc.)
    """

    @abstractmethod
    def fetch_homework_data(self) -> List[Dict[str, Any]]:
        """
        Fetch homework data from the underlying source.

        Returns:
            A list of dictionaries, where each dictionary represents
            a homework record (e.g., student, task, due date, email).
        """
        pass
