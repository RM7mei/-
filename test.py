from flask import Flask, request, Markup, abort
import json

app = Flask(__name__)

f = open("C:/python/buff.json",'r')
json_data = json.load(f)
f.close()


@app.route('/')
def index():
	html = '''
    <form action="/test">
        <p><label>test: </label>
        <input type="text" name="query" value="default">
		<input type="text" name="query2" value="default">
		<button type="submit" formmethod="get">GET</button>
        <button type="submit" formmethod="post">POST</button></p>
    </form>
    '''
	return Markup(html)


@app.route('/test', methods=['GET', 'POST'])
def test():
	try:
		if request.method == 'GET':
			print(request.args.get('query',''))
			print(json_data["akiyama"])
			json_data["akiyama"] = {"height":request.args.get('query',''),"position":"ketu"}
			json_data["nisizumi"] = {"height":request.args.get('query2',''),"position":"ketu"}
			with open('C:/python/buff.json','w') as f:
				json.dump(json_data,f,ensure_ascii=False,indent=4)
			return request.args.get('query', '')
		elif request.method == 'POST':
			return request.form['query']
		else:
			return abort(400)
	except Exception as e:
		return str(e)


if __name__ == '__main__':
	app.run()
