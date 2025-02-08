# Promaiden

## Overview

Promaiden is an automated reporting tool that integrates **Prometheus** for metric collection and **ChatGPT** for analysis, generating structured performance reports. It helps system administrators, SREs, and DevOps engineers gain insights into infrastructure health and performance.

## Features

- **Queries Prometheus** for key system metrics
- **Analyzes data with ChatGPT** to provide structured reports
- **Supports modular design** for easy extensibility
- **Generates formatted reports** for production meetings
- **Logs detailed execution steps** for transparency
- **GitHub Actions support for automation**
- **Version tagging for releases**

## Installation

### Prerequisites

- Python 3.8+
- Prometheus instance running
- OpenAI API key
- Git installed

### Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/bit-bot-bit/promaiden.git
   cd promaiden
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up the OpenAI API key:
   ```sh
   export OPENAI_API_KEY="your_openai_api_key"
   ```
   Or create a `.env` file with:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

## Configuration

Modify `config.json` to specify Prometheus URL, query time ranges, and metrics:

```json
{
  "service_name": "Example Service",
  "prometheus_url": "http://localhost:9090/api/v1/query",
  "start_time": "now-6h",
  "end_time": "now",
  "metrics": [
    "up",
    "process_uptime_seconds",
    "sum(rate(node_cpu_seconds_total[5m])) by (mode)",
    "node_memory_Available_bytes"
  ]
}
```

## Usage

Run Promaiden with:

```sh
python promaiden.py
```

This will:

1. Fetch Prometheus metrics
2. Analyze them using ChatGPT
3. Generate a structured report in `performance_report.txt`

## Logging

Logs are printed to the console and can be redirected to a file:

```sh
python promaiden.py > promaiden.log 2>&1
```

## GitHub Repository

Promaiden is hosted on GitHub: [bit-bot-bit/promaiden](https://github.com/bit-bot-bit/promaiden)

### Contributing

1. **Fork the repository** on GitHub
2. **Create a feature branch** (`git checkout -b feature-branch`)
3. **Commit your changes** (`git commit -m "Add new feature"`)
4. **Push to your branch** (`git push origin feature-branch`)
5. **Submit a pull request** on GitHub

### Issues & Discussions

- **Report bugs and feature requests** in the [GitHub Issues](https://github.com/bit-bot-bit/promaiden/issues)
- **Discuss improvements and ideas** in [GitHub Discussions](https://github.com/bit-bot-bit/promaiden/discussions)

## Automation with GitHub Actions

We plan to integrate **GitHub Actions** to automate:

- **Code formatting checks**
- **Unit testing**
- **Automatic deployment**

## Releases

- **Version tagging** (`v1.0.0`, `v1.1.0`) will be used for stable releases
- Future releases will be listed under the [GitHub Releases](https://github.com/bit-bot-bit/promaiden/releases) page

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Future Enhancements

- Support for multiple AI models
- Real-time dashboard integration
- Alert-based automated reports

