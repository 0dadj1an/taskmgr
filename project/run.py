# project/run.py
from views import app
app.run(debug=True,ssl_context='adhoc', host= '192.168.0.252')
