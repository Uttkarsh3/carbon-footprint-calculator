from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path='/static')

# List to store previous calculations
previous_calculations = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    usage_hours = int(request.form['usage_hours'])
    compute_energy = usage_hours * 0.5
    storage_energy = usage_hours * 0.2
    network_energy = usage_hours * 0.1
    total_energy = compute_energy + storage_energy + network_energy
    carbon_footprint = total_energy * 0.5

    if usage_hours <= 5:
        message = "Great job! Your emissions are very low. Keep up the good work!"
    elif usage_hours <= 10:
        message = "Your emissions are moderate. Consider optimizing your usage for further reduction."
    elif usage_hours <= 20:
        message = "Your emissions are quite high. Try to optimize your usage to reduce your carbon footprint."
    else:
        message = "Your emissions are very high. Significant optimization is needed to reduce your impact."

    # Store calculation data
    calculation_data = {
        'compute_energy': compute_energy,
        'storage_energy': storage_energy,
        'network_energy': network_energy,
        'total_energy': total_energy,
        'carbon_footprint': carbon_footprint,
        'message': message
    }
    previous_calculations.append(calculation_data)

    return jsonify(calculation_data)

if __name__ == '__main__':
    app.run(debug=True)
