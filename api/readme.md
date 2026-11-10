Image Upload and Metadata Search Goal: Create an image metadata storage service with keyword search support. Endpoints: POST /image  -d {"url": "", "tags": ["cat", "funny", "meme"]}

Stores the image URL and its associated tags (max 10 per image).
Returns 201 on success.

GET /images?tag=

Returns up to 10 image URLs that match the given tag.

Requirements:
SQL database for storage.
Ensure duplicate image URLs aren't allowed.