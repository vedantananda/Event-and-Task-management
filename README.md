Flask Event & Task Management API

This project provides a RESTful API for managing events and tasks. It includes endpoints for CRUD operations on both events and tasks, as well as associations between them. The API also supports filtering, searching, and updating operations for both events and tasks.

Features

Event Management
Create, read, update, and delete events.
Filter events by date, location, organizer, and name.
Get upcoming events.
Partially update event details.
Task Management
Create, read, update, and delete tasks.
Filter tasks by status, priority, and deadline.
Search tasks by keywords.
Retrieve tasks by associated event.
Event-Task Associations
Associate tasks with specific events.
Retrieve tasks for a specific event.
Delete tasks from specific events.
Endpoints

Events APIs
1. Get All Events

Endpoint: /events
Method: GET
Description: Retrieve all events.
2. Get Event by ID

Endpoint: /event/<event_id>
Method: GET
Description: Retrieve a specific event by its ID.
3. Create a New Event

Endpoint: /event
Method: POST
Description: Create a new event.
4. Update Event by ID

Endpoint: /event/<event_id>
Method: PUT
Description: Update a specific event by its ID.
5. Delete Event by ID

Endpoint: /event/<event_id>
Method: DELETE
Description: Delete a specific event by its ID.
6. Partially Update Event

Endpoint: /event/<event_id>
Method: PATCH
Description: Partially update an event by its ID (e.g., update only specific fields like name or location).
7. Get Events by Date

Endpoint: /events/date/<date>
Method: GET
Description: Get all events happening on a specific date.
8. Get Events by Location

Endpoint: /events/location/<location>
Method: GET
Description: Get all events held in a specific location.
9. Get Events by Name

Endpoint: /events/name/<name>
Method: GET
Description: Get events by a name (partial match).
10. Get Upcoming Events

Endpoint: /events/upcoming
Method: GET
Description: Get all upcoming events based on the current date.
11. Get Events by Organizer

Endpoint: /events/organizer/<organizer>
Method: GET
Description: Get all events organized by a specific organizer.
Tasks APIs
1. Get All Tasks

Endpoint: /tasks
Method: GET
Description: Retrieve all tasks.
2. Get Task by ID

Endpoint: /task/<task_id>
Method: GET
Description: Retrieve a specific task by its ID.
3. Create a New Task

Endpoint: /task
Method: POST
Description: Create a new task.
4. Update Task by ID

Endpoint: /task/<task_id>
Method: PUT
Description: Update a specific task by its ID.
5. Partially Update Task

Endpoint: /task/<task_id>
Method: PATCH
Description: Partially update a task (e.g., update status or priority).
6. Delete Task by ID

Endpoint: /task/<task_id>
Method: DELETE
Description: Delete a specific task by its ID.
7. Get Tasks by Status

Endpoint: /tasks/status/<status>
Method: GET
Description: Get all tasks with a specific status (pending, in-progress, completed).
8. Get Tasks by Event

Endpoint: /tasks/event/<event_id>
Method: GET
Description: Get all tasks associated with a specific event.
9. Get Overdue Tasks

Endpoint: /tasks/overdue
Method: GET
Description: Get all overdue tasks.
10. Get Tasks by Priority

Endpoint: /tasks/priority/<priority>
Method: GET
Description: Get all tasks with a specific priority (low, medium, high).
11. Search Tasks by Keyword

Endpoint: /tasks/search/<keyword>
Method: GET
Description: Search tasks by keyword in the description.
Event-Task Association APIs
1. Get All Tasks for Event

Endpoint: /event/<event_id>/tasks
Method: GET
Description: Get all tasks associated with a specific event.
2. Create Task for Event

Endpoint: /event/<event_id>/task
Method: POST
Description: Create a new task and associate it with a specific event.
3. Delete Task from Event

Endpoint: /event/<event_id>/task/<task_id>
Method: DELETE
Description: Delete a specific task from an event.
