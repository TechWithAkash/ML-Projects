# 🚀 ML Project - Modular Coding

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![MLOps](https://img.shields.io/badge/MLOps-Ready-orange.svg)](https://mlops.org/)

> An end-to-end machine learning project built with modular architecture and industry best practices for scalable, maintainable, and production-ready ML solutions.

## 🎯 Project Overview

This project demonstrates a complete machine learning pipeline using modular coding principles. It's designed to be:
- **Scalable**: Easy to extend with new features and models
- **Maintainable**: Clean, well-documented code structure
- **Production-Ready**: Follows MLOps best practices
- **Reusable**: Components can be reused across different projects

## 📁 Project Structure

```
ML-Project-Modular-Coding/
├── 📂 src/                          # Source code
│   ├── 📂 components/               # Core ML components
│   │   ├── data_ingestion.py        # Data loading and ingestion
│   │   ├── data_transformation.py   # Feature engineering & preprocessing
│   │   └── model_trainer.py         # Model training logic
│   ├── 📂 pipeline/                 # Pipeline orchestration
│   │   ├── train_pipeline.py        # Training pipeline
│   │   └── predict_pipeline.py      # Prediction pipeline
│   ├── exception.py                 # Custom exception handling
│   ├── logger.py                    # Centralized logging
│   └── utils.py                     # Common utility functions
├── 📂 logs/                         # Application logs
├── 📂 venv/                         # Virtual environment
├── requirements.txt                 # Project dependencies
├── setup.py                         # Package setup configuration
├── .gitignore                       # Git ignore rules
└── README.md                        # Project documentation
```

## 🛠️ Tech Stack

- **Language**: Python 3.8+
- **ML Libraries**: scikit-learn, pandas, numpy
- **Logging**: Python logging module
- **Package Management**: pip, setuptools
- **Version Control**: Git

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ML-Project-Modular-Coding.git
   cd ML-Project-Modular-Coding
   ```

2. **Create and activate virtual environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install the package in development mode**
   ```bash
   pip install -e .
   ```

## 📊 Usage

### Training Pipeline

```python
from src.pipeline.train_pipeline import TrainPipeline

# Initialize and run training pipeline
pipeline = TrainPipeline()
pipeline.run()
```

### Prediction Pipeline

```python
from src.pipeline.predict_pipeline import PredictPipeline

# Initialize prediction pipeline
predictor = PredictPipeline()

# Make predictions
predictions = predictor.predict(input_data)
```

### Individual Components

```python
# Data Ingestion
from src.components.data_ingestion import DataIngestion
data_ingestion = DataIngestion()
data_ingestion.initiate_data_ingestion()

# Data Transformation
from src.components.data_transformation import DataTransformation
data_transformation = DataTransformation()
data_transformation.initiate_data_transformation()

# Model Training
from src.components.model_trainer import ModelTrainer
model_trainer = ModelTrainer()
model_trainer.initiate_model_trainer()
```

## 🏗️ Architecture

### Modular Design Principles

1. **Separation of Concerns**: Each component has a single responsibility
2. **Loose Coupling**: Components are independent and interchangeable
3. **High Cohesion**: Related functionality is grouped together
4. **Reusability**: Components can be reused across different projects

### Pipeline Flow

```
Data Ingestion → Data Transformation → Model Training → Model Evaluation → Deployment
```

### Error Handling & Logging

- **Custom Exception Handling**: Consistent error management across all components
- **Centralized Logging**: All activities are logged with timestamps and details
- **Error Tracking**: Detailed error messages with file names and line numbers

## 📈 Features

- ✅ **Modular Architecture**: Easy to extend and maintain
- ✅ **Comprehensive Logging**: Track all operations and errors
- ✅ **Error Handling**: Robust exception management
- ✅ **Pipeline Orchestration**: Automated training and prediction workflows
- ✅ **Data Validation**: Ensure data quality and consistency
- ✅ **Model Versioning**: Track different model versions
- ✅ **Configuration Management**: Centralized configuration handling

## 🧪 Testing

```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_data_ingestion.py

# Run with coverage
python -m pytest --cov=src tests/
```

## 📝 Logging

All operations are logged with different levels:
- **INFO**: General information about the process
- **DEBUG**: Detailed information for debugging
- **WARNING**: Warning messages
- **ERROR**: Error messages with full traceback

Logs are stored in the `logs/` directory with timestamps.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Development Guidelines

- Follow PEP 8 style guidelines
- Write comprehensive docstrings
- Add unit tests for new features
- Update documentation for any changes
- Use meaningful commit messages

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**: Make sure you've installed the package with `pip install -e .`
2. **Path Issues**: Ensure you're running commands from the project root directory
3. **Virtual Environment**: Always activate your virtual environment before running the code

### Getting Help

- Check the logs in the `logs/` directory for detailed error information
- Ensure all dependencies are installed correctly
- Verify Python version compatibility (3.8+)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Akash Vishwakarma**
- Email: vishwakarmaakashav17@gmail.com
- GitHub: [@yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

- Thanks to the open-source community for the amazing tools and libraries
- Inspired by MLOps best practices and industry standards
- Built with ❤️ for the machine learning community

---

⭐ **Star this repository if you find it helpful!** ⭐

For more information, feel free to reach out or open an issue.
