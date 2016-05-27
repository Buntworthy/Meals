from datastore import DataStoreDict


def setup():
    data = DataStoreDict('test_file')

    titles = ('test title 1',
              'test title 2',
              'test title 3')
    tags = ('tag1 tag2',
            'tag2 tag3',
            'tag1 tag2 tag4')

    for title, tag in zip(titles, tags):
        data.add_entry(title, tag)

    return data, titles, tags


def test_add():
    data, titles, tags = setup()
    index, stored_title, stored_tags = data.get_entry(1)
    assert stored_title == titles[0]
    assert stored_tags == tags[0]


def test_delete():
    data, titles, tags = setup()
    data.delete_entry(1)
    result = data.get_entry(1)
    assert result is None


def test_search_tag():
    data, titles, tags = setup()
    result = data.search_tags(('tag1',))
    assert len(result) == 2
    assert 1 in result
    assert 3 in result

    result = data.search_tags(('tag2', 'tag3'))
    assert len(result) == 1
    assert 2 in result

    result = data.search_tags(('tag1', 'tag2', 'tag3'))
    assert len(result) == 0


def test_edit_add_tag():
    data, titles, tags = setup()
    data.add_tag(1, ('tagx', 'tagy'))

    result = data.search_tags(('tagx',))
    assert len(result) == 1
    assert 1 in result

    result = data.search_tags(('tagx', 'tagy'))
    assert len(result) == 1
    assert 1 in result


def test_edit_remove_tag():
    data, titles, tags = setup()
    data.remove_tag(1, ('tag1',))

    result = data.search_tags(('tag1',))
    assert len(result) == 1
    assert 3 in result

    result = data.get_entry(1)
    assert result[2] == 'tag2'

# TODO test badly formed entries