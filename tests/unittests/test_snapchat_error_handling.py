from distutils.log import debug
import unittest
from unittest import mock
import tap_snapchat_ads
from tap_snapchat_ads import SnapchatClient
import tap_snapchat_ads.client as client
from tap_snapchat_ads.client import requests


class MockedResponse:
    def __init__(self, status_code, debug_message=None) -> None:
        self.status_code = status_code
        self.content = "test"
        self.debug_message = debug_message
        
    def raise_for_status(self):
        raise requests.HTTPError
    
    def json(self):
        return {"request_status": "ERROR", "debug_message": self.debug_message}


@mock.patch('requests.Session.request')
class TestExceptionHandling(unittest.TestCase):
    """
        Test cases to verify error is raised with proper message  for SnapchatClient's request method.
    """
    

    def test_400_error_custom_message(self, mocked_request):
        """
            Test case to verify 400 error message from response
        """
        mocked_request.return_value = MockedResponse(400)
        clx = SnapchatClient("test", "test", "test", "test")
        with self.assertRaises(client.SnapchatBadRequestError) as e:
            clx.request('GET')
            
        self.assertEqual(str(e.exception), "HTTP-error-code: 400, Message: The request is missing or has a bad parameter.")
    
    def test_400_error_response_message(self, mocked_request):
        """
            Test case to verify 400 error message from response
        """

        mocked_request.return_value = MockedResponse(400, "This mesaage from response 400.")
        clx = SnapchatClient("test", "test", "test", "test")
        with self.assertRaises(client.SnapchatBadRequestError) as e:
            clx.request('GET')
            
        self.assertEqual(str(e.exception), "400, None: This mesaage from response 400.")

    def test_401_error_custom_message(self, mocked_request):
        """
            Test case to verify 401 error message from response
        """

        mocked_request.return_value = MockedResponse(401)
        clx = SnapchatClient("test", "test", "test", "test")
        with self.assertRaises(client.SnapchatUnauthorizedError) as e:
            clx.request('GET')

        self.assertEqual(str(e.exception), "HTTP-error-code: 401, Message: Unauthorized access for the URL.")

    def test_401_error_response_message(self, mocked_request):
        """
            Test case to verify 401 error message from response
        """

        mocked_request.return_value = MockedResponse(401, "This mesaage from response 401.")
        clx = SnapchatClient("test", "test", "test", "test")
        with self.assertRaises(client.SnapchatUnauthorizedError) as e:
            clx.request('GET')
            
        self.assertEqual(str(e.exception), "401, None: This mesaage from response 401.")
 
    def test_403_error_custom_message(self, mocked_request):
        """
            Test case to verify 403 error message from response
        """

        mocked_request.return_value = MockedResponse(403)
        clx = SnapchatClient("test", "test", "test", "test")
        with self.assertRaises(client.SnapchatForbiddenError) as e:
            clx.request('GET')

        self.assertEqual(str(e.exception), "HTTP-error-code: 403, Message: User does not have permission to access the resource.")

    def test_403_error_response_message(self, mocked_request):
        """
            Test case to verify 403 error message from response
        """

        mocked_request.return_value = MockedResponse(403, "This mesaage from response 403.")
        clx = SnapchatClient("test", "test", "test", "test")
        with self.assertRaises(client.SnapchatForbiddenError) as e:
            clx.request('GET')

        self.assertEqual(str(e.exception), "403, None: This mesaage from response 403.")
    
    def test_404_error_custom_message(self, mocked_request):
        """
            Test case to verify 404 error message from response
        """
        mocked_request.return_value = MockedResponse(404)
        clx = SnapchatClient("test", "test", "test", "test")
        with self.assertRaises(client.SnapchatNotFoundError) as e:
            clx.request('GET')
            
        self.assertEqual(str(e.exception), "HTTP-error-code: 404, Message: The resource you have specified cannot be found.")

    def test_404_error_response_message(self, mocked_request):
        """
            Test case to verify 404 error message from response
        """

        mocked_request.return_value = MockedResponse(404, 'This mesaage from response 404')
        clx = SnapchatClient("test", "test", "test", "test")
        with self.assertRaises(client.SnapchatNotFoundError) as e:
            clx.request('GET')
        
        self.assertEqual(str(e.exception), "404, None: This mesaage from response 404")

    def test_405_error_custom_message(self, mocked_request):
        """
            Test case to verify 405 error message from response
        """
        mocked_request.return_value = MockedResponse(405)
        clx = SnapchatClient("test", "test", "test", "test")
        with self.assertRaises(client.SnapchatMethodNotAllowedError) as e:
            clx.request('GET')

        self.assertEqual(str(e.exception), "HTTP-error-code: 405, Message: The provided HTTP method is not supported by the URL.")

    def test_405_error_response_message(self, mocked_request):
        """
            Test case to verify 405 error message from response
        """

        mocked_request.return_value = MockedResponse(405, "This mesaage from response 405")
        clx = SnapchatClient("test", "test", "test", "test")
        with self.assertRaises(client.SnapchatMethodNotAllowedError) as e:
            clx.request('GET')

        self.assertEqual(str(e.exception), "405, None: This mesaage from response 405")

    def test_406_error_custom_message(self, mocked_request):
        """
            Test case to verify 406 error message from response
        """
        mocked_request.return_value = MockedResponse(406)
        clx = SnapchatClient("test", "test", "test", "test")
        with self.assertRaises(client.SnapchatNotAcceptableError) as e:
            clx.request('GET')

        self.assertEqual(str(e.exception), "HTTP-error-code: 406, Message: You requested a format that isn’t json.")

    def test_406_error_response_message(self, mocked_request):
        """
            Test case to verify 406 error message from response
        """

        mocked_request.return_value = MockedResponse(406, "This mesaage from response 406")
        clx = SnapchatClient("test", "test", "test", "test")
        with self.assertRaises(client.SnapchatNotAcceptableError) as e:
            clx.request('GET')

        self.assertEqual(str(e.exception), "406, None: This mesaage from response 406")
        
    def test_410_error_custom_message(self, mocked_request):
        """
            Test case to verify 410 error message from response
        """
        mocked_request.return_value = MockedResponse(410)
        clx = SnapchatClient("test", "test", "test", "test")
        with self.assertRaises(client.SnapchatGoneError) as e:
            clx.request('GET')

        self.assertEqual(str(e.exception), "HTTP-error-code: 410, Message: Access to the Snapchat is no longer available.")

    def test_410_error_response_message(self, mocked_request):
        """
            Test case to verify 410 error message from response
        """

        mocked_request.return_value = MockedResponse(410, "This mesaage from response 410")
        clx = SnapchatClient("test", "test", "test", "test")
        with self.assertRaises(client.SnapchatGoneError) as e:
            clx.request('GET')

        self.assertEqual(str(e.exception), "410, None: This mesaage from response 410")
        
    def test_418_error_custom_message(self, mocked_request):
        """
            Test case to verify 418 error message from response
        """
        mocked_request.return_value = MockedResponse(418)
        clx = SnapchatClient("test", "test", "test", "test")
        with self.assertRaises(client.SnapchatTeapotError) as e:
            clx.request('GET')

        self.assertEqual(str(e.exception), "HTTP-error-code: 418, Message: The server refuses to brew coffee because it is, permanently, a teapot.")

    def test_418_error_response_message(self, mocked_request):
        """
            Test case to verify 418 error message from response
        """

        mocked_request.return_value = MockedResponse(418, "This mesaage from response 418")
        clx = SnapchatClient("test", "test", "test", "test")
        with self.assertRaises(client.SnapchatTeapotError) as e:
            clx.request('GET')

        self.assertEqual(str(e.exception), "418, None: This mesaage from response 418")
        
        

    @mock.patch("time.sleep")   
    def test_500_error_response_message(self, mocked_sleep, mocked_request):
        """
            Test case to verify 500 error message from response
        """

        mocked_request.return_value = MockedResponse(500)
        clx = SnapchatClient("test", "test", "test", "test")
        with self.assertRaises(client.Server5xxError) as e:
            clx.request('GET')
            

        self.assertEqual(str(e.exception), "")
