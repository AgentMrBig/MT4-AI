# System Architecture Document for MT4-AI Trading System

---

## 1. Introduction

### 1.1 Purpose
The purpose of this document is to provide a detailed overview of the system architecture for the MT4-AI Trading System. It will describe the components, their roles, and interactions within the system, offering a clear blueprint for implementation. This document will complement the System Design Document (SDD) by elaborating on the architectural details necessary to develop and deploy the system.

### 1.2 Scope
This document covers the architectural design of the entire MT4-AI Trading System, which includes the MT4 Expert Advisor (EA), the Machine Learning "Brain," and the web-based monitoring and configuration interface. It will include diagrams and detailed descriptions of how these components interact and work together.

---

## 2. System Overview

### 2.1 High-Level Architecture
The MT4-AI Trading System is composed of three primary components:

1. **MT4 Expert Advisor (EA):**
   - **Role:** Sends live market data from the MT4 platform to the Machine Learning "Brain" and executes trading signals received from it.
   - **Environment:** Runs on the MT4 platform, typically on a Windows-based machine.
   - **Interaction:** Communicates with the "Brain" through a RESTful API.

2. **Machine Learning "Brain":**
   - **Role:** Analyzes market data, generates trading signals, and continuously learns and evolves through genetic algorithms.
   - **Environment:** Hosted on AWS, utilizing services like EC2, S3, and SageMaker.
   - **Interaction:** Receives data from the EA, processes it, and sends back trading signals.

3. **Web Application:**
   - **Role:** Provides an interface for monitoring the system’s performance, configuring parameters, and viewing historical trading data.
   - **Environment:** Hosted on AWS, accessible via modern web browsers.
   - **Interaction:** Communicates with the "Brain" via an API for real-time data, configuration, and monitoring.

### 2.2 Component Interaction Overview
The components interact as follows:
- The **MT4 EA** streams live market data to the **"Brain"**.
- The **"Brain"** processes this data, applies the trading strategy, and sends back trading signals.
- The **Web App** allows users to monitor the system, adjust parameters, and review historical data, interacting directly with the **"Brain"**.

---

## 3. Component Descriptions

### 3.1 MT4 Expert Advisor (EA)
- **Role:** The EA acts as the data collection and execution point within the MT4 platform. It sends real-time market data (such as price, volume, and indicators) to the "Brain" and receives trading signals in return.
- **Responsibilities:**
  - Collecting and streaming real-time data.
  - Executing trades based on signals received.
  - Error handling and recovery in case of communication failures.

### 3.2 Machine Learning "Brain"
- **Role:** The "Brain" is the core analytical engine of the system. It uses pre-trained models to analyze incoming data and make trading decisions. It also evolves its strategy using genetic algorithms based on performance metrics.
- **Responsibilities:**
  - Receiving and processing real-time data from the EA.
  - Generating and sending trading signals.
  - Continuously improving the trading model through genetic algorithms.
- **Key Components:**
  - **Data Analysis Module:** Analyzes incoming data to identify trading opportunities.
  - **Signal Generation Module:** Produces buy/sell signals based on analysis.
  - **Learning Module:** Adjusts and evolves the model using historical data and live feedback.

### 3.3 Web Application
- **Role:** The web application serves as the user interface for the system, allowing for monitoring, configuration, and analysis.
- **Responsibilities:**
  - Displaying real-time and historical trading data.
  - Allowing users to configure trading parameters and strategies.
  - Providing analytics and performance metrics.
- **Key Components:**
  - **Dashboard:** Displays real-time trading data and system status.
  - **Configuration Interface:** Allows users to adjust system parameters.
  - **Analytics Module:** Provides insights into system performance and trade history.

---

## 4. Interaction Diagrams

### 4.1 Sequence Diagram
Below is a sequence diagram representing the interaction between components during a typical trading cycle:

MT4 EA           "Brain"           Web App
 |                 |                 |
 |---Send Data---->|                 |
 |                 |                 |
 |<--Receive Signal|                 |
 |---Execute Trade-|                 |
 |                 |                 |
 |                 |                 |
 |                 |                 |
 |---Send Request->|                 |
 |                 |<--Send Response-|
 |                 |                 |



### 4.2 Component Diagram
The component diagram below shows how the components are organized and interact:

+----------------+        +------------------------+
|  MT4 EA        |<------>|  "Brain"               |
| (Data Stream   |        |  (Data Analysis &      |
|  & Execution)  |        |   Signal Generation)   |
+----------------+        +------------------------+
        |                          |
        |                          |
        v                          v
+----------------+        +------------------------+
|  Web App       |<------>|  "Brain"               |
| (Monitoring    |        |  (Configuration        |
|  & Config)     |        |   & Monitoring)        |
+----------------+        +------------------------+



---

## 5. Data Flow and Storage

### 5.1 Data Flow
- **Live Data Flow:** The MT4 EA sends live market data to the "Brain" using a RESTful API. The "Brain" processes this data and sends trading signals back to the EA.
- **Signal Flow:** Once the "Brain" generates a trading signal, it sends the signal back to the EA, which then executes the trade.
- **Configuration and Monitoring Flow:** The Web App allows users to interact with the "Brain" for configuring trading parameters and monitoring system performance.

### 5.2 Data Storage
- **Historical Data:** Stored in AWS S3 and used for pretraining the AI and running genetic algorithms.
- **Real-Time Data:** Temporarily stored in AWS databases or in-memory for quick access and processing by the "Brain."
- **User Configuration Data:** Stored securely in AWS databases, with access controlled by the Web App.

---

## 6. Security Considerations

### 6.1 Data Security
- **Encryption:** All data transmitted between components (MT4 EA, "Brain", Web App) will be encrypted using SSL/TLS protocols.
- **Access Control:** Role-based access control (RBAC) will be implemented, ensuring that only authorized users can modify critical system parameters or access sensitive data.

### 6.2 System Integrity
- **Authentication:** Multi-factor authentication (MFA) will be required for accessing the Web App and critical AWS resources.
- **Backup and Recovery:** Regular backups of critical data (e.g., user configurations, historical data) will be performed, with a recovery plan in place to handle data loss or system failures.

---

## 7. Conclusion

This System Architecture Document outlines the structural design of the MT4-AI Trading System, detailing the components, their interactions, and data flows. It provides a clear framework for the implementation phase, ensuring that the system is designed with scalability, security, and performance in mind.
