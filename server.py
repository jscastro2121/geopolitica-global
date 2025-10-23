# ===============================================
# Servidor local com suporte a includes (Geopolítica Global)
# ===============================================

from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
import re

class SSIRequestHandler(SimpleHTTPRequestHandler):
    def send_head(self):
        path = self.translate_path(self.path)
        if path.endswith('.html') and os.path.exists(path):
            with open(path, encoding='utf-8') as f:
                content = f.read()

            # Processa includes: <!--#include virtual="caminho" -->
            pattern = re.compile(r'<!--\s*#include\s+virtual\s*=\s*"([^"]+)"\s*-->')


            def replace_include(match):
                include_path = match.group(1).replace('/', os.sep)
                include_full_path = os.path.join(os.getcwd(), include_path)
                if os.path.exists(include_full_path):
                    with open(include_full_path, encoding='utf-8') as inc:
                        return inc.read()
                else:
                    return f"<!-- include não encontrado: {include_path} -->"

            content = pattern.sub(replace_include, content)
            print(f"[DEBUG] Incluindo: {path}")

            encoded = content.encode('utf-8')
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(encoded)))
            self.end_headers()
            self.wfile.write(encoded)
            print(f"[DEBUG] Conteúdo final de {path} com {len(content)} bytes")

            return None
        else:
            return super().send_head()

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), SSIRequestHandler)
    print("Servidor SSI ativo em http://localhost:8000")
    server.serve_forever()
