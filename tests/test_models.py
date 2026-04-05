import pytest
from peewee import SqliteDatabase
from app.models.link import Link

dbTest = SqliteDatabase(':memory:')
@pytest.fixture(autouse=True)
def setup_test_db():
    dbTest.bind([Link], bind_refs=False, bind_backrefs=False)
    dbTest.connect()
    dbTest.create_tables([Link])

    yield

    dbTest.drop_tables([Link])
    dbTest.close()

def test_create_link_saves_correct_data():
    target_url = 'https://example.com'
    target_code = 'exmp'

    link = Link.create(original_url = target_url, short_code = target_code)

    assert link.original_url == 'https://example.com'
    assert link.short_code == 'exmp'