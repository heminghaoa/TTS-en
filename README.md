# Install

```
$ cd /path/to/your-project
$ python3 -m venv .tts
$ source .tts/bin/activate
pip install -r requirements.txt
pip install --upgrade numpy numba
pip install --no-binary pyuwsgi pyuwsgi
mkdir -p /opt/voices/
cp Voice/SteveJobs.wav /opt/voices/


```
