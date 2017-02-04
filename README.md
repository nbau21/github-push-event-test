# Rally - Github Integration
Upon pushing to a branch, commit messages annotated with `[BLOCKED]` will automatically mark the relevant story as blocked and add the remaining commit message as the blocker's description.

This tool is not connected (yet) to Github or Rally, but I've included sample push events from Github.

# Installation
* Run `pip install -r requirements.txt`

# Usage
Start the app with `python app.py`.

I've included `red_sample.json` (blocked story) and `green_sample.json` (good story). To test each scenario, open another terminal, navigate to the project's folder, and run:

Request:
`curl -H "Content-Type: application/json" -X POST -d @red_sample.json localhost:5000`

Response:

    Story ID: DE444
    Need endpoints from MBAAS


Request:
`curl -H "Content-Type: application/json" -X POST -d @green_sample.json localhost:5000`

Response:
    
    Story ID: S1221 
    Implement latest designs from Danny
