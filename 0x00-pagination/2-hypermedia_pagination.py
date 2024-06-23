#!/usr/bin/env python3
"""0-simple_helper_function.py
"""
import csv
import math
from typing import Tuple, List, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Helper function to return the index_range that takes twointegers"""
    start_page = (page - 1) * page_size
    end_page = start_page + page_size
    return (start_page, end_page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a list of baby names from the dataset
        based on the page and page_size."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page=page, page_size=page_size)
        data = self.dataset()
        try:
            return data[start: end]
        except Exception as e:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns a dictionary with pagination metadata."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {"page_size": page_size,
                "page": page,
                "data": self.get_page(page=page, page_size=page_size),
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages}
