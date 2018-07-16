"""Script defined to test the Subscription class."""

import unittest
import httpretty

from paystackapi.subscription import Subscription


class TestSubscription(unittest.TestCase):
    """Class to test subscription actions."""

    @httpretty.activate
    def test_create(self):
        """Method defined to test subscription creation."""
        httpretty.register_uri(
            httpretty.POST,
            "https://api.paystack.co/subscription",
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Subscription.create(
            customer = 'CUS_xnxdt6s1zg1f4nx',
            plan = 'Pln_2yudUnIds2p',
            authorization = '34'
        )
        self.assertTrue(response['status'])

    @httpretty.activate
    def test_fetch(self):
        """Function defined to test Subscription fetch method."""
        httpretty.register_uri(
            httpretty.GET,
            "https://api.paystack.co/subscription/4013",
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Subscription.fetch(subscription_id=4013)
        self.assertEqual(response['status'], True)

    @httpretty.activate
    def test_list(self):
        """Function defined to test paystackapi subscription list method."""
        httpretty.register_uri(
            httpretty.GET,
            "https://api.paystack.co/subscription",
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Subscription.list()
        self.assertEqual(response['status'], True)

    @httpretty.activate
    def test_disable(self):
        """Function defined to test paystackapi subscription disable method."""
        httpretty.register_uri(
            httpretty.POST,
            "https://api.paystack.co/subscription/disable",
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Subscription.disable(code="SUB_vsyqdmlzble3uii",token="d7gofp6yppn3qz7")
        self.assertEqual(response['status'], True)

    @httpretty.activate
    def test_enable(self):
        """Function defined to test paystackapi subscription enable method."""
        httpretty.register_uri(
            httpretty.POST,
            "https://api.paystack.co/subscription/enable",
            content_type='text/json',
            body='{"status": true, "contributors": true}',
            status=201,
        )

        response = Subscription.enable(code="SUB_vsyqdmlzble3uii", token="d7gofp6yppn3qz7")
        self.assertEqual(response['status'], True)
