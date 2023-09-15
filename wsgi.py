# wsgi.py 文件
from api import app
import sys
print(sys.path)

if __name__ == "__main__":
    app.run()
