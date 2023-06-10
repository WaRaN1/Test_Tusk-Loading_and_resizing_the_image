# Image Optimization API

This is an HTTP API for uploading, optimizing, and serving images. The API allows users to upload images, which are then optimized using a Python library and saved in different quality variants. Users can download the optimized images by specifying the desired quality level.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with the Image Optimization API, follow these steps:

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/MontyPython-ManuL/-.git
   ```

2. Install the required dependencies by running the following command:
   ```
   cd web_app_img
   poetry install
   ```

3. Configure the database and other settings by editing.

4. Start the server by running the following command:
   ```
   python manage.py runserver
   ```
5. Start the worker by running the following command if you use windows:
   ```
   celery -A web_app_img worker -l info --concurrency 4 -P eventlet

   ```
   or other OS:
   ```
   celery -A web_app_img worker -l info
   ```
6. Flower monitoring tool:
   ```
   celery flower --port=5566
   ```

## Usage

### Uploading an Image

To upload an image, send a `POST` request to the `/upload-image/` endpoint. Include the image file in the request body. The API will enqueue the image for optimization to ensure efficient processing.

Example request using cURL:
```
curl -X POST -F "file=@/path/to/image.jpg" http://localhost:8000/upload-image/
```

### Downloading an Optimized Image

To download an optimized image, send a `GET` request to the `/download-image/` endpoint. Specify the image ID and the desired quality level as query parameters (`id` and `quality`).

Example request:
```
GET /download-image/?id=123&quality=75
```

### API Responses

The API returns JSON responses with appropriate status codes. Successful responses will include the URL to download the optimized image.

Example response:
```json
{
  "message": "Image uploaded and sent for optimization. Choose your quality level in the URL: 25, 50, 75, 100",
  "file_url": "http://localhost:8000/download-image/?id=123&quality=75"
}
```

## Contributing

Contributions to the Image Optimization API are welcome! If you have any ideas, suggestions, or bug reports, please open an issue on the [GitHub repository](https://github.com/your-username/image-optimization-api/issues).

To contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Implement your changes.
4. Write tests to ensure code quality and correctness.
5. Commit your changes and push them to your fork.
6. Submit a pull request explaining your changes.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and use the code for your own purposes.