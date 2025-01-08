# Project Overview

This project focuses on detecting and mitigating Denial of Service (DoS) and Distributed Denial of Service (DDoS) attacks using a Python-based system. The solution employs real-time network traffic monitoring, threshold-based detection, and automated IP blocking to ensure network availability and resilience against cyber threats.

## Features

- Real-time traffic analysis and anomaly detection.
- Dynamic IP blocking and unblocking with cooldown periods.
- Automated logging and reporting for forensic analysis.
- High scalability and adaptability for different network configurations.

Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/<username>/dos-ddos-detection.git
    cd dos-ddos-detection
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the main script:
    ```bash
    python src/ddos_detector.py --cooldown 60
    ```

Usage

- Modify thresholds and cooldown parameters in `ddos_detector.py` as needed.
- Use `examples/run_example.sh` to see a demonstration.
- Refer to `docs/report.pdf` for detailed documentation.

Contribution

Feel free to open issues or contribute by submitting pull requests. Ensure all code changes are tested.
