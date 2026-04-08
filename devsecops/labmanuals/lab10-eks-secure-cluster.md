# Lab 10: Creating a Secure Amazon EKS Cluster

**Difficulty:** Intermediate  
**Estimated time:** 45 minutes

## Prerequisites

- AWS account with permissions for **VPC**, **EKS**, **IAM**, and **CloudWatch Logs** (for control plane logging)
- Familiarity with AWS Regions, subnets, and security groups
- **Important:** EKS control plane and any worker nodes incur **ongoing cost**. Delete the cluster and supporting resources as soon as the lab ends.

## Learning objectives

- Create a VPC suitable for EKS using **VPC and more**
- Create an EKS cluster with a dedicated **cluster IAM role**
- Place the Kubernetes API endpoint in **private** mode and use **private subnets** for the cluster
- Enable **control plane logging** to CloudWatch
- Verify the cluster reaches **Active** state

## Overview

Amazon **EKS** runs the Kubernetes control plane for you. A secure baseline often includes: a proper VPC layout (public and private subnets), restricting the Kubernetes API server endpoint to **private** access so it is not reachable from the public internet, and shipping **control plane logs** to CloudWatch for audit and troubleshooting. This lab uses the console to create `secure-eks-lab` and align with those practices.

## Steps

### 1. Create a VPC

1. Open **VPC** in the console.
2. Choose **Create VPC**.
3. Select **VPC and more** so AWS creates subnets, route tables, and associations automatically.
4. Configure a simple lab topology, for example:
   - **Name tag:** `secure-eks-lab-vpc` (or similar)
   - **IPv4 CIDR:** default or your approved lab range
   - **Availability Zones:** 2
   - **Public subnets:** 2  
   - **Private subnets:** 2  
   - **NAT gateways:** For a minimal cost lab, **None** or **1 per AZ** depending on whether nodes need outbound internet; for **cluster-only** creation without managed nodes in this lab, fewer NATs may suffice—follow your organization’s standard.
5. Choose **Create VPC** and wait until resources show **Available**.

### 2. Create the EKS cluster IAM role

1. Open **IAM** → **Roles** → **Create role**.
2. **Trusted entity:** **AWS service**.
3. **Use case:** **EKS** → **EKS - Cluster** (allows EKS to manage AWS resources on your behalf).
4. Attach the AWS managed policy **AmazonEKSClusterPolicy** (attached automatically for the EKS cluster use case in many consoles).
5. Name the role, for example:

   ```text
   secure-eks-lab-cluster-role
   ```

6. Create the role.

### 3. Create the EKS cluster

1. Open **Amazon EKS** → **Clusters** → **Add cluster** → **Create**.
2. **Name:**

   ```text
   secure-eks-lab
   ```

3. **Cluster IAM role:** Select `secure-eks-lab-cluster-role` (or the name you used).
4. Leave **Kubernetes version** at the recommended default unless you need a specific version.

### 4. Configure networking

1. **VPC:** Select the VPC you created in step 1.
2. **Subnets:** Select **only the two private subnets** created with the VPC (do **not** select the public subnets for the cluster control plane placement in this secure pattern).
3. **Cluster security group:** You may use the **default** security group for the lab if permitted; production setups typically use a dedicated cluster security group with least-privilege rules.
4. **Cluster endpoint access:** Choose **Private** (or **Private only**), so the Kubernetes API is **not** publicly reachable.  
   - **Note:** With a **private-only** endpoint, `kubectl` from your laptop will **not** work until you connect via VPN, Direct Connect, a bastion, or CloudShell from an environment that can reach the private API—this is expected for a locked-down cluster.

### 5. Enable control plane logging

1. In the logging section, enable delivery for:
   - **API server**
   - **Audit**
   - **Authenticator**
   - **Controller manager**
   - **Scheduler**
2. Confirm the cluster IAM role and account can create/use the required **CloudWatch Log groups** (the console usually creates them automatically).

### 6. Review and create

1. Review all settings.
2. Choose **Create**. Cluster creation often takes **10–20 minutes**.

### 7. Verify status

1. Stay on the cluster page until **Status** is **Active**.
2. Confirm **Networking** shows **Private** API endpoint access as configured.

### Reference: `eksctl` alternative

For infrastructure-as-code or repeatability, compare your choices to the sample config in the repo (cluster name and Region in the file may differ from this lab—adjust `metadata.name` and `region` if you use it):

- Repository path: `devsecops/labs/eks/eks-cluster-config.yaml`

The sample enables **private** API access, **public** access off, **private** node networking, and the same **control plane log** types:

```yaml
# Excerpt — see full file in devsecops/labs/eks/eks-cluster-config.yaml
vpc:
  clusterEndpoints:
    privateAccess: true
    publicAccess: false
cloudWatch:
  clusterLogging:
    enableTypes:
      - api
      - audit
      - authenticator
      - controllerManager
      - scheduler
```

## Verification steps

- VPC exists with **two public** and **two private** subnets in at least two AZs.
- EKS cluster `secure-eks-lab` is **Active**.
- Cluster endpoint configuration shows **private** access enabled and **no public** access (if that was your selection).
- In **CloudWatch Logs**, log groups exist for the EKS control plane components you enabled.

## Troubleshooting tips

- **Cluster creation fails on subnets:** Ensure subnets are in **different** AZs and tagged/labeled as expected by EKS in your Region.
- **Cannot reach API with `kubectl`:** Expected for **private-only** endpoints from outside the VPC—use corporate VPN, a jump host inside the VPC, or temporarily relax endpoint settings **only in a non-production lab** if your instructor allows it.
- **High cost:** Remove the cluster and NAT gateways as soon as possible; EKS bills per hour.

## Cleanup

**Order matters.** Remove dependent resources first to avoid stuck states.

1. **Node groups / Fargate profiles:** If you added any, delete them first.
2. **EKS cluster:** Delete `secure-eks-lab`.
3. **IAM:** Delete the cluster role if created only for this lab (detach policies first if needed).
4. **VPC:** Delete NAT gateways (if created), release Elastic IPs, then delete subnets, route tables, internet gateway, and finally the VPC.

Confirm in the **Billing** or **Cost Explorer** after a day that no unexpected EKS or NAT charges remain.

## Summary

You built a VPC for EKS, attached a proper **cluster IAM role**, created `secure-eks-lab` with **private** API endpoint and **private** subnets, and turned on full **control plane logging**—a pattern closer to production security baselines than a public, unlogged cluster.

## Related resources

- [Amazon EKS Security](../docs/advanced/amazon-eks-security.md)
