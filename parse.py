from datanashor.parser import ReplayParser

parser = ReplayParser(current_game_version='12.21', train=True,
                      train_api_root='http://54.180.126.43/api/v1/train_game/upload_json', serial_port='COM?????<-이거꼭바꿔라')
parser.parse()
