# homeharvest-interface
Scrap &amp; Save is a Flask web application for scraping property data and saving it to a CSV file.

# Scrap & Save

Scrap & Save is a Flask web application for scraping property data and saving it to a CSV file.

## Installation

To run the Scrap & Save application locally, follow these steps:

1. Clone this repository to your local machine:
git clone https://github.com/yourusername/scrap-and-save.git

2. Navigate to the project directory:
cd scrap-and-save

3. Create a virtual environment:
python -m venv venv


4. Activate the virtual environment:

- On Windows:

  ```
  venv\Scripts\activate
  ```

- On macOS and Linux:

  ```
  source venv/bin/activate
  ```

5. Install the dependencies:

pip install -r requirements.txt


## Usage

To start the Scrap & Save application, run the following command:

python app.py


Once the application is running, open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the home page.

## Features

- Search for properties by location, past days, and listing type.
- Scrape property data from external sources.
- Save scraped property data to a CSV file.

## Folder Structure

```bash
scrap-and-save/
├── app.py
├── templates/
│ ├── base.html
│ ├── search.html
│ └── result.html
├── homeharvest.py
├── requirements.txt
└── README.md
```

## License

This project is licensed under the [MIT License](LICENSE).

## Author

- [Euxen](https://github.com/Euxen)
