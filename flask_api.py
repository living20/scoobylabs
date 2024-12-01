from flask import Flask, request, jsonify
import pandas as pd
import user_input
import scheduler_engine

app = Flask(__name__)

parts_data = []

@app.route('/add_part', methods=['POST'])
def add_part():
    data = request.get_json()
    parts_data.append(data)
    return jsonify({"message": "Part added successfully!"}), 200

@app.route('/schedule', methods=['GET'])
def get_schedule():
    parts_df = pd.DataFrame(parts_data)
    scheduler_engine.schedule_operations(parts_df)
    return jsonify(parts_data), 200

if __name__ == '__main__':
    app.run(debug=True)
