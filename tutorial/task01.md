# Project Task: Member API with Flask

## Goal
Build a small, accessible REST API for managing “members” (e.g., club or course participants). You will practice routing, request/response handling, validation, error management, and (optionally) persistence.

## Task

- 
- Example requests (cURL or Postman collection)

## Core Functionality (MVP)
Implement the following endpoints, always returning JSON:

1. **GET `/members`**  
   - Return a list of all members (with optional pagination: `?page=` & `?per_page=`).
2. **GET `/members/<id>`**  
   - Return a single member by `id` (404 if not found).
3. **POST `/members`**  
   - Create a new member. Required fields: `first_name`, `last_name`, `email`.  
   - Validations: `email` must be valid and unique; names must not be empty.  
   - Response: 201 + created record.
4. **PUT `/members/<id>`**  
   - Full update (all required fields must be present). Response: 200 + updated record.
5. **PATCH `/members/<id>`**  
   - Partial update (only update provided fields). Response: 200 + updated record.
6. **DELETE `/members/<id>`**  
   - Delete the member. Response: 204 (no content).

### Data Model
```json
{
  "id": 1,
  "first_name": "Ada",
  "last_name": "Lovelace",
  "email": "ada@example.org",
  "joined_at": "2025-01-15T10:30:00Z",
  "active": true
}
```
## Technical Requirements
	•	Framework: Flask (3.x API)
	•	Response format: Always application/json; use proper HTTP status codes (200/201/204/400/404/409/422).
	•	Error handling: Consistent schema, e.g.:
```
{ "error": "ValidationError", "message": "email already exists" }
```

## Suggested Project Structure
```
member_api/
  app.py             # Flask app & routes
  models.py          # (optional) database model
  schemas.py         # (optional) validation schema
  README.md
  requirements.txt
```

## Bonus (Optional)
- Search/filter: GET /members?query=ada&active=true
- Sorting: ?sort=last_name&order=asc
- Lightweight Auth
