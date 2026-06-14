import json
from http.server import BaseHTTPRequestHandler, HTTPServer
FINGERPRINT = {
    "files": [
        {"sha":"644e2be244bb3b68f3d52e6ddd5d8b8d2f9542c1","file":"data/about.csv","checksum":"1a1e42f1"},
        {"sha":"c622a919596f4ceb75edbe03748152503c966125","file":"data/ai_units.csv","checksum":"52533b6c"},
        {"sha":"85231df76ffefe3b666024ab921b2f73cf868028","file":"data/avatar.csv","checksum":"c00bbdd7"},
        {"sha":"f0494b2f6e51122e6801d5a422906390e0f0ee33","file":"data/billing_packages.csv","checksum":"6d6767af"},
        {"sha":"eeb166d9135fcfaa550020a5e0672d5c0aefd5bd","file":"data/credits.csv","checksum":"add03621"},
        {"sha":"f230d4b57f6d2f62b511046ca5cbe2e886ce2685","file":"data/cutscene.csv","checksum":"85af02b5"},
        {"sha":"7ee1fded70312742778d83658e237ecf9acb30fb","file":"data/gadget.csv","checksum":"eee68b3e"},
        {"sha":"4d146189e78e306902f8bd80b18cfab7fd4ae5de","file":"data/game_const.csv","checksum":"f3af6035"},
        {"sha":"6ce17a066e5392afa43a7488f85a37bb72c38de5","file":"data/gamelevel.csv","checksum":"eed3c8cc"},
        {"sha":"0626f2b4f8efe5baaa71aa7725aaee63bff02004","file":"data/gui.csv","checksum":"1888eeff"},
        {"sha":"8bb90b0e938954caaee427e3fda0b6d5418358a2","file":"data/handbook.csv","checksum":"1a8c5af1"},
        {"sha":"dc98e0f01b79e9de44398d5eb37a19f65aff5214","file":"data/inboxmessage.csv","checksum":"faa68755"},
        {"sha":"fb498f23ee5c25708792d9aaa3a7897b5ea783e7","file":"data/item.csv","checksum":"bbf1957f"},
        {"sha":"d2de8480c2c3db124e4b533e5eb7e5a23feab673","file":"data/lang.csv","checksum":"2c8d8cf1"},
        {"sha":"25d024081fcf63d32a6acec7c5c224148a99439c","file":"data/lang_de.csv","checksum":"a03d295"},
        {"sha":"f05696522db44746f0736c63d6dd3aa2438fdff6","file":"data/lang_es.csv","checksum":"152e5273"},
        {"sha":"3f99dd0919857d3181d837e30128bf3c2b3267a7","file":"data/lang_fi.csv","checksum":"70d28372"},
        {"sha":"62380592a4067f1d7d70af24fc73219421da3582","file":"data/lang_fr.csv","checksum":"6f95ef82"},
        {"sha":"1cb9c375fba2829ee6a4de6de1b22c6adbab8af6","file":"data/lang_it.csv","checksum":"85c1e297"},
        {"sha":"b1b6d3f2b6d24707640e5552cd641f84d9a1b39e","file":"data/lang_nl.csv","checksum":"24819fb0"},
        {"sha":"29f136fa51e31a332320ca148b3411f3f9191e2f","file":"data/lang_no.csv","checksum":"385e886d"},
        {"sha":"e1eec710fd242eb0108664b9234046df7409fe6b","file":"data/lang_pt.csv","checksum":"836fee94"},
        {"sha":"a44aa8244a5ac04d81c77287556caa482b6c9bde","file":"data/lang_tr.csv","checksum":"b8a4ff6c"},
        {"sha":"fd90521f0dbc61ede120a6b666f6f3223813a427","file":"data/leagues.csv","checksum":"eaccda68"},
        {"sha":"28236bd70ba0f71cab78b2b6b9a3cb5e776d5f80","file":"data/level.csv","checksum":"24fcd3af"},
        {"sha":"f6041a44d1e634dcc3745a7d928ddb09abc03021","file":"data/mission.csv","checksum":"62ef095e"},
        {"sha":"5d066ed4fbe7147c9b0ef1fc42713a868e573ad3","file":"data/mission_tree.csv","checksum":"bb34f1ce"},
        {"sha":"ab795ce57bd205ae3f93a4260e9c37d78ad9036d","file":"data/moneybag.csv","checksum":"c7bee935"},
        {"sha":"a8e4643f7157624432b6066e4d09d3722c40c4f3","file":"data/readingtimes.csv","checksum":"1e7bdc9b"},
        {"sha":"3cc5ab1fb55a9825b8a583bbb9c457c2f89cbdc4","file":"data/shop.csv","checksum":"69644be1"},
        {"sha":"3acc090638669c5e2d883fa932f39a6fd47d54d9","file":"data/skill.csv","checksum":"2a42f860"},
        {"sha":"8a20d74dbe17cf6a9ac8d74dcdc70531e9c02b3e","file":"data/sounds.csv","checksum":"50e2e4cf"},
        {"sha":"70127eade93c26a5d2f760132edf094c428b7d1d","file":"data/sounds_ipad1.csv","checksum":"e5845bda"},
        {"sha":"3b5047a6c8fab85bb8b0b313b8faabd61151bea1","file":"data/speedup.csv","checksum":"c96ef3ea"},
        {"sha":"1388ecfea65b98d1e9e4be785dac1a8a5964df57","file":"data/trainingtimes.csv","checksum":"811f4bd1"},
        {"sha":"a3055faddd0a1eff4f4da59df958235e3e5521c9","file":"data/unit.csv","checksum":"3c1ba78c"},
        {"sha":"6d37f4b27604df00c356e6776c6639b2e06a3669","file":"data/upgrade.csv","checksum":"e5f57998"},
        {"sha":"0f58dfaf958fc79773111a20bd7af4ef78bbe172","file":"data/weapon.csv","checksum":"2c66dd25"},
        {"sha":"20502c013b86a05e9faa3571d524824f081a5e0a","file":"gut.ini","checksum":"5b67908b"},
        {"sha":"2a31a8c726840451e3bbaf6581e808220573049a","file":"gut_ipad2.ini","checksum":"e479cefc"},
        {"sha":"2a31a8c726840451e3bbaf6581e808220573049a","file":"gut_ipad3.ini","checksum":"e479cefc"},
        {"sha":"baad61c9281978fcd2193f1b718213ac5597777b","file":"gut_iphone3.ini","checksum":"5483cd1f"},
        {"sha":"baad61c9281978fcd2193f1b718213ac5597777b","file":"gut_iphone4.ini","checksum":"5483cd1f"}
    ],
    "sha": "cca48b3dea87dda99dceeeba7975cdd2f22183aa"
}

PATH = "/cca48b3dea87dda99dceeeba7975cdd2f22183aa/fingerprint.json"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith("fingerprint.json"):
            body = json.dumps(FINGERPRINT, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()

def run():
    print(f"Starting server on http://0.0.0.0:80")
    print(f"Endpoint: http://localhost:80{PATH}")
    server = HTTPServer(("0.0.0.0", 80), Handler)
    server.serve_forever()