# Flower4all - Flower Framework Tutorial Series

[![GitHub issues](https://img.shields.io/github/issues/aintburak/Flower4all?style=for-the-badge&labelColor=blue)](https://github.com/aintburak/Flower4all/issues) [![GitHub pull requests](https://img.shields.io/github/issues-pr/aintburak/Flower4all?style=for-the-badge&labelColor=green)](https://github.com/aintburak/Flower4all/pulls)  [![GitHub stars](https://img.shields.io/github/stars/aintburak/Flower4all?style=for-the-badge&labelColor=yellow)](https://github.com/aintburak/Flower4all/stargazers)  [![GitHub forks](https://img.shields.io/github/forks/aintburak/Flower4all?style=for-the-badge&labelColor=orange)](https://github.com/aintburak/Flower4all/forks)  ![GitHub](https://img.shields.io/github/license/aintburak/Flower4all?style=for-the-badge)

###### tags: `Python` `Flower Framework` `Federated Learning`  

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Flower4all</h3>
  <div align="center">
    A tutorial series on Flower Framework for federated learning.
    <br />
    <a href="https://github.com/aintburak/Flower4all">Repository Link</a>
    ·
    <a href="https://github.com/aintburak/Flower4all/issues">Report Bug</a>
    ·
    <a href="https://github.com/aintburak/Flower4all/pulls">Contribute</a>
  </div>
</div>

---

## :tada: Welcome to Flower4all!
<!-- Add an introductory paragraph about the repository and its purpose. -->

### :book: Table of Contents
<!-- Add links to each section. -->

1. [Getting Started](#getting-started)
2. [What is Federated Learning?](#what-is-federated-learning)
3. [What is Flower Framework?](#what-is-flower-framework)
4. [Contribution](#contribution)
5. [License](#license)
6. [References](#references)

---
<!--
## :pushpin: **Checklist**
- [x] 📦 Getting Started
- [x] 👩🏻‍💻 What is Federated Learning?
- [x] 🚀 What is Flower Framework?
- [x] 🔨 Contribution
- [x] 🧾 License
- [x] 📚 References
-->

# Flower4all - Flower Framework Tutorial Series

Welcome to Flower4all, a tutorial series repository dedicated to exploring the Flower framework for federated learning. This repository contains several Python flower projects utilizing libraries such as Pandas, NumPy, and leveraging one of the flower datasets, MNIST. 

## Getting Started
To get started with Flower4all tutorials, navigate to the project of your interest within this repository. Each tutorial typically includes at least one `client.py` and one `server.py`. 

### Note on Federated Learning
In Federated Learning, the server should be run before `client.py`. Please ensure you run the server script first before the client script to avoid any issues.

## What is Federated Learning?
Federated Learning is a machine learning approach that allows for training on decentralized data sources, such as mobile devices, without the need to directly access raw data. Instead, model training occurs locally on each device, and only model updates are shared with a central server or aggregator. This preserves data privacy and reduces communication overhead.

## What is Flower Framework?
Flower (Federated Learning with Multi-task Privacy) is an open-source Python framework for federated learning. It simplifies the process of building federated learning systems by providing high-level abstractions and utilities for communication, aggregation, and orchestration of federated learning tasks.

## Contribution
Contributions to Flower4all are welcome! If you find any bugs, have feature requests, or want to contribute enhancements, please feel free to open an issue or submit a pull request.

### How to Contribute
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## References
- Flower Framework: [Official Documentation](https://flower.dev/)
- Federated Learning: [Research Paper](https://arxiv.org/abs/1602.05629)
