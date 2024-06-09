import unittest
from unittest.mock import patch, MagicMock
import os
import tempfile
from webp2png.converter import Converter
from webp2png.utils import file_generator


class TestWebpToPngConverter(unittest.TestCase):

    def setUp(self) -> None:
        # Create a temporary directory
        self.test_dir: tempfile.TemporaryDirectory = tempfile.TemporaryDirectory()
        self.test_file: str = os.path.join(self.test_dir.name, "test.webp")
        with open(self.test_file, "w") as f:
            f.write("fake webp content")

    def tearDown(self) -> None:
        # Cleanup the temporary directory
        self.test_dir.cleanup()

    def test_file_generator(self) -> None:
        # Test file generator for finding .webp files
        files: list[str] = list(file_generator(self.test_dir.name, ".webp"))
        self.assertEqual(len(files), 1)
        self.assertEqual(files[0], self.test_file)

    @patch("webp2png.converter.Image.open")
    def test_convert_webp_to_png(self, mock_open: MagicMock) -> None:
        # Mock the image open and save methods
        mock_image: MagicMock = MagicMock()
        mock_open.return_value.__enter__.return_value = mock_image

        converter: Converter = Converter(self.test_dir.name, dry_run=False)
        result: bool = converter.convert(self.test_file)

        self.assertTrue(result)
        mock_image.save.assert_called_once()

    def test_dry_run(self) -> None:
        # Test dry run mode
        converter: Converter = Converter(self.test_dir.name, dry_run=True)
        result: bool = converter.convert(self.test_file)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()