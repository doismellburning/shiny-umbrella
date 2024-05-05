import kissdump


def test_kissdump(monkeypatch, tmp_path):
    with monkeypatch.context() as m:
        file_name = tmp_path / "test.txt"
        m.setattr(kissdump, "file_name", file_name)
        content = "foo"
        kissdump.kissdump(bytes(content, "utf-8"))

        assert file_name.read_text() == content
