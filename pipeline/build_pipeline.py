import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException
from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder

load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting to build pipeline.")

        loader = AnimeDataLoader('data/anime_with_synopsis.csv', 'data/anime_updated.csv')
        processed_csv = loader.load_and_processed()

        logger.info("Data loaded and processed ...")

        vector_builder = VectorStoreBuilder(processed_csv)
        vector_builder.build_and_save__vectorstore()

        logger.info("Vector store built successfully...")

        logger.info("Pipeline built successfully.")

    except Exception as e:
        logger.error(f"Failed to execute pipeline: {str(e)}")
        raise CustomException("Error during pipeline execution", e)

if __name__ == "__main__":
    main()