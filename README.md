# ambit

**Ambit** is a dynamic website built with Django, Python, HTML, and JavaScript, designed to assist volunteers in managing and documenting cat colonies. The platform allows volunteers to upload images and details of colony cats, generating a comprehensive database. This project incorporates various web technologies and libraries, including `cropper.js` for image cropping and `reportlab` for generating PDF reports.

## Features

- **Cat and Colony Models**: 
  - **Cat Model**: Stores details such as name, colony, sterilization status, sociability, age, etc.
  - **Colony Model**: Represents the cat colonies, allowing cats to be associated with their respective colonies.

- **Dynamic Image Uploads**:
  - Volunteers can upload images of cats which are then added to the database.
  - Integrated `cropper.js` library for image cropping before submission.

- **HTML Templates with Jinja2**:
  - Utilizes Jinja2 templating to create a `base.html` template, which other templates extend.
  - Modular and reusable HTML components for efficient development.

- **GET and POST Actions**:
  - Leverages the capabilities of HTML form elements to handle GET and POST requests.
  - No usage of JavaScript HTTP request classes; form submissions manage all interactions.

- **Cat Filtering**:
  - Provides a list view where cats can be filtered based on various form fields, such as name, sterilization status, and colony.

- **PDF Report Generation**:
  - Uses the `reportlab` library to generate a PDF census of the cats within a colony.
  - The PDF includes names, gender, and sterilization status of the cats.
  - PDF is generated server-side and downloaded to the client's browser.

- **Functional-Based Views**:
  - All views are implemented as functional views, avoiding the use of Django's class-based views.

## Technologies and Libraries

- **Django**: Backend framework for handling database operations, routing, and server-side logic.
- **Python**: Core programming language used for backend logic.
- **HTML/CSS**: Markup and styling for the front-end interface.
- **JavaScript**: Client-side scripting for dynamic functionality, including image cropping.
- **Cropper.js**: JavaScript library used for cropping images before they are uploaded.
- **Jinja2**: Template engine used within Django to create modular HTML templates.
- **ReportLab**: Python library for generating PDFs.

## Installation and Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/ambit.git
    cd ambit
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

6. **Access the application**:
    - Open your web browser and navigate to `http://127.0.0.1:8000/`

## Usage

1. **Upload Cat Images**:
   - Navigate to the upload page and submit cat details along with their image.
   - Use the cropping tool to adjust the image before uploading.

2. **View and Filter Cats**:
   - Visit the list view to see all cats in the database.
   - Use the form fields to filter cats based on various attributes.

3. **Generate PDF Reports**:
   - On the colony page, click the "Generate Census PDF" button to download a PDF report of the colony's cats.

## Learning Outcomes

Through developing the Ambit project, I have gained experience and proficiency in:

- **Django Framework**: Building dynamic web applications, creating models, and managing views using Django.
- **Functional Views in Django**: Understanding the benefits and applications of functional views in contrast to class-based views.
- **HTML and Jinja2**: Creating modular, reusable templates using Jinja2 in Django.
- **JavaScript**: Implementing client-side functionality, including image cropping with `cropper.js`.
- **ReportLab**: Generating dynamic PDF documents from server-side data.
- **Web Forms and HTTP Methods**: Utilizing HTML form elements effectively for GET and POST actions, eliminating the need for additional JavaScript for form submissions.
- **Database Management**: Creating and managing complex data models, including one-to-many relationships between colonies and cats.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Cropper.js**: For providing a powerful and user-friendly image cropping library.
- **ReportLab**: For enabling seamless PDF generation.
- The Django community for providing comprehensive documentation and support.

