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

Built-in smoke test, this only checks the chart has been deployed and the validator can respond, it does not verify the validator is sending the correct response.

```sh
helm test ro-crate-validator [--timeout=70s]
```

## Publishing the chart

The default image is `ghcr.io/esciencelab/ro-crate-validation-service-fivesafes-profile`, with the image tag defaulting to `appVersion` in [`chart/Chart.yaml`](chart/Chart.yaml).
Bump `appVersion` to update the default image.

To publish a new release of the Helm chart tag the repository.
This will trigger a [GitHub workflow](.github/workflows/ci.yaml) that automatically sets `version` in [`chart/Chart.yaml`](chart/Chart.yaml) to the GitHub tag, and publishes the chart to a GitHub pages branch.
The `gh-pages` branch must already exist.
