from os import path
from pathlib import Path

from icrawler.builtin import GoogleImageCrawler

BASE_DIR = Path(__file__).resolve().parent


def google_img_downloader(x: str):
    filters = dict(type="photo", color="color", size="medium")
    crawler = GoogleImageCrawler(storage={"root_dir": path.join(BASE_DIR, r"static\qrc")})
    crawler.crawl(
        keyword=x,
        max_num=1,
        min_size=(600, 600),
        overwrite=True,
        filters=filters,
        file_idx_offset='auto'
    )
