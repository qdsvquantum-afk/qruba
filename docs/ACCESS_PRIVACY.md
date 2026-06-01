# Access, Privacy and Deployment

Qruba supports cloud access and private Docker deployment.

## Qruba Cloud

Cloud access is intended for demos, pilots, controlled workloads and platform evaluation.

URL:

[https://cloud.qruba.site/](https://cloud.qruba.site/)

Cloud is useful when:

- users want fast access;
- data sensitivity permits cloud processing;
- teams need shared demos;
- API access is required.

## Private Docker Access

Private Docker access is intended for controlled environments where users do not want datasets processed in public cloud infrastructure.

URL:

[https://qruba.site/](https://qruba.site/)

The private node is available only when the local deployment is running.

It is useful when:

- datasets are sensitive;
- a pilot must run locally;
- teams require a private environment;
- large local tests are needed;
- the user wants Docker-backed isolation.

## IBM Token Handling

Qruba can store IBM access tokens when hardware execution is enabled.

The platform is designed so users do not need to paste the token into every workflow. Tokens can be saved, used for backend access and revoked or replaced when needed.

Users should only configure IBM tokens in trusted deployments and should revoke tokens from IBM if they are no longer needed.

## Data Handling

Qruba expects users to avoid uploading sensitive data unless the deployment model is appropriate for that data.

For private or regulated datasets, use the Docker/private deployment path.

## Reliability and Hardware Evidence

Hardware execution can be real but still noisy.

Qruba separates:

- semantic decision;
- hardware reconstructed evidence;
- reliability status;
- final recommended decision.

This helps users avoid treating noisy hardware output as a confirmed business or scientific conclusion.
