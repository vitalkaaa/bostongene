import time
import unittest

import requests

url = 'https://www.python.org/static/img/python-logo@2x.png'
bad_url = url + 'qwerty'


class TestAPI(unittest.TestCase):
    def test_in_process(self):
        guid = requests.post('http://0.0.0.0:8888/process', json={'url': url}).json()['data']['guid']
        res_json = requests.get(f'http://0.0.0.0:8888/check/{guid}').json()
        self.assertEqual(res_json.get('error'), 'in process')

    def test_is_ready(self):
        guid = requests.post('http://0.0.0.0:8888/process', json={'url': url}).json()['data']['guid']
        time.sleep(2)
        res_json = requests.get(f'http://0.0.0.0:8888/check/{guid}').json()
        self.assertEqual(res_json.get('success'), True)

    def test_without_url(self):
        response = requests.post('http://0.0.0.0:8888/process', json={}).json()
        self.assertEqual(response['error'], 'url not found')

    def test_without_payload(self):
        response = requests.post('http://0.0.0.0:8888/process').json()
        self.assertEqual(response['error'], 'url not found')

    def test_bad_url(self):
        guid = requests.post('http://0.0.0.0:8888/process', json={'url': bad_url}).json()['data']['guid']
        time.sleep(2)
        res_json = requests.get(f'http://0.0.0.0:8888/check/{guid}').json()
        self.assertEqual(res_json.get('error'), 'resource not found')


if __name__ == '__main__':
    unittest.main()
