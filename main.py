from flask import Flask, request, jsonify
from hsn_validator import HSNValidator

app = Flask(__name__)
validator = HSNValidator('HSN_Master_Data.csv')

@app.route('/validate', methods=['POST'])
def validate():
    data = request.json
    codes = data.get("codes", [])
    response = []

    for code in codes:
        result = validator.validate_code(code)
        response.append(result)

    return jsonify(response)

@app.route('/hierarchy', methods=['POST'])
def validate_hierarchy():
    data = request.json
    code = data.get("code", "")
    result = validator.hierarchical_validation(code)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
