# model-evalution-metrics
A practical guide to machine learning model evaluation metrics: what they mean, when to use them, and common pitfalls across classification, regression, and forecasting.

---

## Overview

Evaluating a machine learning model is really about answering one question:

**What kind of mistakes is this model allowed to make?**

In many real-world problems—like healthcare, fraud detection, and safety—**most cases are normal**, and only a small number are critical. Because of this, some common metrics can make a model look good even when it fails at what actually matters.

This repository explains evaluation metrics in **plain language**, using everyday examples.

---

## What to learn

- Why some metrics are misleading in real life
- How different metrics focus on different mistakes
- Why one metric is rarely enough
- How to think about model performance beyond a single score

---

## Classification Metrics

### Accuracy

**What it means:**  How often the model is right overall.

**Simple example:**  Accuracy works well when deciding between things that happen equally often, like classifying images of cats and dogs.

**Where it fails:**  In fraud detection or healthcare, most cases are *not* fraud or *not* sick. A model that always predicts “not fraud” or “healthy” will look accurate but be useless.

---

### Precision

**What it means:**  When the model says **“this is fraud”**, how often is it actually fraud?

**Fraud example (simple):**  Imagine a system that flags transactions as fraud.  High precision means that **most flagged transactions truly are fraud**, so customers are not unnecessarily blocked or inconvenienced.

**Why precision matters:**  Low precision means many **not-fraud transactions are wrongly flagged as fraud**, causing frustration, customer complaints, and extra manual review.

**Use precision when:**
- False alarms are expensive
- Blocking normal users causes harm

---

### Recall

**What it means:**  Out of all the **actual fraud cases**, how many did the model catch?

**Fraud example (simple):**  High recall means that **most fraudulent transactions are detected**, even if some normal transactions are flagged too.

**Why recall matters:**  Low recall means **real fraud is slipping through**, leading to financial loss and security risk.

**Use recall when:**
- Missing fraud is more dangerous than flagging extra cases
- Safety and coverage are top priorities

---

### Precision vs Recall (Fraud vs Not-Fraud)

**Simple way to think about it:**
- **Precision focuses on not bothering normal users**
- **Recall focuses on catching as much fraud as possible**

A strict system may block fewer normal users (high precision) but miss fraud (low recall).  
An aggressive system may catch most fraud (high recall) but inconvenience more users (lower precision).

The right balance depends on business risk and tolerance.

---

### F1 Score

**What it means:**  A balance between precision and recall.

**Simple example:**  F1 score is useful in fraud systems where **both missing fraud and blocking normal users are bad**, and you want a single score to represent that balance.

**Limitation:**  
It does not tell you *which* mistake happens more often.

---

### ROC-AUC

**What it means:**  How well the model separates fraud from not-fraud across different thresholds.

**Simple example:**  Helpful when comparing multiple fraud models before deciding how strict the system should be.

**Watch out:**  It can look strong even if the model struggles with rare fraud cases.

---

### PR-AUC

**What it means:**  How well the model handles fraud detection when fraud is rare.

**Simple example:**  PR-AUC gives a clearer picture of fraud-catching ability when most transactions are not fraud.

---

### Log Loss

**What it means:**  
How confident and accurate
