# Amazon EKS Security

*Security concepts for Amazon Elastic Kubernetes Service: architecture, hardening themes, certificate workflows, and IAM integration for workloads—without cluster lab steps.*

---

## What is Amazon EKS?

**Amazon EKS** is a **managed Kubernetes** service. AWS runs and scales the Kubernetes **control plane** (API server, scheduler, controllers, and the backing **etcd** data store in AWS’s responsibility model). You connect **worker capacity**—**managed node groups**, **self-managed nodes**, or **AWS Fargate** profiles—to run **pods**.

EKS’s role is to **reduce operational toil** for the control plane while you remain accountable for **cluster configuration**, **network design**, **workload security**, and **identity** patterns for applications and teams.

---

## EKS architecture (security-relevant)

### Control plane (AWS-managed)

AWS operates highly available **Kubernetes API** endpoints and core control-plane components. You configure **cluster endpoint access** (public/private), **logging**, **version upgrades**, and **add-ons**, but you do not administer control-plane nodes directly.

### Data plane (customer-managed)

**Worker nodes** (or Fargate) run **kubelet**, the **container runtime**, and **your pods**. Compromise of a node or pod can threaten **workloads**, **service accounts**, and—if misconfigured—**cluster credentials**. Harden AMIs, isolate tenants with namespaces and policies, and keep **node** IAM roles minimal.

### VPC networking

The cluster lives in a **VPC**: subnets for nodes and load balancers, **security groups** for the cluster and nodes, and optional **private-only** API endpoints. **CNI** behavior (e.g., ENI-based) affects IP management and **network policy** support depending on add-on choice.

---

## Configuration and vulnerability analysis

- **Cluster configuration:** Audit API server flags (anonymous auth disabled), **audit logging** to CloudWatch, and **secrets encryption** (KMS for etcd secrets).
- **Add-ons:** Keep **VPC CNI**, **kube-proxy**, **CoreDNS**, and **CSI drivers** current; review CVE advisories for Kubernetes and EKS-optimized AMIs.
- **Workload images:** Scan container images in **ECR** or external registries; enforce **admission** policies for image provenance and resource limits.

---

## Security best practices (summary)

| Theme | Practice |
|-------|----------|
| **Private API endpoint** | Restrict Kubernetes API exposure to corporate networks or bastion patterns; avoid unnecessary public endpoints. |
| **Encryption at rest** | Enable **KMS encryption** for etcd-stored Kubernetes secrets where required by policy. |
| **Pod security** | Use **Pod Security Standards** (or equivalent admission controls) to restrict privileged pods, host namespaces, and dangerous capabilities. |
| **Network policies** | Define **Kubernetes NetworkPolicy** (with a CNI that enforces them) to segment workload traffic east-west. |
| **IRSA** | **IAM Roles for Service Accounts** map Kubernetes **service accounts** to **IAM roles** via OIDC—avoid static AWS keys in pods. |

---

## Certificate signing in Kubernetes (concept)

**Certificate Signing** in Kubernetes allows workloads or users to obtain **X.509 client certificates** trusted by the cluster (for kubelet client certs, legacy user auth patterns, or custom integrations).

**What it is:** A **CertificateSigningRequest (CSR)** resource asks the cluster to approve and sign a public key into a certificate, according to cluster **signer** configuration and **approval** workflow.

**Benefits**

- **Strong authentication** for components or users that present client certificates.
- **Short-lived credentials** when combined with rotation and narrow **CN/O** usage.
- **Integration** with organizational PKI in advanced setups (subject to cluster configuration).

**Stages (conceptual)**

1. **CSR creation:** A private key is generated; a CSR object is submitted to the API with the public key and requested identity/usage.
2. **Approval:** A privileged controller or administrator **approves** the CSR if the request is legitimate (policy, identity proof).
3. **Certificate issuance:** The configured **signer** issues the certificate; the requester retrieves the signed cert and uses it per the intended **purpose** (e.g., kubelet client authentication).

Exact signers and approval paths depend on **EKS version** and **configuration**; prefer **IRSA** and **OIDC** for many application use cases on EKS.

---

## Kubernetes service accounts and IRSA

### Service account elements

A **ServiceAccount** is a namespaced identity for pods. Key elements include:

- **Namespace + name** (identity within the cluster).
- **Automount** behavior for API credentials (token projected into pods).
- **Image pull secrets** (optional) for private registries.
- **Annotations** (on EKS) linking to **IAM role** trust for **IRSA**.

### IRSA mapping (IAM Roles for Service Accounts)

1. **OIDC identity provider:** EKS exposes an **OIDC issuer URL** for the cluster.
2. **IAM role trust policy:** The IAM role trusts the OIDC provider and restricts **audience** and **subject** (often `system:serviceaccount:<namespace>:<name>`).
3. **Pod annotation:** `eks.amazonaws.com/role-arn` on the **ServiceAccount** tells the EKS **pod identity webhook** to inject **AWS credentials** (via the **AWS SDK** credential chain) scoped to that role.

Result: applications use **temporary AWS credentials** without long-lived access keys and with **least-privilege IAM** per workload.

---

## Hands-On Labs

- [Lab 10: Secure EKS Cluster](../labmanuals/lab10-eks-secure-cluster.md)

---

Last updated: March 2026
