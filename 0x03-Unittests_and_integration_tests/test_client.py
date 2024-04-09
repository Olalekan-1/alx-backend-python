#!/usr/bin/env python3

""" Testing """

import unittest
from unittest.mock import patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):

    endpoint = "https://api.github.com/orgs/testorg/repos"

    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()

        cls.mock_get.side_effect = [
            lambda url: org_payload if url == endpoint else repos_payload,
            lambda url: repos_payload,
            lambda url: apache2_repos,
        ]

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        known_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "mit"}},
        ]

        with patch.object(GithubOrgClient,
                          '_public_repos_url', return_value=endpoint):
            mock_get_json.return_value = known_payload

            client = GithubOrgClient("testorg")

            repos = client.public_repos(license="mit")

            mock_get_json.assert_called_once_with(endpoint)
            self.assertEqual(repos, ["repo1", "repo3"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        client = GithubOrgClient("testorg")

        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)

    def test_public_repos(self):
        client = GithubOrgClient("testorg")
        repos = client.public_repos()

        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        client = GithubOrgClient("testorg")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
