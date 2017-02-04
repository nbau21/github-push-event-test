from flask import Flask, request, abort
import re, logging

app = Flask(__name__)


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/', methods=['POST', 'GET'])
def webhook():
    if request.method == 'GET' or 'POST':
        response = request.get_json()
        latest_commit = response['commits'][0]
        commit_msg = latest_commit['message']
        branch = response['ref'].replace('refs/heads/', '').strip()
        
        m = re.search('(?<=-)(S|DE)(.*)', branch)
        story_id = m.group(0)
        print('Story ID: %s' % story_id)
        
        if '[BLOCKED]' in commit_msg:
            message = commit_msg.replace('[BLOCKED]', '').strip() 
            print(message)
        else:
            print(commit_msg)
        return '', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
