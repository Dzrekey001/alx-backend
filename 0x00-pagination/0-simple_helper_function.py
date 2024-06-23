#!/usr/bin/env python3
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Helper function to return the index_range that takes twointegers"""
    start_page = (page - 1) * page_size
    end_page = start_page + page_size
    return (start_page, end_page)
