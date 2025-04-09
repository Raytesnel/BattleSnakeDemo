# BattleSnakeDemo

A demo script for battlesnake with FastApi and Pydantic

## Installation

1. Clone the repository:
2. Install dependencies
   - using pip: pip install -r requirements.txt
   - using uv: uv sync
3. Run the server:
   - uvicorn main:app --reload
4. Open your browser and go to <http://localhost:8000/docs> to check the API documentation.
5. Run the local hosting script:
   - download the hosting script <https://github.com/BattlesnakeOfficial/rules/releases>
   - run the script with the client and name filled in
      - for solo testing `battlesnake play -W 11 -H 11 --name <SNAKE_NAME> --url <SNAKE_URL> -g solo -v --browser`
      - for multiplayer `battlesnake play -W 11 -H 11 --name Snake1 --url http://snake1-url-whatever --name Snake2 --url http://snake2-url-whatever --browser`
6. See the result in browser