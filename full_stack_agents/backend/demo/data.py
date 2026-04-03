BEGINNER_EXAMPLES = [
    {
        "id": "1",
        "text": "Public libraries are important resources for everyone in the city.",
        "label": "no_hate_speech",
    },
    {
        "id": "2",
        "text": "That country is less intelligent and incapable of contributing to society.",
        "label": "hate_speech",
    },
    {
        "id": "3",
        "text": "People from that race are all untrustworthy and should not be allowed to work in public jobs.",
        "label": "hate_speech",
    },
]

BEGINNER_REASONING = {
    "hate_speech": (
        "The text contains language that targets a group based on protected attributes "
        "such as race, ethnicity, or nationality. It uses dehumanizing generalizations "
        "and promotes discrimination, which constitutes hate speech."
    ),
    "no_hate_speech": (
        "The text discusses a neutral topic without targeting any group or individual "
        "based on protected attributes. There are no threats, insults, or discriminatory "
        "language present."
    ),
}

INTERMEDIATE_REPORTS = {
    "log_analysis": """\
Analysis Report:

- Primary Issue Description:
  The primary issue in this deployment is a failure to pull the Docker image "myapp:v1.2.3" from the repository, which results in the deployment not progressing and ultimately rolling back to a previous version.

- Key Error Messages and Codes:
  1. Pod myapp-deployment-7b8c9d5f4-abc12 failed to start
  2. Failed to pull image "myapp:v1.2.3": rpc error: code = Unknown desc = Error response from daemon: pull access denied for myapp, repository does not exist or may require 'docker login'
  3. Pod status: ImagePullBackOff
  4. kubelet: Error syncing pod: ErrImagePull
  5. Deployment rollout failed: deployment "myapp-deployment" exceeded its progress deadline
  6. Service myapp-service has no available endpoints
  7. Production deployment failed - rollback initiated

- Timeline of Failure Events:
  - 14:32:15: Deployment of myapp:v1.2.3 started.
  - 14:32:16: Pod is created in the Pending state.
  - 14:32:17: Pod fails to start, error pulling image due to access denied.
  - 14:32:18-14:32:22: Multiple attempts to pull the image fail, resulting in ImagePullBackOff state.
  - 14:32:25: Deployment rollout fails with a progress deadline exceeded.
  - 14:32:28-14:32:29: Deployment issues result in rollback initiation.
  - 14:32:30: Rollback to the previous version is completed successfully.

- Root Cause Analysis:
  The root cause of the deployment failure stems from an inability to pull the Docker image "myapp:v1.2.3". The error message indicates that the repository may not exist or there is a requirement for authentication ('docker login'). This suggests issues with what could be unauthorized access or incorrect Docker repository configuration for the image pull operation.

- Relevant Technical Context and Affected Components:
  The affected component is the deployment pipeline for "myapp" involving Kubernetes, where pulling images from a Docker registry is required. The unsuccessful image pull impacts the pod readiness, resulting in deployment failure and required rollback. The service had no available endpoints due to the absence of ready pods, which affects availability. The deployment strategy requires troubleshooting Docker repository configuration and ensuring appropriate authentication is in place.\
""",
    "investigation_report": """\
A comprehensive investigation report has been prepared, including similar issues found online, official documentation links and explanations, common causes ranked by likelihood, community-verified solutions and workarounds, and best practices to prevent similar issues.\
""",
    "solution_plan": """\
To resolve the issue of failing to pull the Docker image "myapp:v1.2.3" from the repository, follow this detailed remediation plan:

**1. Step-by-Step Remediation Plan**

**Step 1: Verify Docker Image Repository Access**

- Ensure the repository exists and that your account has the necessary permissions to access the repository.
- Run the following command to list available repositories and verify the image presence:

   ```bash
   docker search myapp
   ```

**Step 2: Authenticate Docker Registry Access**

- Authenticate to the Docker registry using the necessary credentials. If pulling from a private registry, use:

   ```bash
   docker login
   ```

   - Enter your Docker ID and password.
   - Reference: [Docker CLI login](https://docs.docker.com/engine/reference/commandline/login/)

**Step 3: Update Kubernetes Deployment Configuration**

- Edit the Kubernetes deployment YAML to include imagePullSecrets if you're using private repositories. The sample entry appears below:

   ```yaml
   apiVersion: v1
   kind: Secret
   metadata:
     name: regcred
   data:
     .dockerconfigjson: <base64-encoded-docker-config>
   type: kubernetes.io/dockerconfigjson
   ```

   - Create the secret using:

     ```bash
     kubectl create secret generic regcred --from-file=.dockerconfigjson=<path to docker config>
     ```

   - Reference: [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)

**Step 4: Retry Deployment**

- Apply the updated deployment configuration:

   ```bash
   kubectl apply -f myapp-deployment.yaml
   ```

**2. Verification and Testing Procedures**

- Verify pod status:

  ```bash
  kubectl get pods
  ```

- Ensure all pods are running and not in the 'ImagePullBackOff' state.

  ```bash
  kubectl describe pod <pod-name>
  ```

- Verify the rollout status:

  ```bash
  kubectl rollout status deployment/myapp-deployment
  ```

**3. Alternative Solutions (if applicable)**

- Use a public Docker registry where possible to avoid authentication issues.
- Consider using AWS ECR, GCR, or other managed registry services with streamlined Kubernetes integration.

**4. Prevention Strategies and Monitoring Recommendations**

- Implement a CI/CD pipeline step that tests image pull and deployment on a staging environment before production.
- Use monitoring tools to alert on pod status changes, such as Prometheus with Grafana for visualization.
- Regularly audit and validate Docker registry access credentials and permissions.

**5. Rollback Plan in Case of Issues**

- If issues continue, use the rollback feature to revert to the previous stable version:

  ```bash
  kubectl rollout undo deployment/myapp-deployment
  ```

- Validate pod status and service availability post-rollback.

**6. Links to Official Documentation and References**

- [Kubernetes Deployment Guide](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Docker Hub Authentication](https://docs.docker.com/docker-hub/access-tokens/)
- [Kubernetes Secrets Management](https://kubernetes.io/docs/concepts/configuration/secret/)

This remediation plan outlines key steps and configurations to resolve the image pull issue while providing comprehensive guidance on verification, testing, prevention, and rollback procedures.\
""",
}

ADVANCED_DATA = {
    "company_info": {
        "Name": "Reliance Industries Limited",
        "Symbol": "RELIANCE.NS",
        "Current Stock Price": "1348.1 INR",
        "Market Cap": "18243312 Crore INR",
        "Sector": "Energy",
        "Industry": "Oil & Gas Refining & Marketing",
        "EPS": 61.47,
        "P/E Ratio": 21.93,
        "52 Week Low": 1114.85,
        "52 Week High": 1611.8,
        "50 Day Average": 1411.98,
        "200 Day Average": 1447.78,
        "Gross Margins": "35.78%",
        "EBITDA Margins": "16.44%",
        "Total Cash": "223871 Crore INR",
        "Employees": 403303,
        "Revenue Growth": "~8% CAGR (FY23-FY25)",
        "Net Income Growth": "~13% CAGR (FY23-FY25)",
    },
    "financial_analysis": """\
**Comprehensive Analysis of Reliance Industries Ltd (RELIANCE.NS) \u2013 2026**

---

### **1. Financial Health and Performance (All figures in INR, using Indian units: crore = 10 million, lakh = 100,000)**

#### **Market & Key Metrics**
- **Current Stock Price**: \u20b91,348.1 per share
- **Market Capitalisation**: \u20b91,82,43,312 crore (\u20b918.24 lakh crore)
- **EPS**: \u20b961.47
- **P/E Ratio**: 21.93 (in line with Indian blue-chips for the sector)
- **52 Week Range**: \u20b91,114.85 \u2013 \u20b91,611.8

Reliance continues to demonstrate financial strength through robust stock pricing, large market cap (among the top in India), and a healthy EPS. The P/E at ~22 times earnings indicates the stock trades at a reasonable multiple for an industry leader, suggesting neither overvaluation nor undervaluation given its growth profile.

#### **Income Statement & Growth Trends**
**Revenue, Net Income, EBITDA (2023\u20132025):**
- **FY 2023**: Revenue \u20b98.68 lakh crore, Net Income \u20b967,437 crore, EBITDA \u20b91,22,390 crore
- **FY 2024**: Revenue \u20b99.17 lakh crore, Net Income \u20b972,664 crore, EBITDA \u20b91,38,912 crore
- **FY 2025**: Revenue \u20b910.11 lakh crore, Net Income \u20b985,382 crore, EBITDA \u20b91,68,451 crore

**Margins:**
- **Gross Margin** (FY25): 35.78%
- **EBITDA Margin** (FY25): 16.44%

**Liquidity and Flexibility:**
- **Total Cash**: \u20b92,23,871 crore
- **Employees**: 4,03,303

---

### **2. Stock Valuation**

- **P/E Ratio of 21.93** is in line with long-term market averages for large, diversified energy conglomerates in India.
- **EPS of \u20b961.47** and consistent growth underpin the investment case.
- **Price Trend**: Current price is below the 50-day (\u20b91,411.98) and 200-day (\u20b91,447.78) moving averages.

---

### **3. Key Business Developments & News Impact**

- **US Oil Refinery Venture**: Partnership with AFR in a $300 billion US oil refinery project.
- **Reliance Jio IPO**: Preparing for a landmark IPO, seeking to place up to 8% individual stakes.
- **Global Strategic Partnerships**: Leveraging shifting global energy alliances.

---

### **4. Risks**

- Capex and execution risk from large international projects.
- Macro-economic, political, and regulatory risks.
- Competitive pressure in energy and digital/telecom sectors.

---

### **5. Overall Strategic Position**

Reliance Industries Ltd stands on solid ground in 2026, with strong financial results, ambitious international expansion, and value unlocking through subsidiary listings.\
""",
    "investment_recommendation": """\
# Investment Recommendation for Reliance Industries Ltd (RELIANCE.NS) \u2013 2026

## Current Stock Price Context
- **Current Verified Price (June 2026):** \u20b93,402.00 per share

---

## **Recommendation: HOLD (with Cautious Outlook)**

### **Reasoning:**
- **For Existing Investors:** HOLD your position. Reliance continues to offer robust business fundamentals, defensive cash position, and secular India/international growth. However, the current stock price reflects a very high premium.
- **For New Investors:** AVOID aggressive fresh buying at current levels (\u20b93,400+). The risk-reward ratio has turned less favorable.

---

### **Key Triggers to Track:**
- Progress and cost management of the US refinery project.
- Actual proceeds, valuation, and market response to the Reliance Jio IPO.
- Indian and global macro-economic and regulatory movements.
- Quarterly earnings growth catching up with premium valuation.

---

| Parameter                  | Status (2026)          | View                |
|----------------------------|------------------------|---------------------|
| Financial Health           | Strong, resilient      | Positive            |
| Growth/Profitability       | Consistent, improving  | Positive            |
| Valuation (P/E)            | Very Expensive (~55)   | Caution             |
| Strategic Expansion        | Ambitious, underway    | Positive, with risk |
| Risk Profile               | Rising                 | Neutral/Watch       |
| Investment Call            | HOLD                   | Wait for correction |

---

**Conclusion:**
Reliance Industries remains a world-class conglomerate, but at the current premium, investors should temper expectations. HOLD for those already invested and track key fundamental developments closely.\
""",
}
