# To run a single test:
# python -munittest test.TestValidator.test_valid 

import json
import urllib.request

import unittest


HOST = "http://localhost:5000"
# Optionally enable debug logging
# DEBUGLEVEL = 1
DEBUGLEVEL = 0


def request(host, crate_path):
    url = f"{host}/v1/ro_crates/validate_metadata"

    with open(crate_path) as f:
        payload = json.dumps({
            "crate_json": f.read(),
            "profile_name": "five-safes-crate",
        })

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    req = urllib.request.Request(url, data=payload.encode(), headers=headers, method="POST")

    http_handler = urllib.request.HTTPHandler(debuglevel=DEBUGLEVEL)
    opener = urllib.request.build_opener(http_handler)

    with opener.open(req, timeout=60) as response:
        body = response.read().decode("utf-8")
        status = response.status

    body = json.loads(body)
    return status, body


class TestValidator(unittest.TestCase):

    def test_invalid(self):
        status, body = request(HOST, "dummy.json")
        self.assertEqual(status, 200)
        self.assertEqual(body["status"], "invalid", msg=json.dumps(body, indent=2))


    def test_valid(self):
        status, body = request(HOST, "ro-crate-metadata-5s.json")
        self.assertEqual(status, 200)
        self.assertEqual(body["status"], "valid", msg=json.dumps(body, indent=2))


if __name__ == '__main__':
    unittest.main()
