from flask import Flask

from router import tts_app

import os
import nltk
nltk.data.path.append('nltk_data')

app = Flask(__name__)

app.register_blueprint(tts_app)

#env文件中PORT设置端口号
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)


