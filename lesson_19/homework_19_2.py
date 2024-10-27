import pytest
from pathlib import Path
from requests import HTTPError

from lesson_19.src.clients.flask_client import FlaskClient

def test_crud_with_flask():
    """
    tests are depended, for example I wrote its in one method
    """
    # test data
    fc = FlaskClient()
    file_name = 'mars_photo1.jpg'
    file_path = Path.cwd() / file_name
    expected_response = fc.format_file_name_to_flask_response(file_name)

    # upload file
    with open(file_path, 'rb') as file_binary:
        actual_response = fc.upload_file(file_binary)
        assert expected_response == actual_response, 'Somthing wrong in upload response'

    # get file url by name
    actual_response = fc.get_file_url(file_name)
    assert expected_response == actual_response, 'Somthing wrong in get response'

    # delete file
    actual_response = fc.delete_file(file_name)
    assert actual_response == {'message': 'Image mars_photo1.jpg deleted'}, 'somthing wrong when delete file'

    # try to get deleted file's url
    try:
        not_exists_file_url = fc.get_file_url(file_name)
    except HTTPError as e:
        not_exists_file_url = 'file not exists'
    assert not_exists_file_url == 'file not exists', 'Deleted file is exists in server!!'
