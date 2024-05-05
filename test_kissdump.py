import uuid

from hypothesis import HealthCheck, given, settings, strategies

import kissdump


@given(data=strategies.binary())
@settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
def test_kissdump(monkeypatch, tmp_path, data):
    with monkeypatch.context() as m:
        file_name = tmp_path / f"{uuid.uuid4()}.txt"
        m.setattr(kissdump, "file_name", file_name)
        kissdump.kissdump(data)

        assert file_name.read_bytes() == data
