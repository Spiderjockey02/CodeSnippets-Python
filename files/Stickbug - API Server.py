import random
import os
import string
import urllib.request
from flask import Flask, jsonify, request
from PIL import Image
from gsbl.stick_bug import StickBug

app = Flask(__name__)
opener = urllib.request.build_opener()
opener.addheaders = [(
    'User-Agent',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36'
)]
urllib.request.install_opener(opener)


@app.route('/api/stickbug', methods=['GET'])
def Home():
    id = request.args.get('image')
    if id:
        if id.endswith('.png'):
            name = ''.join(
                random.choice(string.ascii_letters) for i in range(20))
            urllib.request.urlretrieve(id, "C:/Users/benja/Desktop/stickbug-api/images/{yeb}.png".format(yeb=name))
            sb = StickBug(Image.open("C:/Users/benja/Desktop/stickbug-api/images/{yeb}.png".format(yeb=name)))
            sb.save_video("C:/Users/benja/Desktop/stickbug-api/static/{yeb}.mp4".format(yeb=name))
            os.remove("C:/Users/benja/Desktop/stickbug-api/images/{yeb}.png".format(yeb=name))
            return jsonify({
                "success": "true",
                "video": "https://86.25.177.233/static/{yeb}.mp4".format(yeb=name)
            })
        else:
            return jsonify({
                "message": "Image url must end with '.png'",
            })
    else:
        return jsonify({
            "message": "Missing image query",
        })


app.run(host='0.0.0.0', port=443, debug=False)
