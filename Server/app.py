import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the API endpoint for updating the bot's information
@app.route('/api/bots/update', methods=['POST'])
def update_bot():
    # Get the bot's information from the request
    bot_id = request.json['id']
    intents = request.json['intents']
    entities = request.json['entities']
    actions = request.json['actions']

    # Connect to the database
    cnx = mysql.connector.connect(user='admin', password='Eigen100%bot',
                                  host='database-1.c5kmzx0rtavj.ap-northeast-1.rds.amazonaws.com',
                                  database='myapp_production_db')
    cursor = cnx.cursor()

    # Update the bot's information in the backend
    update_query = ("""
        UPDATE bots
        SET intents=%s, entities=%s, actions=%s
        WHERE id=%s
    """)
    cursor.execute(update_query, (intents, entities, actions, bot_id))
    cnx.commit()

    # Close the database connection
    cursor.close()
    cnx.close()

    # Return a response indicating that the update was successful
    return jsonify({'message': 'Bot updated successfully'})

if __name__ == '__main__':
    app.run(debug=True)
