from flask import Flask, jsonify, request, abort
import json

app = Flask(__name__)

# Load the data from a JSON file
def load_data():
    with open('data.json', 'r') as file:
        return json.load(file)

# Save data to the JSON file
def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

# ---------- Events APIs ----------

@app.route('/events', methods=['GET'])
def get_events():
    """Get all events"""
    data = load_data()
    return jsonify(data['events'])

@app.route('/event/<int:event_id>', methods=['GET'])
def get_event(event_id):
    """Get event by ID"""
    data = load_data()
    event = next((e for e in data['events'] if e['id'] == event_id), None)
    if event:
        return jsonify(event)
    return abort(404, "Event not found")

@app.route('/event', methods=['POST'])
def create_event():
    """Create a new event"""
    data = load_data()
    new_event = request.get_json()
    new_event['id'] = len(data['events']) + 1
    data['events'].append(new_event)
    save_data(data)
    return jsonify(new_event), 201

@app.route('/event/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    """Update an event"""
    data = load_data()
    updated_event = request.get_json()
    for event in data['events']:
        if event['id'] == event_id:
            event.update(updated_event)
            save_data(data)
            return jsonify(event)
    return abort(404, "Event not found")

@app.route('/event/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    """Delete an event"""
    data = load_data()
    event = next((e for e in data['events'] if e['id'] == event_id), None)
    if event:
        data['events'].remove(event)
        save_data(data)
        return jsonify({"message": "Event deleted"})
    return abort(404, "Event not found")

@app.route('/event/<int:event_id>', methods=['PATCH'])
def partial_update_event(event_id):
    """Partially update an event"""
    data = load_data()
    updated_fields = request.get_json()
    for event in data['events']:
        if event['id'] == event_id:
            event.update(updated_fields)
            save_data(data)
            return jsonify(event)
    return abort(404, "Event not found")

@app.route('/events/date/<date>', methods=['GET'])
def get_events_by_date(date):
    """Get events by date"""
    data = load_data()
    events = [event for event in data['events'] if event['date'] == date]
    return jsonify(events)

@app.route('/events/location/<location>', methods=['GET'])
def get_events_by_location(location):
    """Get events by location"""
    data = load_data()
    events = [event for event in data['events'] if event['location'].lower() == location.lower()]
    return jsonify(events)

@app.route('/events/name/<name>', methods=['GET'])
def get_events_by_name(name):
    """Get events by name (partial match)"""
    data = load_data()
    events = [event for event in data['events'] if name.lower() in event['name'].lower()]
    return jsonify(events)

@app.route('/events/upcoming', methods=['GET'])
def get_upcoming_events():
    """Get upcoming events (events with a future date)"""
    data = load_data()
    upcoming_events = [event for event in data['events'] if event['date'] > '2025-02-04']  # Adjust current date as needed
    return jsonify(upcoming_events)

@app.route('/events/organizer/<organizer>', methods=['GET'])
def get_events_by_organizer(organizer):
    """Get events by organizer"""
    data = load_data()
    events = [event for event in data['events'] if event['organizer'].lower() == organizer.lower()]
    return jsonify(events)

# ---------- Tasks APIs ----------

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    data = load_data()
    return jsonify(data['tasks'])

@app.route('/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get task by ID"""
    data = load_data()
    task = next((t for t in data['tasks'] if t['id'] == task_id), None)
    if task:
        return jsonify(task)
    return abort(404, "Task not found")

@app.route('/task', methods=['POST'])
def create_task():
    """Create a new task"""
    data = load_data()
    new_task = request.get_json()
    new_task['id'] = len(data['tasks']) + 1
    data['tasks'].append(new_task)
    save_data(data)
    return jsonify(new_task), 201

@app.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update a task"""
    data = load_data()
    updated_task = request.get_json()
    for task in data['tasks']:
        if task['id'] == task_id:
            task.update(updated_task)
            save_data(data)
            return jsonify(task)
    return abort(404, "Task not found")

@app.route('/task/<int:task_id>', methods=['PATCH'])
def partial_update_task(task_id):
    """Partially update a task"""
    data = load_data()
    updated_fields = request.get_json()
    for task in data['tasks']:
        if task['id'] == task_id:
            task.update(updated_fields)
            save_data(data)
            return jsonify(task)
    return abort(404, "Task not found")

@app.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    data = load_data()
    task = next((t for t in data['tasks'] if t['id'] == task_id), None)
    if task:
        data['tasks'].remove(task)
        save_data(data)
        return jsonify({"message": "Task deleted"})
    return abort(404, "Task not found")

@app.route('/tasks/status/<status>', methods=['GET'])
def get_tasks_by_status(status):
    """Get tasks by status (pending, in-progress, completed)"""
    data = load_data()
    tasks = [task for task in data['tasks'] if task['status'].lower() == status.lower()]
    return jsonify(tasks)

@app.route('/tasks/event/<int:event_id>', methods=['GET'])
def get_tasks_by_event(event_id):
    """Get all tasks for a specific event"""
    data = load_data()
    tasks = [task for task in data['tasks'] if task['event_id'] == event_id]
    return jsonify(tasks)

@app.route('/tasks/overdue', methods=['GET'])
def get_overdue_tasks():
    """Get overdue tasks (if task deadlines are implemented)"""
    data = load_data()
    overdue_tasks = [task for task in data['tasks'] if task['status'] == 'overdue']
    return jsonify(overdue_tasks)

@app.route('/tasks/priority/<priority>', methods=['GET'])
def get_tasks_by_priority(priority):
    """Get tasks by priority (low, medium, high)"""
    data = load_data()
    tasks = [task for task in data['tasks'] if task['priority'].lower() == priority.lower()]
    return jsonify(tasks)

@app.route('/tasks/search/<string:keyword>', methods=['GET'])
def search_tasks_by_keyword(keyword):
    """Search tasks by keyword"""
    data = load_data()
    tasks = [task for task in data['tasks'] if keyword.lower() in task['description'].lower()]
    return jsonify(tasks)

# ---------- Event-Task Association APIs ----------

@app.route('/event/<int:event_id>/tasks', methods=['GET'])
def get_event_tasks(event_id):
    """Get all tasks for a specific event"""
    data = load_data()
    event = next((e for e in data['events'] if e['id'] == event_id), None)
    if event:
        event_tasks = [task for task in data['tasks'] if task['event_id'] == event_id]
        return jsonify(event_tasks)
    return abort(404, "Event not found")

@app.route('/event/<int:event_id>/task', methods=['POST'])
def create_task_for_event(event_id):
    """Create a new task for a specific event"""
    data = load_data()
    new_task = request.get_json()
    new_task['id'] = len(data['tasks']) + 1
    new_task['event_id'] = event_id
    data['tasks'].append(new_task)
    save_data(data)
    return jsonify(new_task), 201

@app.route('/event/<int:event_id>/task/<int:task_id>', methods=['DELETE'])
def delete_event_task(event_id, task_id):
    """Delete a specific task from a specific event"""
    data = load_data()
    task = next((t for t in data['tasks'] if t['id'] == task_id and t['event_id'] == event_id), None)
    if task:
        data['tasks'].remove(task)
        save_data(data)
        return jsonify({"message": "Task deleted from event"})
    return abort(404, "Task not found or not associated with this event")


if __name__ == '__main__':
    app.run(debug=True)
