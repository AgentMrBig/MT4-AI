# Software Requirements Specification (SRS) for MT4-AI Trading System

## 1. Introduction

### 1.1 Purpose
This document outlines the Software Requirements Specification (SRS) for a Machine Learning (ML) and AI-based trading system that integrates with MetaTrader 4 (MT4) to analyze and execute trades on the USD/JPY currency pair. The system will be hosted on AWS and leverage historical data to pre-train the ML models. The system's "Brain" will continuously learn and adapt using a genetic algorithm to optimize trading strategies, particularly focusing on scalping the 1-minute chart.

### 1.2 Scope
The system will consist of the following components:
- **MT4 EA (Expert Advisor):** Responsible for sending live market data to the "Brain" and executing trading signals received from the "Brain."
- **Machine Learning "Brain":** A system trained on historical data, designed to analyze market data and generate trading signals. It will improve its performance over time using a genetic algorithm.
- **Web Application:** A platform for monitoring, controlling, and analyzing the performance of the trading system. It will integrate multiple AI components for comprehensive market analysis.

### 1.3 Definitions, Acronyms, and Abbreviations
- **MT4:** MetaTrader 4, a trading platform.
- **EA:** Expert Advisor, an automated trading script for MT4.
- **ML:** Machine Learning.
- **AWS:** Amazon Web Services.
- **SRS:** Software Requirements Specification.
- **Genetic Algorithm:** An optimization algorithm based on the principles of natural selection and genetics.

### 1.4 References
- MetaTrader 4 Documentation
- AWS Machine Learning Documentation
- Historical Forex Data Repositories

## 2. Overall Description

### 2.1 Product Perspective
The trading system will be built as a distributed system, where the MT4 EA acts as the data provider and executor, while the "Brain" resides on AWS, performing data analysis, signal generation, and continuous learning. The web app will serve as the control center for the system.

### 2.2 Product Functions
- **Data Collection:** The MT4 EA will stream live market data (e.g., price, volume) to the "Brain" via a secure API.
- **Data Analysis:** The "Brain" will process incoming data, analyze historical patterns, and generate trading signals.
- **Signal Execution:** The MT4 EA will receive trading signals from the "Brain" and execute trades on the USD/JPY pair.
- **Learning and Optimization:** The "Brain" will use a genetic algorithm to optimize its trading strategy based on past performance and repeated simulations.
- **Web Interface:** A user-friendly web app will allow users to monitor system performance, view historical data, and configure the "Brain's" parameters.

### 2.3 User Classes and Characteristics
- **Traders:** Users who will monitor the system, adjust parameters, and receive trading insights.
- **Developers:** Technical users responsible for maintaining the system and improving its algorithms.
- **Administrators:** Users responsible for managing the AWS infrastructure and ensuring the system’s security and reliability.

### 2.4 Operating Environment
- **MT4 EA:** Runs on Windows-based MetaTrader 4 platform.
- **"Brain":** Hosted on AWS, leveraging EC2, S3, and other AWS services for computation, storage, and machine learning.
- **Web App:** Accessible via modern web browsers, hosted on AWS.

### 2.5 Design and Implementation Constraints
- **Real-Time Data Processing:** The system must handle and process market data in real-time with minimal latency.
- **Scalability:** The "Brain" should be able to scale with increasing data loads and computational demands.
- **Security:** Secure data transmission between MT4 EA and the "Brain" is crucial.

### 2.6 Assumptions and Dependencies
- **AWS Services:** The system assumes the availability of AWS services like EC2, S3, and SageMaker.
- **MT4 Platform:** The system relies on the MT4 platform for executing trades and streaming market data.

## 3. Specific Requirements

### 3.1 Functional Requirements
- **FR1: Data Streaming**
  - The MT4 EA shall stream live market data (price, volume, etc.) to the "Brain" every minute.
  
- **FR2: Signal Generation**
  - The "Brain" shall analyze incoming data and generate buy/sell signals based on pre-trained models.

- **FR3: Signal Execution**
  - The MT4 EA shall execute trading signals received from the "Brain" immediately on the USD/JPY pair.

- **FR4: Pre-Training the "Brain"**
  - The system shall allow pre-training of the "Brain" using historical USD/JPY data before live deployment.

- **FR5: Genetic Algorithm Optimization**
  - The "Brain" shall run a genetic algorithm to optimize trading strategies, retraining on simulated historical data to improve performance.

- **FR6: Web App Monitoring**
  - The web app shall provide real-time monitoring of the system’s performance, display trading history, and allow configuration of trading parameters.

### 3.2 Non-Functional Requirements
- **NFR1: Performance**
  - The system shall process and analyze market data within 1 second of receipt to ensure timely signal generation.

- **NFR2: Scalability**
  - The system shall be able to scale horizontally to handle increased data loads and additional computational tasks.

- **NFR3: Security**
  - Data transmission between MT4 and the "Brain" shall be encrypted using SSL/TLS protocols.

- **NFR4: Availability**
  - The system shall maintain 99.9% uptime, ensuring continuous operation during market hours.

### 3.3 Interface Requirements
- **IR1: MT4 EA to Brain API**
  - The MT4 EA shall communicate with the "Brain" via a RESTful API hosted on AWS.

- **IR2: Web App to Brain API**
  - The web app shall interface with the "Brain" via a secure API to retrieve data and manage configurations.

### 3.4 System Models
- **Data Flow Diagram:** Depicts the flow of data between MT4 EA, the "Brain," and the web app.
- **Entity-Relationship Diagram:** Shows the relationship between different components within the system.

### 3.5 Testing Requirements
- **TR1: Unit Testing**
  - Each component of the system shall undergo unit testing to verify functionality.
  
- **TR2: Integration Testing**
  - The system shall undergo integration testing to ensure that all components work together as expected.

- **TR3: Performance Testing**
  - The system shall be tested under simulated market conditions to ensure it meets performance requirements.

## 4. Appendices

### 4.1 Glossary
- **Scalping:** A trading strategy that aims to profit from small price changes.
- **Genetic Algorithm:** An algorithm that simulates the process of natural selection to optimize solutions.

### 4.2 References
- AWS Machine Learning Documentation
- MetaTrader 4 Expert Advisor Documentation
- Historical Data for USD/JPY (e.g., from Dukascopy or similar providers)
