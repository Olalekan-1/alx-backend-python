#!/usr/bin/env python3

""" Testing """

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Test Github client client """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """ tests_ org testing """
        client = GithubOrgClient(org_name)
        expected_url = GithubOrgClient.ORG_URL.format(org=org_name)

        mock_get_json.return_value = {"name": org_name}
        org_info = client.org()
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(org_info, {"name": org_name})

    def test_public_repos_url(self):
        known_payload = {"repos_url":
                         "https://api.github.com/orgs/testorg/repos"}

        with patch.object(GithubOrgClient,
                          'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = known_payload

            client = GithubOrgClient("testorg")

            public_repos_url = client._public_repos_url

            self.assertEqual(public_repos_url,
                             "https://api.github.com/orgs/testorg/repos")


if __name__ == "__main__":
    unittest.main()
