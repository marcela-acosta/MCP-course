# Bootcamp Project: A Hands-On Implementation of a Crypto Price MCP

## Overview

This repository showcases my project from the Udemy course, **"The Hands On MCP (Model Context Protocol) Bootcamp"**. The project is a fully functional implementation of a Model Context Protocol (MCP) designed to allow an AI Agent to query real-time cryptocurrency prices.

The purpose of this repository is to demonstrate my practical skills in integrating external systems with Large Language Models (LLMs) using standardized, modern protocols.

➡️ **Course Credits:** The foundational knowledge and step-by-step guidance for this project were provided by the [MCP Bootcamp: Build, Deploy & Secure Model Context Protocol](https://www.udemy.com/course/learn-mcp-model-context-protocol-course-and-a2a-bootcamphands-hands-on/?referralCode=4BB6FF5CE336B4460CDA) on Udemy.

### Implemented Features

* **MCP Tool Definition:** A formal tool definition for `getCryptoPrice` was created, specifying its input parameters (e.g., `crypto_symbol`) and expected output schema.
* **Multi-Provider LLM Integration:** The MCP was integrated with multiple AI ecosystems, including OpenAI (Agents API, Response API), Anthropic's Claude, and Cursor, demonstrating the protocol's interoperability.
* **Development Environment:** A complete development environment (compatible with Mac & Windows) was configured for building and testing MCPs.
* **Validation and Testing:** The **MCP Inspector** tool was used to debug the interactions between the LLM and the tool, ensuring that requests and responses adhered to the protocol.
* **Deployment-Ready Container:** The MCP service was containerized using Docker, and the final image was published to the [GitHub Package Registry](https://github.com/users/marcela-acosta/packages/container/package/simple-binance-mcp) to simulate a production deployment workflow.
* **Cloud Deployment on AWS:** The container was deployed to a serverless architecture on AWS using Elastic Container Service (ECS) with Fargate. This involved publishing the image to ECR, configuring task definitions, and setting up the necessary security groups.

## Key Technologies and Concepts

This project provided me with hands-on experience in the following areas:

* **Cloud & DevOps:** AWS (ECS, Fargate, ECR), Docker
* **AI Protocols:** Model Context Protocol (MCP)
* **Language Models:** OpenAI, Claude, Cursor
* **Programming Language:** Python (Primary)
* **APIs & External Services:** Integrating with third-party REST APIs
* **Core AI Concepts:**
  * The mechanics of LLM Tool Calling
  * Standardization for LLM interoperability
  * The development and debugging lifecycle of an MCP

## Conclusions & Key Takeaways

Completing this project was an invaluable learning experience. It allowed me to bridge the gap between understanding the theory behind MCPs and implementing a functional solution from the ground up. This exercise solidified my understanding of how to build robust, modular AI applications that are not locked into a single model provider's ecosystem, and provided me with practical, end-to-end experience in deploying a containerized service to a production-ready cloud environment on AWS.
