import socket
import threading
import os
import json
from urllib.parse import urlparse, unquote
from datetime import datetime

class HTTPServer:
    def __init__(self, host='0.0.0.0', port=8080):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print("Server başlatılıyor...")
        
        # MIME types for different file extensions
        self.mime_types = {
            '.html': 'text/html; charset=utf-8',
            '.css': 'text/css; charset=utf-8',
            '.js': 'application/javascript; charset=utf-8',
            '.json': 'application/json; charset=utf-8',
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.gif': 'image/gif',
            '.ico': 'image/x-icon'
        }

    def start(self):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            
            print("Server çalışıyor...")
            while True:
                try:
                    client_socket, address = self.server_socket.accept()
                    client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
                    client_thread.start()
                except Exception as e:
                    print(f"Error accepting connection: {e}")
        except Exception as e:
            print(f"Error starting server: {e}")
            raise

    def handle_client(self, client_socket):
        try:
            request = client_socket.recv(4096).decode('utf-8')
            if not request:
                print("Boş istek alındı")
                return

            request_lines = request.split('\r\n')
            request_line = request_lines[0]
            method, path, _ = request_line.split(' ')

            self.log_request(method, path)

            if method == 'GET':
                response = self.handle_get_request(path)
            else:
                response = self.create_response(405, 'İzin Verilmeyen Metod')

            client_socket.sendall(response)
        except Exception as e:
            print(f"İstek işlenirken hata: {e}")
            response = self.create_response(500, 'Sunucu Hatası')
            client_socket.sendall(response)
        finally:
            print("İstemci bağlantısı kapatılıyor")
            client_socket.close()

    def handle_get_request(self, path):
        try:
            parsed_path = urlparse(path).path
            decoded_path = unquote(parsed_path)

            if decoded_path == '/api/hello':
                return self.handle_api_hello()
            
            elif decoded_path == '/api/data':
                return self.handle_api_data()
            
            elif decoded_path.startswith('/static/'):
                return self.handle_static_file(decoded_path)
            
            elif decoded_path == '/':
                return self.handle_static_file('/static/index.html')
            
            else:
                return self.create_response(404, 'Sayfa Bulunamadı')
        except Exception as e:
            return self.create_response(500, 'Sunucu Hatası')

    def handle_api_hello(self):
        response_data = {
            'message': 'Merhaba Dünya!',
            'timestamp': datetime.now().isoformat()
        }
        return self.create_response(200, 'OK', json.dumps(response_data, ensure_ascii=False), 'application/json; charset=utf-8')

    def handle_api_data(self):
        try:
            image_path = 'static/marmara.jpg'  
            if not os.path.exists(image_path):
                return self.create_response(404, 'Resim bulunamadı')

            with open(image_path, 'rb') as f:
                image_data = f.read()

            return self.create_response(200, 'OK', image_data, 'image/jpeg')
        except Exception as e:
            print(f"Hata: {e}")
            return self.create_response(500, 'Sunucu Hatası')
        
    
    def handle_static_file(self, path):
        try:
            file_path = path[1:] if path.startswith('/') else path
            if not os.path.exists(file_path):
                print(f"Dosya bulunamadı: {file_path}")
                return self.create_response(404, 'Dosya Bulunamadı')

            _, ext = os.path.splitext(file_path)
            content_type = self.mime_types.get(ext, 'application/octet-stream')

            with open(file_path, 'rb') as f:
                content = f.read()
            return self.create_response(200, 'Tamam', content, content_type)
        
        except Exception as e:
            return self.create_response(500, 'Sunucu Hatası')

    def create_response(self, status_code, status_message, content='', content_type='text/plain; charset=utf-8'):
        
        response = f"HTTP/1.1 {status_code} {status_message}\r\n"
        response += f"Content-Type: {content_type}\r\n"
        
        if isinstance(content, str):
            content = content.encode('utf-8')
        
        response += f"Content-Length: {len(content)}\r\n"
        response += "Connection: close\r\n"
        response += "\r\n"
        
        return response.encode('utf-8') + content

    def log_request(self, method, path):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{timestamp}] {method} {path}")
        
if __name__ == '__main__':
   
    os.makedirs('static', exist_ok=True)
   
    server = HTTPServer()
    server.start() 