"""Make Jaeger Thrift exporter 1.21 importable on OpenTelemetry SDK 1.45."""

import opentelemetry.sdk.environment_variables as otel_env

# The SDK dropped these Jaeger exporter settings. Exporter 1.21 still imports
# them, and each value is the environment variable name.
_JAEGER_ENV_VARS = (
    "OTEL_EXPORTER_JAEGER_AGENT_HOST",
    "OTEL_EXPORTER_JAEGER_AGENT_PORT",
    "OTEL_EXPORTER_JAEGER_AGENT_SPLIT_OVERSIZED_BATCHES",
    "OTEL_EXPORTER_JAEGER_ENDPOINT",
    "OTEL_EXPORTER_JAEGER_PASSWORD",
    "OTEL_EXPORTER_JAEGER_TIMEOUT",
    "OTEL_EXPORTER_JAEGER_USER",
)


def install() -> None:
    """Restore Jaeger environment-variable names removed from the SDK."""
    for name in _JAEGER_ENV_VARS:
        if not hasattr(otel_env, name):
            setattr(otel_env, name, name)


install()
