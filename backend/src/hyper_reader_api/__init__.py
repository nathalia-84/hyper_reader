def main() -> None:
    """Runs the API locally, reachable from other devices on the LAN."""
    import uvicorn

    uvicorn.run(
        "hyper_reader_api.server:app_from_environment",
        factory=True,
        host="0.0.0.0",
        port=8000,
    )
