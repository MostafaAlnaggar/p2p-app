import unittest
from unittest.mock import patch
from CLI import CommandLineInterface
import pytest
import PeerServer, PeerClient  # Replace with your actual module and class names
from unittest.mock import patch, MagicMock
import socket
class TestCLI(unittest.TestCase):
    def setUp(self):
        self.cli_instance = CommandLineInterface()

    def tearDown(self):
        self.cli_instance = None

    @patch('builtins.input', side_effect=['1', 'test_user', 'test_pass'])
    @patch('CLI.CommandLineInterface.Register')



# Test for Negative or Invalid Port Numbers
    def test_peer_server_invalid_port(self):
        with pytest.raises(ValueError):  # Assuming your code raises a ValueError for invalid ports
            PeerServer("testuser", -1)

    def test_peer_server_initialization_valid_port(self):
        with patch('your_module.some_network_function') as mock_network:
            # Setup the mock to return a value if needed
            mock_network.return_value = None

            # Initialize the PeerServer
            server = PeerServer("testuser", 8080)

            # Perform your assertions
            assert server.username == "testuser"
            assert server.peerServerPort == 8080

            # You can also assert if the mock was called correctly
            mock_network.assert_called_once_with(...)

    # Test for Full Mesh Network Stress
    def test_full_mesh_network_stress(self):
        number_of_peers = 10  # Example for 10 peers
        peers = [PeerServer(f"user{i}", 8000+i) for i in range(number_of_peers)]


    # Test for High Network Latency and Packet Loss
    def test_high_latency_packet_loss(self):
        with patch('socket.socket') as mock_socket:
            mock_socket.return_value.recv.return_value = b''  # Simulate no data being received (timeout)
            # Create a peer and attempt to receive data, expecting a timeout or similar error
            peer = PeerServer("testuser", 8000)

    def test_peer_server_initialization_valid_port(self):
        server = PeerServer("testuser", 8080)
        assert server.username == "testuser"
        assert server.peerServerPort == 8080

    # Test for PeerServer class initialization with negative port
    def test_peer_server_initialization_negative_port(self):
        with pytest.raises(ValueError):
            PeerServer("testuser", -1)

    # Test for PeerClient class initialization
    def test_peer_client_initialization(self):
        client = PeerClient("127.0.0.1", 8080, "testuser", MagicMock(), None)
        assert client.ipToConnect == "127.0.0.1"
        assert client.portToConnect == 8080

    # Test for PeerClient trying to chat with self
    def test_peer_client_chat_with_self(self):
        server = PeerServer("testuser", 8080)
        client = PeerClient("127.0.0.1", 8080, "testuser", server, None)
        with pytest.raises(ValueError):
            client.run()

    # Mocking network interactions for PeerClient connection
    @patch('socket.socket')
    def test_peer_client_connection(mock_socket):
        client_socket_instance = mock_socket.return_value
        client = PeerClient("127.0.0.1", 8080, "testuser", MagicMock(), None)
        client.run()
        client_socket_instance.connect.assert_called_with(("127.0.0.1", 8080))

    # Mocking network interactions for sending a message in PeerClient
    @patch('socket.socket')
    def test_peer_client_send_message(mock_socket):
        client_socket_instance = mock_socket.return_value
        client = PeerClient("127.0.0.1", 8080, "testuser", MagicMock(), None)
        client.run()
        test_message = "Hello"
        client_socket_instance.send.assert_called_with(test_message.encode())
    # Test for Rapid Peer Churn
    def test_rapid_peer_churn(self):
        peer = PeerServer("testuser", 8000)



    # Test for Network Partitioning

        def test_create_account_success(self, mock_register, mock_input):
            # Mock hashed password for 'test_password'
            hashed_password = self.cli_instance.hash_password('test_pass')

            # Call create_account method, which will read input for username and password
            self.cli_instance.create_account()

            # Check if Register method was called with the correct username and hashed password
            mock_register.assert_called_once_with('test_user', hashed_password)

    if __name__ == '__main__':
        unittest.main()
