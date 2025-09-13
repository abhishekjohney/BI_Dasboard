#!/usr/bin/env python3
"""
Simple HTTP server for the Marketing Intelligence Dashboard
"""
import http.server
import socketserver
import os
import webbrowser
from urllib.parse import quote

class DashboardHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="/home/runner/work/BI_Dasboard/BI_Dasboard", **kwargs)
    
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    PORT = 8000
    
    # Change to the dashboard directory
    os.chdir("/home/runner/work/BI_Dasboard/BI_Dasboard")
    
    print("Marketing Intelligence Dashboard Server")
    print("=" * 50)
    print(f"Starting server on port {PORT}")
    print(f"Dashboard URL: http://localhost:{PORT}")
    print(f"Dashboard files location: {os.getcwd()}")
    print()
    
    # Check if required files exist
    required_files = ['index.html', 'dashboard_data.json']
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file} found")
        else:
            print(f"✗ {file} not found")
    
    print("\nPress Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        with socketserver.TCPServer(("", PORT), DashboardHTTPRequestHandler) as httpd:
            print(f"Server running at http://localhost:{PORT}/")
            print("Open this URL in your web browser to view the dashboard")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except Exception as e:
        print(f"Error starting server: {e}")

if __name__ == "__main__":
    main()