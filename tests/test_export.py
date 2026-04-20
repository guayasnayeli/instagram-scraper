import os
from export.exporter import export_to_csv

def test_export_creates_file():
    data = [{"id": 1, "username": "test"}]

    export_to_csv(data, "testfile")

    # verificar carpeta outputs
    assert os.path.exists("outputs")