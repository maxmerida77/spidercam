"""
Punto de entrada principal del sistema.

Uso:
    python scripts/run_pipeline.py --config config/config.yaml
"""
import argparse
import yaml


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()

    with open(args.config, "r") as f:
        config = yaml.safe_load(f)

    # TODO: from spidercam.pipeline import Pipeline
    # Pipeline(config).run(config["video"]["input_path"])
    raise NotImplementedError("Se implementa en Fase 8 (Integración completa)")


if __name__ == "__main__":
    main()
