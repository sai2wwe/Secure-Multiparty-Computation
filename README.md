# Secure Multi-Party Computation (MPC)

## Overview
This project demonstrates the implementation of **Secure Multi-Party Computation (MPC)**, allowing multiple participants to collaboratively compute functions (such as addition and average) over their private inputs without revealing the actual inputs. The implementation ensures privacy using cryptographic principles, making it suitable for scenarios where data confidentiality is critical.

---

## Features
- **MPC Addition**: Securely computes the sum of participants' inputs.
- **MPC Average**: Computes the average of participants' inputs securely.
- **Cryptographically Secure Randomness**: Utilizes Python's `secrets` module for secure random number generation.
- **Scalable Architecture**: Modular and extensible codebase to support additional MPC operations.
- **Logging**: Provides detailed logging of the computation process for transparency.

---

## How It Works
1. Each participant's input is split into **random shares** using modular arithmetic.
2. These shares are distributed across multiple parties, ensuring no single party knows the original input.
3. Each party performs partial computations on its shares.
4. The results from all parties are aggregated to compute the final result (e.g., sum, average) without revealing the individual inputs.

---
