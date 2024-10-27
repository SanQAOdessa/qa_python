from lesson_19.src.clients.base_client import BaseClient
import logging


class FlaskClient(BaseClient):
    """API Client for SWAPI."""

    BASE_URL = "http://127.0.0.1:8080"

    def upload_file(self, file) -> dict:
        """Upload image to server"""
        logging.info(f"sending file={file}")
        url = f"{self.BASE_URL}/upload"
        files = {'image': file}
        response = self.make_request("POST", url, files=files)
        return response.json()

    def get_file_url(self, file_name) -> dict:
        """Getting file url by name"""
        logging.info(f"Getting file {file_name}")
        url = f"{self.BASE_URL}/image/{file_name}"
        headers = {'Content-Type': 'text'}
        response = self.make_request("GET", url, headers=headers)
        return response.json()

    def delete_file(self, file_name) -> dict:
        """Deleting file by name"""
        logging.info(f"Deleting file {file_name}")
        url = f"{self.BASE_URL}/delete/{file_name}"
        params = {'Content-type': 'text'}
        response = self.make_request("DELETE", url, params=params)
        return response.json()

    def format_file_name_to_flask_response(self, file_name):
        return {'image_url': f'{self.BASE_URL}/uploads/{file_name}'}