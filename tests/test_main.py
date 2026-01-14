from app.main import analyze_log
import tempfile

def test_analyze_log():
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write("Error 1\nError 2\nError 3\n")
        f.seek(0)
        assert analyze_log(f.name) == 3
