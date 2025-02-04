# Event and Task Management API

This project provides a Flask-based API for managing events and tasks associated with those events. The API supports basic CRUD operations and can be used to create, update, and delete events and tasks.

## API Endpoints

### 1. Event APIs

- `GET /events` - Retrieve all events.
- `GET /event/<id>` - Retrieve a single event by its ID.
- `POST /event` - Create a new event.
- `PUT /event/<id>` - Update an event by its ID.
- `PATCH /event/<id>` - Partially update an event by its ID.
- `DELETE /event/<id>` - Delete an event by its ID.
- `GET /event/<event_id>/tasks` - Retrieve all tasks for a specific event.
- `POST /event/<event_id>/task` - Create a new task for a specific event.
- `DELETE /event/<event_id>/task/<task_id>` - Delete a specific task from a specific event.

### 2. Task APIs

- `GET /tasks` - Retrieve all tasks.
- `GET /task/<id>` - Retrieve a single task by its ID.
- `POST /task` - Create a new task.
- `PUT /task/<id>` - Update a task by its ID.
- `PATCH /task/<id>` - Partially update a task by its ID.
- `DELETE /task/<id>` - Delete a task by its ID.
- `GET /tasks/status/<status>` - Retrieve tasks by their status (e.g., "pending").
- `GET /tasks/event/<event_id>` - Retrieve tasks associated with a specific event.
- `PATCH /task/<task_id>/status` - Update the status of a task.

### 3. Event Filtering/Search APIs

- `GET /events/date/<date>` - Retrieve events on a specific date.
- `GET /events/location/<location>` - Retrieve events in a specific location.
- `GET /events/upcoming` - Retrieve all upcoming events.
- `GET /events/name/<name>` - Retrieve events by their name.

### 4. Task Filtering/Search APIs

- `GET /tasks/event/date/<event_date>` - Retrieve tasks for events happening on a specific date.
- `GET /tasks/overdue` - Retrieve overdue tasks.
- `GET /tasks/name/<name>` - Retrieve tasks by name.

