#!/usr/bin/env python3
"""2. Hypermedia pagination"""
import csv
import math
from typing import Tuple, List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get corresponding page
        Args:
            page: page number
            page_size: size of the page

        Return:
            content of the target page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        pagination_range: Tuple = self.index_range(page, page_size)
        data: List = self.dataset()

        return data[pagination_range[0] : pagination_range[1]]

    def get_hyper(self, page: int, page_size: int) -> Dict:
        """
        Hypermedia pagination
        Args:
            page: page number
            page_size: number of elements per page

        Return:
            Dictionary that contain the following elements
            page_size: the length of the returned dataset page.
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """

        try:
            data = self.get_page(page, page_size)
        except AssertionError:
            return {}

        dataset: List = self.dataset()
        total_pages: int = math.ceil(len(dataset) / page_size)
        prev_page = None if page == 1 else page - 1
        next_page = None if page + 1 > total_pages else page + 1

        hypermedia: Dict = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }

        return hypermedia

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        The function should return a tuple of size two containing a start index
        and an end index corresponding to the range of indexes to return in a
        list for those particular pagination parameters.

        Args:
            page: Current page
            page_size: Total size of the page
        Return:
            tuple with the range start and end size page
        """
        final_size: int = page * page_size
        start_size: int = final_size - page_size

        return (start_size, final_size)
