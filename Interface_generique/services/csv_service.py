from pathlib import Path


class CsvService:

    def read_file(self):

        base_dir = Path(__file__).parent
        file = base_dir / "data.csv"

        if not file.exists():
            return "data.csv introuvable"

        return file.read_text(
            encoding="utf-8"
        )