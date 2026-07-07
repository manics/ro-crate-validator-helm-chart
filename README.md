# RO-Crate Validator Helm Chart

[![CI](https://github.com/manics/ro-crate-validator-helm-chart/actions/workflows/ci.yaml/badge.svg)](https://github.com/manics/ro-crate-validator-helm-chart/actions/workflows/ci.yaml)

A Helm chart for https://github.com/eScienceLab/RO-Crate-Validation-Service

## Supported features

Deploys RO-Crate Validation service for metadata validation only.
S3 storage is disabled, so the full RO-Crate cannot be validated.

Only the `POST v1/ro_crates/validate_metadata` endpoint is supported.

Minimal Redis and Celery servers are deployed, but for production you are advised to deploy these seperately.

## Deploy

```sh
helm upgrade --install ro-crate-validator ./chart --wait [--values config.yaml]
```

Built-in smoke test

```sh
helm test ro-crate-validator [--timeout=70s]
```
