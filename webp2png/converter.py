import os
import time
import logging
from PIL import Image

logger: logging.Logger = logging.getLogger("webp2png.converter")


class Converter:
    def __init__(
        self,
        output_directory: str,
        retries: int = 3,
        compression_level: int = 6,
        retry_delay: int = 1,
        dry_run: bool = False,
    ) -> None:
        self.output_directory: str = output_directory
        self.retries: int = retries
        self.compression_level: int = compression_level
        self.retry_delay: int = retry_delay
        self.dry_run: bool = dry_run

    def convert(self, file_path: str) -> bool:
        """
        Convert a .webp file to a .png file.

        Args:
            file_path (str): Path to the .webp file.

        Returns:
            bool: True if conversion is successful, False otherwise.
        """
        png_filename: str = f"{os.path.splitext(os.path.basename(file_path))[0]}.png"
        png_path: str = os.path.join(self.output_directory, png_filename)
        attempt: int = 0

        if self.dry_run:
            logger.info(f"Dry run: would convert {file_path} to {png_path}")
            return True

        while attempt < self.retries:
            try:
                start_time: float = time.time()
                with Image.open(file_path) as img:
                    img.save(
                        png_path, "PNG", compress_level=self.compression_level
                    )
                end_time: float = time.time()
                logger.info(
                    f"Converted {file_path} to {png_path} in {end_time - start_time:.2f} seconds"
                )
                return True
            except Exception as e:
                attempt += 1
                logger.error(
                    f"Attempt {attempt} failed to convert {file_path}: {e}"
                )
                time.sleep(self.retry_delay)

        logger.error(
            f"Failed to convert {file_path} after {self.retries} attempts"
        )
        return False
