#!/usr/bin/env python3
"""
Simple HTTP server to serve the Backrooms chatbot locally.
Run this script and open http://localhost:8000 in your browser.
"""

import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

print(f"""
========================================
  BACKROOMS TERMINAL SERVER
========================================

  Server running at: http://localhost:{PORT}

  Press Ctrl+C to stop the server.

========================================
""")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[SERVER TERMINATED]")
