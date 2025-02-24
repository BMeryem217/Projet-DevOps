from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Données initiales pour l'API REST
tasks = [
    {"id": 1, "title": "Faire les courses du ramadan karem", "done": False},
    {"id": 2, "title": "aprrendre devops", "done": True},
]

# Route pour la page d'accueil
@app.route('/')
def home():
    return render_template('index.html')  # Rend le template HTML

# Route pour obtenir toutes les tâches (API REST)
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Route pour obtenir une tâche par son ID (API REST)
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({"error": "Tâche non trouvée"}), 404
    return jsonify(task)

# Route pour ajouter une nouvelle tâche (API REST)
@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = {
        "id": len(tasks) + 1,
        "title": request.json.get('title'),
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# Route pour mettre à jour une tâche (API REST)
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({"error": "Tâche non trouvée"}), 404
    task['title'] = request.json.get('title', task['title'])
    task['done'] = request.json.get('done', task['done'])
    return jsonify(task)

# Route pour supprimer une tâche (API REST)
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({"message": "Tâche supprimée"}), 200

# Démarrer l'application
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)