import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# لیست کتاب‌ها در بک‌اند پایتون
books = [
    {
        "title": "پایتون پیشرفته (از سرور خودم!)",
        "price": "390,000",
        "description": "این کارت زنده از سرور پایتون داخل گوشی تو آمده است!"
    },
    {
        "title": "معماری میکروسرویس با .NET",
        "price": "520,000",
        "description": "ارتباط واقعی فرانت‌اند و بک‌اند (Fullstack)"
    },
    {
    "title":"طراحی سایت با React و پایتون",
    "price": "500,000",
    "description": "طراحی سایت های آماده"
    }
]

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        data = json.dumps(books, ensure_ascii=False)
        self.wfile.write(data.encode("utf-8"))

print("سرور پایتون روشن شد! در حال گوش دادن به پورت 8000...")
HTTPServer(("", 8000), MyServer).serve_forever()